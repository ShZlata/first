#A. Привет, Яндекс!

print("Привет, Яндекс!")

#B. Привет всем!

print("Как Вас зовут?")
username = input()
print(f"Привет, {username}")

#C. Излишняя автоматизация

a = input()
print(f'{a} \n' * 3)

#D. Сдача

kg = 2.5
rub = 38
summ = int(kg * rub)
cash = int(input())
print(cash - summ)

#E. Магазин

c = int(input())
w = int(input())
rub = int(input())
print(rub - c * w)

#F. Чек

name = input()
c = int(input())
w = int(input())
rub = int(input())
print("Чек")
print(f'{name} - {w}кг - {c}руб/кг')
print(f'Итого: {w * c}руб')
print(f'Внесено: {rub}руб')
print(f'Сдача: {rub - w * c}руб')

#G. Делу — время, потехе — час

a = int(input())
print(f"Купи слона! \n" * a)

#H. Наказание

a = int(input())
b = input()
print(f'Я больше никогда не буду писать "{b}"! \n' * a)

#I. Деловая колбаса

N = int(input())
M = int(input())
print(int(M * N / 2))

#J. Детский сад — штаны на лямках

name = input()
number = input()
print(f'Группа №{number[0]}.')
print(f'{number[2]}. {name}.')
print(f'Шкафчик: {number}.')
print(f'Кроватка: {number[1]}.')

#K. Автоматизация игры

a = input()
print(f'{a[1]}{a[0]}{a[3]}{a[2]}')

#L. Интересное сложение

n = int(input())
m = int(input())
a = n % 10
b = m % 10
c = n // 10 % 10
d = m // 10 % 10
e = n // 100 % 10
f = m // 100 % 10
g = (a + b) % 10
h = (c + d) % 10
i = (e + f) % 10
print(f'{i}{h}{g}')

#M. Дед Мороз и конфеты

kids = int(input())
candy = int(input())
print(candy // kids)
print(candy % kids)

#N. Шарики и ручки

red = int(input())
green = int(input())
blue = int(input())
print(red + blue + 1)

#O. В ожидании доставки

N = int(input())
M = int(input())
T = int(input())
newM = str((M + T) % 60)
newN = str((N + (M + T) // 60) % 24)
print(f'{newN:0>2}:{newM:0>2}')

#P. Доставка

a = int(input())
b = int(input())
c = int(input())
print(f'{(b - a) / c:.2f}')

#Q. Ошибка кассового аппарата

nat = int(input())
bi = input()
print(int(nat + int(bi, 2)))

#R. Сдача 10

bi = int(input(), 2)
rub = int(input())
print(int(rub - bi))

#S. Украшение чека

good = input()
price = int(input())
weight = int(input())
cash = int(input())

price_string = str(weight) + 'кг * ' + str(price) + 'руб/кг'
sum_string = str(price * weight) + 'руб'
cash_string = str(cash) + 'руб'
change_string = str(cash - price * weight) + 'руб'

print('================Чек================')
print(f'Товар: {good:>28}')
print(f'Цена: {price_string:>29}')
print(f'Итого: {sum_string:>28}')
print(f'Внесено: {cash_string:>26}')
print(f'Сдача: {change_string:>28}')
print('===================================')

#T. Мухи отдельн, котлеты отдельно

n = int(input())
m = int(input())
k1 = int(input())
k2 = int(input())
x = int((m - k2) * n / (k1 - k2))
y = n - x
print(x, y)