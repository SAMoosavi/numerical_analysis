import sympy as sp

class Interpolation:
    def __init__(self, points: list[(float, float)]):
        self._points = points.copy()
        self._x = sp.Symbol('x')
        self._p: sp.Expr = (self._x - self._x).simplify()
        self._n = len(points)

    def get_p(self) -> sp.Expr:
        return self._p.simplify()

    def P(self, x: float) -> float:
        return round(self._p.evalf(subs={self._x: x}), 4)

    def _print(self):
        print(f"P = {self._p} = {self.get_p()}")
