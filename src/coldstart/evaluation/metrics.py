"""Ranking metrics."""
import math
from collections.abc import Sequence
from typing import TypeVar
T=TypeVar("T")
def recall_at_k(recommended: Sequence[T], relevant: set[T] | Sequence[T], k: int) -> float:
    """Binary Recall@k; empty targets return zero."""
    if k < 0: raise ValueError("k must be non-negative")
    target=set(relevant)
    return len(set(recommended[:k]) & target)/len(target) if target else 0.0
def ndcg_at_k(recommended: Sequence[T], relevant: set[T] | Sequence[T], k: int) -> float:
    """Binary NDCG@k; empty targets return zero."""
    if k < 0: raise ValueError("k must be non-negative")
    target=set(relevant)
    if not target: return 0.0
    dcg=sum(1/math.log2(i+2) for i,x in enumerate(recommended[:k]) if x in target)
    ideal=sum(1/math.log2(i+2) for i in range(min(k,len(target))))
    return dcg/ideal if ideal else 0.0
