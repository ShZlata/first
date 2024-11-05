#A. Азбука

num = int(input())
letters = ["а", "б", "в"]
for _ in range(0, num):
    slovo = input()
    if slovo[0] not in letters:
        print("NO")
        break 
else:
    print("YES")

#B. Кручу-верчу

slovo = input()
for i in slovo:
    print(i)

#C. Анонс новости

dlina = int(input())
kolvo = int(input())
for _ in range(0, kolvo):
    ans = input()
    if len(ans) <= dlina:
        print(ans)
    else:
        print(ans[:dlina - 3] + "...")

#D. Очистка данных

while True:
    text = input()
    if text == '':
        break
    if text.endswith('@@@'):
        continue
    elif text.startswith('##'):
        print(text[2:])
    else:
        print(text)

#E. А роза упала на лапу Азора 4.0

text = input()
if text == text[::-1]:
    print('YES')
else:
    print('NO')

#F. Зайка — 6

n = int(input())
counter = 0
for _ in range(n):
    text = input()
    counter += text.count('зайка')
print(counter)

#G. А и Б сидели на трубе

n = input()
lst = n.split()
print(int(lst[0]) + int(lst[1]))

#H. Зайка — 7

n = int(input())
for _ in range(n):
    text = input()
    counter = text.find('зайка') + 1
    if counter:
        print(counter)
    else:
        print('Заек нет =(')

#I. Без комментариев

while text := input():
    if text.startswith('#'):
        continue
    if '#' in text:
        n = text.index('#')
        print(text[:n])
    else:
        print(text)

#J. Частотный анализ на минималках

text = ''
n = input()
while n != 'ФИНИШ':
    text += n.lower()
    n = input()
counter = 0
maximum = ''
for i in text:
    if i == ' ':
        continue
    c = text.count(i)
    if c > counter:
        counter = c
        maximum = i
    elif c == counter:
        if i < maximum:
            maximum = i
print(maximum)

#K. Найдётся всё

n = int(input())
text = []
for _ in range(n):
    text.append(input())
key = input()
for i in text:
    if key.lower() in i.lower():
        print(i)