import pandas as pd
from coldstart.data.splits import cold_start_split
def test_cold_absent_from_train():
    df=pd.DataFrame({"user_id":[1,2,1,3,2,4],"track_id":[10,10,11,12,13,14]})
    train,val,test,cold=cold_start_split(df,[10,11,12,13,14,15],frac=.5,seed=4)
    assert not set(train.track_id)&set(cold)
    assert set(val.track_id)|set(test.track_id)<=set(cold)
