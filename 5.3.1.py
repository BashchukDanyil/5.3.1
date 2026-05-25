class Rational:
    def __init__(self, a, b = 1):
        if isinstance(a, Rational):
            self.a = a.a
            self.b = a.b
            self.r = a.r
        elif isinstance(a, str):
            c = ""
            s = a[0]
            i = 1
            while s != '/':
                c += s
                s = a[i]
                i += 1
            b = ""
            s = ''
            while i < len(a):
                s = a[i]
                b += s
                i += 1
            c = int(c)
            b = int(b)
            if b == 0:
                raise ZeroDivisionError
            self.a = abs(c)
            self.b = abs(b)
            d = self._nsd(self.a, self.b)
            if c * b  >= 0:
                self.a //= d
            else:
                self.a //= -d
            self.b //= d
            self.r = f'{self.a} / {self.b}'
        else:
            if b == 0:
                raise ZeroDivisionError
            self.a = abs(a)
            self.b = abs(b)
            d = self._nsd(self.a, self.b)
            if a * b  >= 0:
                self.a //= d
            else:
                self.a //= -d
            self.b //= d
            self.r = f'{self.a} / {self.b}'
    def _nsd(self, a, b):
        while b != 0:
            r = a % b
            a = b
            b = r
        return a
    def __add__(self, other):
        if isinstance(other, Rational):
            return Rational(self.a * other.b + other.a * self.b, self.b * other.b)
        elif isinstance(other, int):
            other = Rational(other, 1)
            return Rational(self.a * other.b + other.a * self.b, self.b * other.b)
        else:
            raise TypeError
    def __sub__(self, other):
        if isinstance(other, Rational):
            return Rational(self.a * other.b - other.a * self.b, self.b * other.b)
        elif isinstance(other, int):
            other = Rational(other, 1)
            return Rational(self.a * other.b - other.a * self.b, self.b * other.b)
        else:
            raise TypeError
    def __mul__(self, other):
        if isinstance(other, Rational):
            return Rational(self.a * other.a, self.b * other.b)
        elif isinstance(other, int):
            return Rational(self.a * other, self.b)
        else:
            raise TypeError
    def __truediv__(self, other):
        if isinstance(other, Rational):
            return Rational(self.a * other.b, self.b * other.a)
        elif isinstance(other, int):
            return Rational(self.a, self.b * other)
        else:
            raise TypeError
    def __call__(self):
        return self.a / self.b
    def __setitem__(self, key, value):
        if key == "n":
            self.a = value
        if key == "d":
            self.b = value
        raise KeyError
    def __getitem__(self, key):
        if key == "n":
            return self.a
        if key == "d":
            return self.b
        raise KeyError





if __name__ == '__main__':
    file = open("input.txt", "r")

    for line in file:
        l = line.split()
        i = 0
        while i != len(l):
            try:
                l[i] = int(l[i])
                i += 1
            except ValueError:
                i += 1
        sum = Rational(l[0])
        for j in range(1, len(l) - 2, 2):
            if l[j] == "+":
                r = Rational(l[j + 1])
                sum += r
            if l[j] == "-":
                r = Rational(l[j + 1])
                sum -= r
            if l[j] == "*":
                r = Rational(l[j + 1])
                sum *= r
            if l[j] == "/":
                r = Rational(l[j + 1])
                sum /= r
        print(sum())


    file.close()

    # r1 = Rational("90/16")
    # r2 = Rational(r1)
    # r3 = Rational(2)
    # print(r3.r)
    # r = r1 + 8
    # print(r1.r)
    # print(r1.r)
    # print(r2.r)
    # print(r.r)
