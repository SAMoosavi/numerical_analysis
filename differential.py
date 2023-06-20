import sympy as sp


class Differential:
    def __init__(self, f: sp.Expr, y: sp.Symbol, t: sp.Symbol, a, b, w, n):
        self.__f = f
        self.__t = t
        self.__y = y
        self.__a = a
        self.__b = b
        self.__w = w
        self.__n = n

    def euler(self):
        a = self.__a
        h = (self.__b - a) / self.__n
        w = self.__w
        r = [[a, w]]
        while a + h < self.__b:
            w = w + h * self.__f.evalf(subs={self.__t: a, self.__y: w})
            a += h
            r.append([round(a, 4), round(w, 4)])
        return r

    def runge_kutta(self):
        t = self.__a
        h = (self.__b - t) / self.__n
        w = self.__w
        r = [[t, w]]
        while t + h < self.__b:
            k1 = h * self.__f.evalf(subs={self.__t: t, self.__y: w})
            k2 = h * self.__f.evalf(subs={self.__t: t + h / 2, self.__y: w + k1 / 2})
            k3 = h * self.__f.evalf(subs={self.__t: t + h / 2, self.__y: w + k2 / 2})
            k4 = h * self.__f.evalf(subs={self.__t: t + h, self.__y: w + k3})
            w = w + (k1 + 2 * k2 + 2 * k3 + k4) / 6
            t += h
            r.append([round(t, 4), round(w, 4)])
        return r
