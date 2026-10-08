import numpy as np

def linear_regression_closed_form(X: list, y: list) -> list:
    """
    Returns the optimal weight vector as a list.
    """
    # Write code here
    X=np.asarray(X,dtype=float)
    Y=np.asarray(y,dtype=float)
    X_T=X.T
    w=np.linalg.inv(X_T @ X) @ (X_T @ Y)
    return w.tolist()
    
    
    