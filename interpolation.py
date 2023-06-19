from polynomial import Polynomial


class Interpolation:
    def __init__(self, points: list[(float, float)]):
        self._points = points.copy()
        self._p: Polynomial = Polynomial([])
        self._n = len(points)
        self._s: list = []

    def get_p(self) -> Polynomial:
        return self._p

    def P(self, x: float) -> float:
        return self._p.P(x)

    def _print(self):
        a = ""
        for i in self._s:
            if type(i) == Polynomial:
                a += i.get_str() + ") +"
            else:
                if float(i) < 0:
                    a = a[:-1]
                a += str(i) + "("
        if a != "":
            a = "= " + a
        print(f"P {a[:-1]}= {self._p.get_str()}")
