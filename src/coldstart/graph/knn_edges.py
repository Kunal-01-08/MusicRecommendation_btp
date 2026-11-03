"""Audio embedding nearest-neighbour edges."""
import numpy as np
def build_audio_knn_edges(embeddings:np.ndarray,k:int,metric:str="cosine")->np.ndarray:
    """Return directed 2xE edges; all supplied tracks, including cold tracks, are queried.

    For a train graph, callers can query cold tracks against a warm-only index.
    FAISS is preferred; exact NumPy fallback supports minimal environments.
    """
    x=np.asarray(embeddings,dtype=np.float32)
    if x.ndim!=2 or not np.isfinite(x).all(): raise ValueError("embeddings must be finite 2-D array")
    n=len(x)
    if not isinstance(k,int) or k<0 or k>=n: raise ValueError("k must satisfy 0 <= k < n")
    if metric not in {"cosine","l2"}: raise ValueError("metric must be cosine or l2")
    if k==0: return np.empty((2,0),dtype=np.int64)
    y=x.copy()
    if metric=="cosine": y/=np.maximum(np.linalg.norm(y,axis=1,keepdims=True),np.finfo(np.float32).eps)
    try:
        import faiss
        index=faiss.IndexFlatIP(x.shape[1]) if metric=="cosine" else faiss.IndexFlatL2(x.shape[1]); index.add(y)
        _, neighbours=index.search(y,n)
    except ImportError:
        score=y@y.T if metric=="cosine" else -((x[:,None]-x[None,:])**2).sum(axis=2)
        neighbours=np.argsort(-score,axis=1)
    edges=[(i,int(j)) for i,row in enumerate(neighbours) for j in row if int(j)!=i][:]
    edges=[(i,int(j)) for i,row in enumerate(neighbours) for j in [v for v in row if int(v)!=i][:k]]
    return np.asarray(edges,dtype=np.int64).T
