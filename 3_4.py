#A. Автоматизация списка

for index, word in enumerate(input().split(), start=1):
    print(f'{index}. {word}')

#B. Сборы на прогулку

fst = input().split(', ')
snd = input().split(', ')
for i in zip(fst, snd):
    print(f'{i[0]} - {i[1]}')

#C. Рациональная считалочка

from itertools import count
start, stop, step = [float(x) for x in input().split()]
for i in count(start, step):
    if i >= stop:
        break
    print(f'{i:.2f}')

#D. Словарная ёлка

from itertools import accumulate
for i in accumulate([slovo + ' ' for slovo in input().split()]):
    print(i)

#E. Список покупок

from itertools import chain
text = [input().split(', ') for _ in range(3)]
alll = sorted(set(chain.from_iterable(text)))
for index, word in enumerate(alll, 1):
    print(f'{index}. {word}')

#F. Колода карт

from itertools import product
num = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз']
mast = ['пик', 'треф', 'бубен', 'червей']
mast.remove(input())
for n, m in product(num, mast):
    print(n, m)

#G. Игровая сетка

from itertools import combinations
names = [input() for _ in range(int(input()))]
print('\n'.join([f'{name1} - {name2}' for name1, name2 in combinations(names, 2)]))

#H. Меню питания 2.0

from itertools import islice, cycle
kasha = [input() for _ in range(int(input()))]
kdays = int(input())
menu = islice(cycle(kasha), kdays)
print('\n'.join(menu))

#I. Таблица умножения 3.0

import itertools
n = int(input())
num = range(1, n + 1)
tab = [x * y for x, y in itertools.product(num, repeat=2)]
for i in range(n):
    print(*itertools.islice(tab, i * n, (i + 1) * n))

#J. Мы делили апельсин 2.0

from itertools import combinations
dol = int(input())
num = range(1, dol)
print('А Б В')
for fst, snd in list(combinations(num, 2)):
    print(f'{fst} {snd - fst} {dol - snd}')
