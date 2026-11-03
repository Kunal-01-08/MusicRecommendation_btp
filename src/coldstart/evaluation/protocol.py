"""Cold-start evaluation protocol interface."""
def evaluate_cold_start(*args: object, **kwargs: object) -> dict[str, float]:
    """Evaluate recommendation quality under the cold-start split."""
    raise NotImplementedError("TODO: implement cold-start evaluation")
