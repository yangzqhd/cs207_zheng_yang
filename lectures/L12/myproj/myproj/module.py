import numpy as np
class Myproj(object):
    def __add__(self, other):
        """

        :param: teo complex numbers
        :return: float, add real part of two complex numbers
        """
        return self.a + other.a

    def __radd__(self, other):
        """

        :param: teo complex numbers
        :return: float, add conjugate part of two complex numbers
        """
        return self.b + other.b

    def complex_conj(self):
        """

        input: complex number
        :return: conjugate part of a complex number
        """
        return self.b

    def magnitude(self):
        """

        input: complex number
        :return: conjugate part of a complex number
        """
        return np.sqrt(self.a**2 + self.b**2)

    def angle(self):
        """

        input: complex number
        :return: conjugate part of a complex number
        """
        return np.arctan(self.a/self.b)