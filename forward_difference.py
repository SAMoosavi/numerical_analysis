from interpolation import Interpolation
from polynomial import Polynomial


class ForwardDifference(Interpolation):
    def __init__(self, points: list[(float, float)]):
        super().__init__(points)
        self.__ni: list[Polynomial] = [Polynomial([1])] * (len(self._points))
