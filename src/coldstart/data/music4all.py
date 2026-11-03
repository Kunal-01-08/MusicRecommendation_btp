"""Music4All loader interfaces."""
from pathlib import Path
import pandas as pd

def load_tracks(path: str | Path) -> pd.DataFrame:
    """Load track metadata."""
    raise NotImplementedError("TODO: implement track loading")

def load_artists(path: str | Path) -> pd.DataFrame:
    """Load artist metadata."""
    raise NotImplementedError("TODO: implement artist loading")

def load_genres(path: str | Path) -> pd.DataFrame:
    """Load genre and tag metadata."""
    raise NotImplementedError("TODO: implement genre loading")

def load_interactions(path: str | Path) -> pd.DataFrame:
    """Load user-track interactions."""
    raise NotImplementedError("TODO: implement interaction loading")
