import sympy as sp
from integral import Integral
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
derivation = Derivation(0.0001, x ** 3, x)
print(derivation.bisection_method(-1, 1))
print(derivation.newton_raphson(1))
print(derivation.regula_falsi(-1, 1))
print(derivation.secant(-1, 1))

integral = Integral(x ** 3, x, 0, 10)
print(integral.trapeziums(10))
print(integral.simson(10))
print(integral.ramberg(10))
