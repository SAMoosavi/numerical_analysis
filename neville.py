from interpolation import Interpolation
from polynomial import Polynomial


class Neville(Interpolation):
    def __init__(self, points: list[(float, float)]):
        super().__init__(points)
        self._p = self.__calculate(0, len(self._points) - 1)
        self.__print()

    def __calculate(self, start: int, end: int) -> Polynomial:
        if start == end:
            return Polynomial([self._points[start][1]])
        else:
            a = Polynomial([1, -self._points[start][0]]).product(self.__calculate(start + 1, end))
            b = Polynomial([1, -self._points[end][0]]).product(self.__calculate(start, end - 1))
            c = Polynomial([self._points[end][0] - self._points[start][0]])
            return a.subtraction(b).quotient(c)[0]

    def __print(self):
        print("================================")
        print("Neville")
        self._print()
        print("================================")