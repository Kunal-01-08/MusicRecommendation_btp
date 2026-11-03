"""Seed helpers."""
import random

def set_seed(seed: int) -> None:
    """Seed Python and optional NumPy/PyTorch RNGs."""
    random.seed(seed)
    try:
        import numpy as np
        np.random.seed(seed)
    except ImportError:
        pass
    try:
        import torch
        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)
    except ImportError:
        pass
