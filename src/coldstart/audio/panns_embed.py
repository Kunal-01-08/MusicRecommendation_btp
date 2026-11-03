"""PANNs embedding interface."""
from pathlib import Path

def extract_embeddings(audio_paths: list[str | Path], batch_size: int = 32, cache_path: str | Path | None = None) -> object:
    """Extract batched PANNs embeddings and optionally cache to NPY."""
    raise NotImplementedError("TODO: implement PANNs embedding extraction")
