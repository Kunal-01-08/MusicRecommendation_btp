"""Recommendation loss interfaces."""
def bpr_loss(positive_scores: object, negative_scores: object) -> object:
    """Compute pairwise Bayesian personalized ranking loss."""
    raise NotImplementedError("TODO: implement BPR loss")
def bce_loss(scores: object, labels: object) -> object:
    """Compute binary cross-entropy loss."""
    raise NotImplementedError("TODO: implement BCE loss")
