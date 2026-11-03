"""Cold-start interaction splits."""
from typing import Any
import numpy as np
import pandas as pd

def cold_start_split(interactions_df: pd.DataFrame, track_ids: list[Any], frac: float = 0.15, seed: int = 42, stratify_by_popularity: bool = True) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, list[Any]]:
    """Hold out cold tracks and split their interactions between validation/test.

    Every interaction for each held out track is excluded from training.
    Popularity stratification samples approximately proportionally across quantile bins.
    """
    if not 0 <= frac <= 1:
        raise ValueError("frac must be between 0 and 1")
    if "track_id" not in interactions_df:
        raise ValueError("interactions_df must contain track_id")
    ids = list(dict.fromkeys(track_ids))
    count = round(len(ids) * frac)
    rng = np.random.default_rng(seed)
    if stratify_by_popularity and count and ids:
        popularity = interactions_df.track_id.value_counts().reindex(ids, fill_value=0)
        bins = pd.qcut(popularity.rank(method="first"), q=min(5, len(ids)), labels=False, duplicates="drop")
        groups = pd.DataFrame({"track": ids, "bin": bins.to_numpy()}).groupby("bin", sort=True)
        allocations = {key: int(count * len(group) / len(ids)) for key, group in groups}
        remainder = count - sum(allocations.values())
        for key, group in groups:
            extra = min(remainder, len(group) - allocations[key])
            allocations[key] += extra
            remainder -= extra
        cold = []
        for key, group in groups:
            cold.extend(rng.choice(group.track.to_numpy(), size=allocations[key], replace=False).tolist())
    else:
        cold = rng.choice(ids, size=count, replace=False).tolist() if count else []
    cold_rows = interactions_df[interactions_df.track_id.isin(cold)]
    train = interactions_df[~interactions_df.track_id.isin(cold)].copy()
    order = rng.permutation(len(cold_rows))
    cut = len(order) // 2
    val = cold_rows.iloc[order[cut:]].copy().reset_index(drop=True)
    test = cold_rows.iloc[order[:cut]].copy().reset_index(drop=True)
    return train.reset_index(drop=True), val, test, list(cold)
