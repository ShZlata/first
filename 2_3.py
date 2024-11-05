#A. Раз, два, три! Ёлочка, гори!

eve = 'Три!'
while input() != eve:
    print('Режим ожидания...')
print('Ёлочка, гори!')

#B. Зайка — 3

counter = 0
while True:
    inp = input()
    if inp == "Приехали!":
        break
    if "зайка" in inp:
        counter += 1
print(counter)

#C. Считалочка

n = int(input())
k = int(input())
a = ''
for i in range(n, k + 1, 1):
    print(i, end=' ')

#D. Считалочка 2.0

nachalo = int(input())
konets = int(input())

if nachalo >= konets:
    for i in range(nachalo, konets - 1, -1):
        print(i, end=' ')
else:
    for i in range(nachalo, konets + 1, 1):
        print(i, end=' ')

#E. Внимание! Акция!

summa = 0
while (n := float(input())) != 0:
    if n >= 500:
        summa += n * 0.9
    else:
        summa += n
print(summa)

#F. НОД

a = int(input())
b = int(input())
while a != 0 and b != 0:
    if a >= b:
        a -= b
    else:
        b -= a
print(a + b)

#G. НОК

a = a1 = int(input())
b = b1 = int(input())
while a != 0:
    a, b = b % a, a
print(a1 * b1 // (a + b))

#H. Излишняя автоматизация 2.0

a = input()
N = int(input())
for _ in range(N):
    print(a)

#I. Факториал

a = int(input())
fact = 1
if a == 0:
    print(1)
else:
    for i in range(1, a + 1):
        fact *= i
print(fact)

#J. Маршрут построен

x = 0
y = 0
while (napr := input()) != "СТОП":
    n = int(input())
    if napr == "СЕВЕР":
        y += n
    elif napr == "ЮГ":
        y -= n
    elif napr == "ЗАПАД":
        x -= n
    elif napr == "ВОСТОК":
        x += n
print(y)
print(x)

#K. Цифровая сумма

a = int(input())
b = 0

while a > 0:
    b += a % 10
    a = a // 10
print(b)

