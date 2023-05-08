from prettytable import PrettyTable
from interpolation import Interpolation
from polynomial import Polynomial


class Newton(Interpolation):
    def __init__(self, points: list[(float, float)]):
        super().__init__(points)
        self.__ni: list[Polynomial] = [Polynomial([1])] * (len(self._points))
        self.__calculate_ni()
        self.__calculate_n()
        self.__print()

    def __calculate_ni(self) -> None:
        for i in range(len(self._points) - 1):
            self.__ni[i + 1] = self.__ni[i].product(Polynomial([1, -self._points[i][0]]))

    def __calculate_ai(self, start: int, end: int) -> float:
        if start == end:
            return self._points[start][1]
        else:
            numerator = self.__calculate_ai(start + 1, end) - self.__calculate_ai(start, end - 1)
            denominator = self._points[end][0] - self._points[start][0]
            return numerator / denominator

    def __calculate_n(self):
        a = [0.0] * len(self.__ni)
        for i in range(len(a)):
            a[i] = self.__calculate_ai(0, i)
        for i, ni in enumerate(self.__ni):
            self._s.append(a[i])
            self._s.append(ni)
            self._p = self._p.sum(ni.product(Polynomial([a[i]])))

    def __print(self):
        print("================================")
        print("Newton")
        print("f[i, j] = (f[(i + 1), j] - f[i, (j - 1)]) / (x_j - x_i)")
        table = PrettyTable()
        for n in range(self._n):
            col = []
            for i in range(n):
                col.append("")
            for i in range(self._n - n):
                col.append(self.__calculate_ai(i, i + n))
                col.append("")
            for i in range(n):
                col.append("")
            col.pop()
            header = "f[i"
            if n != 0:
                header += f", i + {n}"
            header += "]"
            table.add_column(header, col, align='c')
        print(table)
        self._print()
        print("================================")
