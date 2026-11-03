"""Optional raag label interfaces."""
from pathlib import Path
import pandas as pd

def load_raag_labels(path: str | Path) -> pd.DataFrame:
    """Load optional track-to-raag labels."""
    raise NotImplementedError("TODO: implement raag label loading")

def predict_raag(audio_path: str | Path) -> str:
    """Predict a raag when curated labels are unavailable."""
    raise NotImplementedError("TODO: implement predicted-raag fallback")
