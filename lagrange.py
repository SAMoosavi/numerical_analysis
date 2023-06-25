from interpolation import Interpolation
import sympy as sp


class Lagrange(Interpolation):
    def __init__(self, points: list[(float, float)]):
        super().__init__(points)
        self.__l: sp.Expr = 1
        self.__calculate_l()
        self.__li: list[sp.Expr] = [1] * self._n
        self.__lli: list[sp.Expr] = [1] * self._n
        self.__calculate_li()
        self.__calculate_p()
        self.__print()

    def __calculate_l(self) -> None:
        for i in self._points:
            self.__l = self.__l * (self._x - i[0])

    def __calculate_li(self) -> None:
        for i, val in enumerate(self._points):
            self.__lli[i] = (self.__l / (self._x - val[0])).simplify()
            self.__li[i] = self.__lli[i] / (self.__lli[i].evalf(subs={self._x: val[0]}))

    def __calculate_p(self) -> None:
        for i, val in enumerate(self._points):
            self._p += self.__li[i] * val[1]

    def __print(self):
        print("================================")
        print("Lagrange")
        for i, val in enumerate(self._points):
            print(
                f"L{val} = ({self.__lli[i]}) / {round(self.__lli[i].evalf(subs={self._x: val[0]}), 4)} = {self.__li[i].simplify()}")
        self._print()
        print("================================")
