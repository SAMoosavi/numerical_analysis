from polynomial import Polynomial


class Interpolation:
    def __init__(self, points: list[(float, float)]):
        self._points = points.copy()
        self._p: Polynomial = Polynomial([])

    def get_p(self) -> Polynomial:
        return self._p

    def P(self, x: float) -> float:
        return self._p.P(x)
