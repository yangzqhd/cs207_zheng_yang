import numpy as np
class Myproj(object):
    def __add__(self, other):
        """

        :param: two complex number objects
        :return: summation of two complex numbers objects
        """
        return self.__init__(self.real + other.real, self.imaginary + other.imaginary)

    def __radd__(self, other):
        """

        :param: teo complex numbers objects
        :return: summation of two complex numbers object
        """
        return self.__init__(self.real + other.real, self.imaginary + other.imaginary)

    def complex_conj(self):
        """

        input: complex number objects
        :return: complex conjugate of a complex number object
        """
        return self.__init__(self.real, 0-self.imaginary)

    def magnitude(self):
        """

        input: complex number objects
        :return: magnitude of a complex number object
        """
        return np.sqrt(self.imaginary**2 + self.real**2)

    def angle(self):
        """

        input: complex number object
        :return: angle of a complex number object
        """
        return np.arctan(self.imaginary/self.real)