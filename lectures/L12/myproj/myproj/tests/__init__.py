import doctest

class Tests(object):
    def __init__(self):
        doctest.testmod(module, verbose=True)
