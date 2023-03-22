from lagrange import Lagrange
from neville import Neville
from newton import Newton

points = [(1, 5), (2, 0), (3, 5)]

neville = Neville(points)
neville.get_p().print()
print(neville.P(1.5))

newton = Newton(points)
newton.get_p().print()
print(newton.P(1.5))

lagrange = Lagrange(points)
lagrange.get_p().print()
print(lagrange.P(1.5))
