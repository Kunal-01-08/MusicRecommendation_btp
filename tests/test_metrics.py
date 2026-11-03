import math
from coldstart.evaluation.metrics import ndcg_at_k,recall_at_k
def test_metrics_hand_computed():
    assert recall_at_k(["a","x","b"],{"a","b","c"},2)==1/3
    assert abs(ndcg_at_k(["a","x","b"],{"a","b"},2)-1/(1+1/math.log2(3)))<1e-12
def test_empty_relevant():
    assert recall_at_k([],set(),3)==0 and ndcg_at_k([],set(),3)==0
