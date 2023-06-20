class SystemOfLinearEquations:
    def __init__(self, a: list[list[int]], b: list[int], start: list[int]):
        self.__a = a.copy()
        i = 0
        for _ in a:
            i += 1
        if len(b) != i:
            raise "not correct size!"
        self.__b = b
        if len(start) != len(self.__a):
            raise "not correct size!"
        self.__start = start

    def gauss_seidel(self):
        s1 = self.__start.copy()
        s2 = self.__start.copy()
        w = True
        n = 0
        while w:
            w = False
            for i in range(len(self.__a)):
                x = 0
                for j in range(len(self.__a[i])):
                    if i != j:
                        x -= self.__a[i][j] * s2[j]
                s2[i] = (x + self.__b[i]) / self.__a[i][i]

            for i in range(len(s1)):
                if not -0.0001 < s1[i] - s2[i] < 0.0001:
                    w = True
                    break
            if n == 1e5:
                return [round(i, 4) for i in s2]
            s1 = s2.copy()
            n += 1
        return [round(i, 4) for i in s2]

    def jacobi(self):
        s1 = self.__start.copy()
        s2 = self.__start.copy()
        w = True
        n = 0
        while w:
            w = False
            for i in range(len(self.__a)):
                x = 0
                for j in range(len(self.__a[i])):
                    if i != j:
                        x -= self.__a[i][j] * s1[j]
                s2[i] = (x + self.__b[i]) / self.__a[i][i]

            for i in range(len(s1)):
                if not -0.0001 < s1[i] - s2[i] < 0.0001:
                    w = True
                    break
            if n == 1e5:
                return [round(i, 4) for i in s2]
            s1 = s2.copy()
        return [round(i, 4) for i in s2]
