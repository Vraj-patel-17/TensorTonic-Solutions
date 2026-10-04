import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a Python float.
    """
    # Write code here
    x=np.asarray(x,dtype=float)
    y=np.asarray(y,dtype=float)
    difference=x-y
    return np.sqrt(np.sum(difference**2))