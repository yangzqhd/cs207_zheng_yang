import numpy as np
<<<<<<< HEAD
def L2(v, *args):
    """Returns the weighted L2 norm of a vector
    
    INPUTS
    =======
    v: list, vector to be calculated
    *arg: list, a vector of weights, same length as the input vector
    
    RETURNS
    ========
    weighted L2 norm: float
=======

def L2(v, *args):
    """Compute the weighted L2 norm.
    
    INPUTS
    =======
    v: a list of floats
    args: a list of variable input arguments
       args[0]: a list of weights, floats
    
    RETURNS
    ========
    s: the weighted L2 norm of the input v
>>>>>>> cbdd711a503cadd47ce71efd2c3c1327e1ab6f76

    NOTES
    =====
    PRE: 
<<<<<<< HEAD
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
=======
         - v is a list of floats
         - the weights are stored in args[0]
    POST:
         - a, b, and c are not changed by this function
         - raises a ValueError exception if len(v) .ne. len(args[0])
         - returns a float

    EXAMPLES
    =========
    >>> L2([3.0, 4.0], [1.0, 2.0])
    8.54400374531753
    """
    
>>>>>>> cbdd711a503cadd47ce71efd2c3c1327e1ab6f76
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
<<<<<<< HEAD
    return np.sqrt(s)
=======
    return np.sqrt(s)
>>>>>>> cbdd711a503cadd47ce71efd2c3c1327e1ab6f76
