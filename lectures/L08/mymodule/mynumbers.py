import math

# class RealExtensions:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

# class Complex(RealExtensions):
#     def _magnitude(self):
#         return math.sqrt(self.a**2 + self.b**2)

#     def _angle(self):
#         return math.atan(self.b/self.a)
class _Complex(RealExtensions):
    def _magnitude(self):
        return math.sqrt(self.a**2 + self.b**2)

    def _angle(self):
        return math.atan(self.b/self.a)

class Dual(RealExtensions):
    def _magnitude(self):
        return self.a

    def _angle(self):
        return math.atan(self.b/self.a)
