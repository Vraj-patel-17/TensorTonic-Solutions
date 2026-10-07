import math

def log_loss(y_true: list, y_pred: list, eps: float = 1e-15) -> list:
    """
    Returns a list of loss values.
    """
    # Write code here
    losses=[]
    for target,probability in zip(y_true,y_pred):
        p_=max(eps,min(1-eps,max(eps,probability)))
        losses.append(-(target * math.log(p_) + (1 - target) * math.log(1 - p_)))
    return losses