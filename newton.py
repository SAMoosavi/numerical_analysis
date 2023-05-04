from interpolation import Interpolation
from polynomial import Polynomial


class Newton(Interpolation):
    def __init__(self, points: list[(float, float)]):
        super().__init__(points)
        self.__ni: list[Polynomial] = [Polynomial([1])] * (len(self._points))
        self.__calculate_ni()
        self.__calculate_n()

    def __calculate_ni(self) -> None:
        for i in range(len(self._points) - 1):
            self.__ni[i + 1] = self.__ni[i].product(Polynomial([1, -self._points[i][0]]))

    def __calculate_ai(self, start: int, end: int) -> Polynomial:
        if start == end:
            return Polynomial([self._points[start][1]])
        elif end - start == 1:
            return Polynomial([(self._points[end][1] - self._points[start][1]) /
                               (self._points[end][0] - self._points[start][0])])
        else:
            return self.__calculate_ai(start + 1, end) \
                .subtraction(self.__calculate_ai(start, end - 1)) \
                .quotient(Polynomial([(self._points[end][0] - self._points[start][0])]))[0]

    def __calculate_n(self):
        for i, ni in enumerate(self.__ni):
            self._p = self._p.sum(ni.product(self.__calculate_ai(0, i)))