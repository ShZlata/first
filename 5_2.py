#A. Классная точка 3.0

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, nx, ny):
        self.x += nx
        self.y += ny

    def length(self, point):
        last = ((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** 0.5
        return round(last, 2)


class PatchedPoint(Point):

    def __init__(self, *args):
        match len(args):
            case 0:
                self.x, self.y = 0, 0
            case 1:
                self.x, self.y = args[0]
            case 2:
                self.x, self.y = args

#B. Классная точка 4.0

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, nx, ny):
        self.x += nx
        self.y += ny

    def length(self, point):
        last = ((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** 0.5
        return round(last, 2)


class PatchedPoint(Point):

    def __init__(self, *args):
        match len(args):
            case 0:
                self.x, self.y = 0, 0
            case 1:
                self.x, self.y = args[0]
            case 2:
                self.x, self.y = args

    def __str__(self):
        line = f'({self.x}, {self.y})'
        return line

    def __repr__(self):
        line = f'PatchedPoint({self.x}, {self.y})'
        return line

#C. Классная точка 5.0

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, nx, ny):
        self.x += nx
        self.y += ny

    def length(self, point):
        last = ((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** 0.5
        return round(last, 2)


class PatchedPoint(Point):

    def __init__(self, *args):
        match len(args):
            case 0:
                self.x, self.y = 0, 0
            case 1:
                self.x, self.y = args[0]
            case 2:
                self.x, self.y = args

    def __str__(self):
        line = f'({self.x}, {self.y})'
        return line

    def __repr__(self):
        line = f'PatchedPoint({self.x}, {self.y})'
        return line

    def __add__(self, other):
        return PatchedPoint(self.x + other[0], self.y + other[1])

    def __iadd__(self, other):
        self.move(other[0], other[1])
        return self

#D. Дроби v0.1

class Fraction():
    def __init__(self, *args):
        if isinstance(args[0], str):
            self.__fst, self.__snd = [int(c) for c in args[0].split('/')]
        else:
            self.__fst = args[0]
            self.__snd = args[1]
        self.__reduction()

    def __gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return abs(a)

    def __reduction(self):
        gcd = self.__gcd(self.__fst, self.__snd)
        self.__fst = self.__fst // gcd
        self.__snd = self.__snd // gcd
        return self

    def __str__(self):
        return f'{self.__fst}/{self.__snd}'

    def __repr__(self):
        return f'Fraction({self.__fst}, {self.__snd})'

    def numerator(self, *args):
        if len(args):
            self.__fst = args[0]
            self.__reduction()
        return self.__fst

    def denominator(self, *args):
        if len(args):
            self.__snd = args[0]
            self.__reduction()
        return self.__snd

#E. Дроби v0.2

class Fraction():
    def __init__(self, *args):
        if isinstance(args[0], str):
            self.__fst, self.__snd = [int(c) for c in args[0].split('/')]
        else:
            self.__fst = args[0]
            self.__snd = args[1]
        self.__reduction()

    def __gcd(self, a, b):
        while b:
            a, b = b, a % b
        return abs(a)

    def __reduction(self):
        gcd = self.__gcd(self.__fst, self.__snd)
        self.__fst = self.__fst // gcd
        self.__snd = self.__snd // gcd
        if self.__snd < 0:
            self.__fst = -self.__fst
            self.__snd = abs(self.__snd)
        return self

    def __str__(self):
        return f'{self.__fst}/{self.__snd}'

    def __repr__(self):
        return f"Fraction('{self.__fst}/{self.__snd}')"

    def numerator(self, *args):
        if len(args):
            self.__fst = args[0] * self.__sigh()
        self.__reduction()
        return abs(self.__fst)

    def denominator(self, *args):
        if len(args):
            self.__snd = args[0]
        self.__reduction()
        return abs(self.__snd)

    def __sigh(self):
        if self.__fst < 0:
            return -1
        else:
            return 1

    def __neg__(self):
        return Fraction(-self.__fst, self.__snd)
    