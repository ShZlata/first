#A. Просто здравствуй, просто как дела

print('Как Вас зовут?')
name = input()
print(f'Здравствуйте, {name}!')
print('Как дела?')
vibe = input()
if (vibe == "хорошо"):
    print('Я за вас рада!')
elif (vibe == "плохо"):
    print('Всё наладится!')

#B. Кто быстрее?

petya = int(input())
vasya = int(input())
if (petya > vasya):
    print('Петя')
elif (petya < vasya):
    print('Вася')

#C. Кто быстрее на этот раз?

petya = int(input())
vasya = int(input())
tolya = int(input())
if petya < tolya and vasya < tolya:
    print("Толя")
if petya < vasya and tolya < vasya:
    print("Вася")
if tolya < petya and vasya < petya:
    print("Петя")

#D. Список победителей

petya = int(input())
vasya = int(input())
tolya = int(input())
if petya < vasya < tolya:
    print(f'1. Толя\n2. Вася\n3. Петя')
if petya < tolya < vasya:
    print(f'1. Вася\n2. Толя\n3. Петя')
if tolya < vasya < petya:
    print(f'1. Петя\n2. Вася\n3. Толя')
if tolya < petya < vasya:
    print(f'1. Вася\n2. Петя\n3. Толя')
if vasya < petya < tolya:
    print(f'1. Толя\n2. Петя\n3. Вася')
if vasya < tolya < petya:
    print(f'1. Петя\n2. Толя\n3. Вася')

#E. Яблоки

npetya = int(input())
mvasya = int(input())
petya = (6 + npetya)
vasya = (12 + mvasya)
if petya < vasya:
    print('Вася')
if vasya < petya:
    print('Петя')

#F. Сила прокрастинации

year = int(input())
if year % 4 or not year % 100 and year % 400:
    print('NO')
else:
    print('YES')

#G. А роза упала на лапу Азора

number = int(input())

if number // 1000 == number % 10 and number % 1000 // 100 == number % 100 // 10:
    print('YES')
else:
    print('NO')

#H. Зайка -- 1

text = input()
if "зайка" in text:
    print("YES")
else:
    print("NO")

#I. Первому игроку приготовиться

pl1 = input()
pl2 = input()
pl3 = input()
if pl1 < pl2 and pl1 < pl3:
    print(pl1)
elif pl2 < pl1 and pl2 < pl3:
    print(pl2)
elif pl3 < pl1 and pl3 < pl2:
    print(pl3)

#J. Лучшая защита -- шшифрование

num = int(input())
first = num // 10
last = num % 100
sum1 = first // 10 + first % 10
sum2 = last // 10 + last % 10
if sum1 < sum2:
    print(str(sum2) + str(sum1))
else:
    print(str(sum1) + str(sum2))

#K. Красота спасёт мир

num = int(input())
first = num // 100
second = num // 10 % 10
third = num % 10
middle = first + second + third - max(first, second, third) - min(first, second, third)
if max(first, second, third) + min(first, second, third) == middle * 2:
    print('YES')
else:
    print('NO')

#L. Музыкальный инструмент

first = int(input())
second = int(input())
third = int(input())
if first < (second + third) and second < (first + third) and third < (first + second):
    print('YES')
else:
    print('NO')

#M. Властелин Чисел: Братство общей цифры

elf = int(input())
gnom = int(input())
human = int(input())
ne1 = elf // 10
ne2 = elf % 10
ng1 = gnom // 10
ng2 = gnom % 10
nh1 = human // 10
nh2 = human % 10
if ne1 == ng1 == nh1:
    print(f'{ne1}')
elif ne2 == ng2 == nh2:
    print(f'{ne2}')

#N. Властелин Чисел: Две Башни

number = int(input())
n1 = number // 100
n2 = number // 10 % 10
n3 = number % 10
medium = (n1 + n2 + n3 - min(n1, n2, n3) - max(n1, n2, n3))
if min(n1, n2, n3) != 0:
    minimal = min(n1, n2, n3) * 10 + medium
elif medium != 0:
    minimal = medium * 10
else:
    minimal = max(n1, n2, n3) * 10
maximal = max(n1, n2, n3) * 10 + medium
print(minimal, maximal)

#O. Властелин Чисел: Возвращение Цезаря

n1 = int(input())
n2 = int(input())
a = n1 // 10
b = n1 % 10
c = n2 // 10
d = n2 % 10
summa = a + b + c + d
minimal = min(a, b, c, d)
maximal = max(a, b, c, d)
medium = (summa - minimal - maximal) % 10
print(maximal * 100 + medium * 10 + minimal)

#P. Легенды велогонок возвращаются: кто быстрее?

petya = int(input())
vasya = int(input())
tolya = int(input())
first = max(petya, vasya, tolya)
third = min(petya, vasya, tolya)
second = petya + vasya + tolya - first - third
if first == petya:
    first_name = 'Петя'
elif first == vasya:
    first_name = 'Вася'
else:
    first_name = 'Толя'
if second == petya:
    second_name = 'Петя'
elif second == vasya:
    second_name = 'Вася'
else:
    second_name = 'Толя'
if third == petya:
    third_name = 'Петя'
elif third == vasya:
    third_name = 'Вася'
else:
    third_name = 'Толя'
print(f'{first_name: ^24}')
print(f'{second_name: ^8}{" ": ^16}')
print(f'{" ": ^16}{third_name: ^8}')
print(f'{"II": ^8}{"I": ^8}{"III": ^8}')