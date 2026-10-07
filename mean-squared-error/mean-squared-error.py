import numpy as np

def mean_squared_error(y_pred: list, y_true: list) -> float:
    """
    Returns the error as a float.
    """
    # Write code here
    y_pred=np.asarray(y_pred,dtype=float)
    y_true=np.asarray(y_true,dtype=float)
    N=y_pred.shape[0]
    return float((np.sum(np.square(y_pred-y_true)))/N)