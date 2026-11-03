"""Log-mel feature extraction interface."""
from pathlib import Path

def extract_log_mel(audio_path: str | Path, sample_rate: int = 32000, mel_bins: int = 64) -> object:
    """Extract a log-mel spectrogram."""
    raise NotImplementedError("TODO: implement log-mel extraction")
