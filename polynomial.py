class Polynomial:
    def __init__(self, a: list[float]):
        self.a = a[::-1]

    def sum(self, other) -> 'Polynomial':
        if type(other) != Polynomial:
            other = Polynomial([other])
        deg = max(len(other.a), len(self.a))
        new_a = [0.0] * deg
        for i in range(deg):
            if i < len(self.a):
                new_a[i] += self.a[i]
            if i < len(other.a):
                new_a[i] += other.a[i]
        return Polynomial(new_a[::-1])

    def subtraction(self, other) -> 'Polynomial':
        if type(other) != Polynomial:
            other = Polynomial([other])
        deg = max(len(other.a), len(self.a))
        new_a = [0.0] * deg
        for i in range(deg):
            if i < len(self.a):
                new_a[i] += self.a[i]
            if i < len(other.a):
                new_a[i] -= other.a[i]
        return Polynomial(new_a[::-1])

    def product(self, other) -> 'Polynomial':
        if type(other) != Polynomial:
            other = Polynomial([other])
        new_a = [0.0] * (len(self.a) + len(other.a) - 1)
        for i, x in enumerate(self.a):
            for j, y in enumerate(other.a):
                new_a[i + j] += x * y
        return Polynomial(new_a[::-1])

    def quotient(self, other) -> ('Polynomial', 'Polynomial'):
        if type(other) != Polynomial:
            other = Polynomial([other])
        a_copy = self.a[::-1]
        if len(a_copy) < len(other.a):
            raise ValueError
        deg = len(a_copy) - len(other.a) + 1
        q = [0.0] * deg
        j = deg
        for i in range(deg):
            q[i] = a_copy[i] / other.a[-1]
            a = [0.0] * j
            a[0] = q[i]
            p1 = Polynomial(a)
            p2 = other.product(p1)
            p3 = Polynomial(a_copy)
            a_copy = p3.subtraction(p2).a[::-1]
            j -= 1

        return Polynomial(q), Polynomial(a_copy)

    def get_str(self) -> str:
        r: list[str] = []
        for i, val in enumerate(self.a):
            s = ""
            val = round(val, 4)
            if val != 0:
                if val > 0:
                    s = "+"
                if val != 1:
                    if val == -1:
                        s = "-"
                    else:
                        s = f"{s}{int(val) if val == val // 1 else val}"
                if i == 0:
                    if val == 1 or val == -1:
                        s += '1'
                elif i == 1:
                    s += 'x'
                else:
                    s = f"{s}x^{i}"
                r.append(s)
        r.reverse()
        s = "".join(r)
        if s == "":
            s = "0"
        elif s[0] == '+':
            s = s[1:]
        return s

    def print(self) -> None:
        print(self.get_str(), end='')

    def P(self, x: float) -> float:
        r = 0.0
        x_ = 1
        for i in self.a:
            r += i * x_
            x_ *= x
        r = round(r, 4)
        return int(r) if r.is_integer() else r
