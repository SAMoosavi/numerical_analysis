import sympy as sp

from forward_difference import ForwardDifference
from backward_difference import BackwardDifference
from lagrange import Lagrange
from neville import Neville
from newton import Newton
from derivation import Derivation

points = [(-1, 0), (0, -1), (1, 0)]

backward_difference = BackwardDifference(points)
print(backward_difference.P(1.5))

forward_difference = ForwardDifference(points)
print(forward_difference.P(1.5))

neville = Neville(points)
print(neville.P(1.5))

newton = Newton(points)
print(newton.P(1.5))

lagrange = Lagrange(points)
print(lagrange.P(1.5))

x = sp.Symbol('x')
a = sp.sin((((x ** 5 + 5) ** 2) / x ** 6) ** 2) * sp.tan(x)
derivation = Derivation(0.0001, a, x)
b = derivation.bisection_method(1.2, 1.5)
print(b)
b = derivation.newton_raphson(1.5)
print(b)
b = derivation.regula_falsi(1.2, 1.5)
print(b)
b = derivation.secant(1.2, 1.5)
print(b)
