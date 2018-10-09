import numpy as np
def L2(v, *args):
    """Returns the weighted L2 norm of a vector
    
    INPUTS
    =======
    v: list, vector to be calculated
    *arg: list, a vector of weights, same length as the input vector
    
    RETURNS
    ========
    weighted L2 norm: float

    NOTES
    =====
    PRE: 
         - v, *args are arrays
    POST:
         - v and *arg are not changed by this function
         - treat vector of weights as ones, if not given that argument
         - raises a ValueError exception if lengths of the vector and the vector of weights(*args) are not same
         - returns the weighted L2 norm of the input vector

    EXAMPLES
    =========
    >>> L2([3, 4], [2, 2])
    10.0
    """
    s = 0.0 # Initialize sum
    if len(args) == 0: # No weight vector
        for vi in v:
            s += vi * vi
    else: # Weight vector present
        w = args[0] # Get the weight vector
        if (len(w) != len(v)): # Check lengths of lists
            raise ValueError("Length of list of weights must match length of target list.")
        for i, vi in enumerate(v):
            s += w[i] * w[i] * vi * vi
    return np.sqrt(s)