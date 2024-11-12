#A. Классная точка

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

#B. Классная точка 2.0

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

#C. Не нажимай красную кнопку!

class RedButton:
    def __init__(self):
        self.counter = 0

    def click(self):
        self.counter += 1
        print('Тревога!')

    def count(self):
        return self.counter

#D. Работа не волк

class Programmer:

    def __init__(self, name, position):
        self.name = name
        lstP = {'Junior': 10, 'Middle': 15, 'Senior': 20}
        self.time = 0
        self.moneyH = lstP[position]
        self.money = 0

    def work(self, time):
        self.time += time
        self.money += self.moneyH * time

    def rise(self):
        if self.moneyH < 20:
            self.moneyH += 5
        else:
            self.moneyH += 1

    def info(self):
        return f'{self.name} {self.time}ч. {self.money}тгр.'

#E. Классный прямоугольник

class Rectangle:

    def __init__(self, *xy):
        self.xy = xy
        self.vis = abs(self.xy[0][1] - self.xy[1][1])
        self.shir = abs(self.xy[0][0] - self.xy[1][0])

    def perimeter(self):
        return round(2 * (self.vis + self.shir), 2)

    def area(self):
        return round(self.vis * self.shir, 2)
