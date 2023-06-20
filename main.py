import sympy as sp
from integral import Integral
from forward_difference import ForwardDifference
from backward_difference import BackwardDifference
from lagrange import Lagrange
from neville import Neville
from newton import Newton
from derivation import Derivation
from system_of_linear_equations import SystemOfLinearEquations
from differential import Differential

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

system_of_linear_equations = SystemOfLinearEquations([[10, -1, 2, 0], [-1, 11, -1, 3], [2, -1, 10, -1], [0, 3, -3, 8]],
                                                     [6, 25, -11, 15], [0, 0, 0, 0])
print(system_of_linear_equations.gauss_seidel())
print(system_of_linear_equations.jacobi())

y = sp.Symbol('y')
t = sp.Symbol('t')
differential = Differential(-y + t + 1, y, t, 0, 1, 1, 10)
print(differential.euler())
print(differential.runge_kutta())
