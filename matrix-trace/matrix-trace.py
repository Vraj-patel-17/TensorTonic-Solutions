import numpy as np

def matrix_trace(A: list) -> float:
    """
    Returns the trace as a float.
    """
    # Write code here
    n=len(A)
    trace=0
    for i in range(n):
        trace+=A[i][i]
    return float(trace)