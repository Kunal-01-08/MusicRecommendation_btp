from coldstart.evaluation.longtail import catalogue_coverage,head_tail_split,mean_popularity,tail_share_at_k
def test_longtail():
    h,t=head_tail_split({"a":10,"b":5,"c":1,"d":0},.5)
    assert h=={"a","b"} and t=={"c","d"}
    assert tail_share_at_k(["c","a","d"],t,2)==.5
    assert catalogue_coverage([["a","c"],["b"]],{"a","b","c","d"},1)==.5
    assert mean_popularity(["a","c"],{"a":10,"c":2},2)==6
