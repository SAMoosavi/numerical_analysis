from interpolation import Interpolation
from polynomial import Polynomial


class ForwardDifference(Interpolation):
    def __init__(self, points: list[(float, float)]):
        super().__init__(points)
        self.__ni: list[Polynomial] = [Polynomial([1])] * (len(self._points))
        self.__calculate_ni()
        self._p = Polynomial([0])
        self.__calculate_p()

    def __calculate_nfi(self, n: int, i: int):
        a = 0
        if n == 0:
            a = self._points[i][1]
        else:
            a = self.__calculate_nfi(n - 1, i + 1) - self.__calculate_nfi(n - 1, i)
        print(f"{n}f{i} = {a}")
        return a

    def __calculate_ni(self):
        t, _ = Polynomial([1, -self._points[0][0]]).quotient(Polynomial(
            [self._points[1][0] - self._points[0][0]]))
        for i in range(1, len(self.__ni)):
            self.__ni[i], _ = self.__ni[i - 1].product(t.subtraction(Polynomial([i - 1]))).quotient(Polynomial([i]))

    def __calculate_p(self):
        ai: list[float] = [0] * len(self.__ni)
        for i in range(len(self.__ni)):
            ai[i] = self.__calculate_nfi(i, 0)
        print("P = ", end='')
        for i, val in enumerate(self.__ni):
            print(ai[i], end='')
            print(" ( ", end='')
            val.print()
            print(" ) + ", end='')
            self._p = self._p.sum(val.product(Polynomial([ai[i]])))
        print()
