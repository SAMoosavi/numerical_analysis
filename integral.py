import sympy as sp


class Integral:
    def __init__(self, f: sp.Expr, x: sp.Symbol, start, end):
        self.__f = f
        self.__x = x
        self.__start = start
        self.__end = end

    def trapeziums(self, n: int):
        h = (self.__end - self.__start) / n
        x1 = self.__start
        x2 = x1 + h
        r = 0
        while x2 <= self.__end:
            r += (self.__f.evalf(subs={self.__x: x1}) + self.__f.evalf(subs={self.__x: x2})) * h / 2
            x1 = x2
            x2 += h
        return round(r, 4)

    def simson(self, n):
        h = (self.__end - self.__start) / n
        x1 = self.__start
        x2 = x1 + h + h
        r = 0
        while x2 <= self.__end:
            r += (self.__f.evalf(subs={self.__x: x1}) + 4 * self.__f.evalf(subs={self.__x: (x1 + h)}) + self.__f.evalf(
                subs={self.__x: x2})) * h / 3
            x1 = x2
            x2 += h + h
        return round(r, 4)

    def ramberg(self, n):
        return round((4 * self.trapeziums(2 * n) - self.trapeziums(n)) / 3, 4)
