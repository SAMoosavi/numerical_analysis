from polynomial import Polynomial
from interpolation import Interpolation


class Lagrange(Interpolation):
    def __init__(self, points: list[(float, float)]):
        super().__init__(points)
        self.__l = Polynomial([1])
        self.__calculate_l()
        self.__li: list[Polynomial] = [Polynomial([1])] * len(points)
        self.__calculate_li()
        self._p = Polynomial([0])
        self.__calculate_p()
        self.__print()

    def __calculate_l(self) -> None:
        for i in self._points:
            self.__l = self.__l.product(Polynomial([1, -i[0]]))

    def __calculate_li(self) -> None:
        for i, val in enumerate(self._points):
            self.__li[i], _ = self.__l.quotient(Polynomial([1, -val[0]]))
            self.__li[i], _ = self.__li[i].quotient(Polynomial([self.__li[i].P(val[0])]))

    def __calculate_p(self) -> None:
        for i, val in enumerate(self._points):
            self._s.append(val[1])
            self._s.append(self.__li[i])
            self.__li[i].product(Polynomial([val[1]]))
            self._p = self._p.sum(self.__li[i].product(Polynomial([val[1]])))

    def __print(self):
        print("================================")
        print("Lagrange")
        for i, val in enumerate(self._points):
            print(f"{val} =({self.__li[i].get_str()}) / {self.__li[i].P(val[0])} = {self.__li[i].get_str()}")
        self._print()
        print("================================")