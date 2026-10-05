import numpy as np

def make_diagonal(v: list) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, N).
    """
    # Write code here
    n=len(v)
    k=0
    array=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if i==j:
                array[i][j]=v[k]
                k+=1
    return array