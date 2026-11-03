"""Long-tail metrics."""
from collections.abc import Sequence
from typing import TypeVar
T=TypeVar("T")
def head_tail_split(popularity: dict[T,int], head_fraction: float=.2)->tuple[set[T],set[T]]:
    """Split catalog into most popular head and remaining tail."""
    if not 0<=head_fraction<=1: raise ValueError("head_fraction must be in [0,1]")
    items=sorted(popularity,key=lambda x:(-popularity[x],str(x))); n=int(len(items)*head_fraction+.5)
    return set(items[:n]),set(items[n:])
def tail_share_at_k(recommended: Sequence[T],tail_items:set[T],k:int)->float:
    """Tail share of a ranked list top-k."""
    if k<0: raise ValueError("k must be non-negative")
    top=recommended[:k]; return sum(x in tail_items for x in top)/len(top) if top else 0.0
def catalogue_coverage(recommendations:Sequence[Sequence[T]],catalogue:set[T]|Sequence[T],k:int)->float:
    """Fraction of catalogue recommended across top-k lists."""
    if k<0: raise ValueError("k must be non-negative")
    items=set(catalogue); seen={x for row in recommendations for x in row[:k] if x in items}
    return len(seen)/len(items) if items else 0.0
def mean_popularity(recommended:Sequence[T],popularity:dict[T,int],k:int)->float:
    """Mean popularity of top-k recommendations."""
    if k<0: raise ValueError("k must be non-negative")
    top=recommended[:k]; return sum(popularity.get(x,0) for x in top)/len(top) if top else 0.0
