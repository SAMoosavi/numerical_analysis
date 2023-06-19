import math

import sympy as sp


class Derivation:
    def __init__(self, stop: float, f: sp.Expr, x: sp.Symbol):
        self.__stop = stop
        self.__n = math.log10(stop)
        if self.__stop < 1:
            self.__n = -self.__n
        self.__n = int(self.__n)
        self.__f = f
        self.__x = x

    def bisection_method(self, a, b) -> float:
        d1 = d2 = a
        while True:
            start = self.__f.evalf(subs={self.__x: a})
            end = self.__f.evalf(subs={self.__x: b})
            if start * end >= 0:
                raise "a,b isn't correct"

            d2 = (a + b) / 2
            mid = self.__f.evalf(subs={self.__x: d2})
            if -self.__stop < d1 - d2 < self.__stop or mid == 0:
                return round(d2, self.__n)
            if start * mid < 0:
                b = d2
            else:
                a = d2
            d1 = d2

    def newton_raphson(self, start) -> float:
        n1 = n2 = start

        diff = sp.diff(self.__f, self.__x)
        while True:
            n2 = n1 - self.__f.evalf(subs={self.__x: n1}) / diff.evalf(subs={self.__x: n1})
            if -self.__stop < n2 - n1 < self.__stop:
                return round(n2, self.__n)
            n1 = n2

    def regula_falsi(self, a, b):
        if self.__f.evalf(subs={self.__x: a}) * self.__f.evalf(subs={self.__x: b}) >= 0:
            raise "You have not assumed right a and b"
        c1 = c2 = a
        while True:
            c2 = (a * self.__f.evalf(subs={self.__x: b}) - b * self.__f.evalf(subs={self.__x: a})) / (
                    self.__f.evalf(subs={self.__x: b}) - self.__f.evalf(subs={self.__x: a}))

            if -self.__stop < c1 - c2 < self.__stop or self.__f.evalf(subs={self.__x: c2}) == 0:
                return round(c2, self.__n)

            if self.__f.evalf(subs={self.__x: c2}) * self.__f.evalf(subs={self.__x: a}) < 0:
                b = c2
            else:
                a = c2
            c1 = c2

    def secant(self, a, b):
        if self.__f.evalf(subs={self.__x: a}) * self.__f.evalf(subs={self.__x: b}) >= 0:
            raise "Secant method fails."
        n1 = n2 = a
        while True:
            n2 = a - self.__f.evalf(subs={self.__x: a}) * (b - a) / (
                    self.__f.evalf(subs={self.__x: b}) - self.__f.evalf(subs={self.__x: a}))
            fn = self.__f.evalf(subs={self.__x: n2})
            if -self.__stop < n1 - n2 < self.__stop or fn == 0:
                return round(n2, self.__n)
            if self.__f.evalf(subs={self.__x: a}) * fn < 0:
                b = n2
            elif self.__f.evalf(subs={self.__x: b}) * fn < 0:
                a = n2
            else:
                raise "Secant method fails."

            n1 = n2
