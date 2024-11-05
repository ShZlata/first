#A. Таблица умножения

n = int(input())
for i in range(n):
    for j in range(n):
        print((i + 1) * (j + 1), end=' ')
    print()

#B. Не таблица умножения

n = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f'{j} * {i} = {i * j}')

#C. Новогоднее настроение

size = int(input())
print(1)
last_len = 1
current_len = 0
for num in range(2, size + 1):
    if current_len > last_len:
        last_len = current_len
        current_len = 0
        print('')
    print(num, end=' ')
    current_len += 1

#D. Суммарная сумма

n = int(input())
summ = 0
for _ in range(n):
    num = int(input())
    while num > 0:
        summ += num % 10
        num //= 10
print(summ)

#E. Зайка — 5

n = int(input())
counter = 0
for _ in range(n):
    counted = False
    while (text := input()) != 'ВСЁ':
        if text == 'зайка' and counted is False:
            counter = counter + 1
            counted = True
print(counter)

#F. НОД 2.0

n = int(input())
a = int(input())
for _ in range(0, n - 1):
    b = int(input())
    while a != 0:
        if a < b:
            a, b = b, a
        a = a % b
    a = b
print(a)

#G. На старт! Внимание! Марш!

n = int(input())
for i in range(n):
    for j in range(3 + i, 0, -1):
        print(f'До старта {j} секунд(ы)')
    print(f'Старт {i + 1}!!!')

#H. Максимальная сумма

n = int(input())
wname = ''
maxsumm = 0
for i in range(n):
    name = input()
    num = int(input())
    summ = 0
    while num > 0:
        summ += num % 10
        num //= 10
    if summ >= maxsumm:
        maxsumm = summ
        wname = name
print(wname)

#I. Большое число

n = int(input())
end = 0
for _ in range(n):
    num = int(input())
    maximum = -1
    while num > 0:
        if num % 10 > maximum:
            maximum = num % 10
        num //= 10 
    end = end * 10 + maximum
print(end)

#J. Мы делили апельсин

slices = int(input())
print('А Б В')
for a in range(1, slices - 1):
    for b in range(1, slices - a):
        v = slices - a - b
        print(a, b, v)

#K. Простая задача 3.0

n = int(input())
counter = 0
for _ in range(n):
    a = int(input())
    if a == 1:
        continue
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            break
    else:
        counter += 1
print(counter)