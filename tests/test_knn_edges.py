import numpy as np
from coldstart.graph.knn_edges import build_audio_knn_edges
def test_knn_edges():
    x=np.array([[1,0],[.9,.1],[0,1],[-1,0]],dtype=np.float32); e=build_audio_knn_edges(x,2)
    assert e.shape==(2,8) and not np.any(e[0]==e[1])
    assert np.all(np.bincount(e[0],minlength=4)==2)
