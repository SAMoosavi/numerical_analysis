from forward_difference import ForwardDifference
from backward_difference import BackwardDifference
from lagrange import Lagrange
from neville import Neville
from newton import Newton

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
