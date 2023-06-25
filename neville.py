from interpolation import Interpolation


class Neville(Interpolation):
    def __init__(self, points: list[(float, float)]):
        super().__init__(points)
        self._p = self.__calculate(0, self._n - 1)
        self.__print()

    def __calculate(self, start: int, end: int):
        if start == end:
            return self._points[start][1]
        else:
            a = (self._x - self._points[start][0]) * self.__calculate(start + 1, end)
            b = (self._x - self._points[end][0]) * self.__calculate(start, end - 1)
            c = self._points[end][0] - self._points[start][0]
            return (a - b) / c

    def __print(self):
        print("================================")
        print("Neville")
        self._print()
        print("================================")
