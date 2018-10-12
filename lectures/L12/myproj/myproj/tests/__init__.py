import doctest
import myproj

class Tests(object):
    def __init__(self):
        doctest.testmod(myproj.module.magnitude, verbose=True)

