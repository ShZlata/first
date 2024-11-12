#A. A+B+...

from sys import stdin
summa = 0
for i in stdin.read().split():
    summa += int(i)
print(summa)

#B. Средний рост

from sys import stdin
lines = stdin.read().split('\n')
med = 0
kid = 0
for line in lines:
    if line:
        name, h1, h2 = line.split()
        med += int(h2) - int(h1)
        kid += 1
print(round(med / kid))

#C. Без комментариев 2.0

from sys import stdin
for i in stdin:
    if i[0] != '#':
        print(i.split('#')[0].rstrip('\n'))

#D. Найдётся всё 2.0

from sys import stdin
full = stdin.readlines()
key = full[-1].strip('\n').lower()
ost = full[:-1]
for i in ost:
    if i.lower().find(key) + 1:
        print(i.strip('\n'))

#E. А роза упала на лапу Азора 6.0

from sys import stdin
slova = []
full = stdin.readlines()
for line in full:
    for word in line.rstrip('\n').split():
        if word.lower() == word.lower()[::-1]:
            slova.append(word)
print('\n'.join(sorted(set(slova))))

#F. Транслитерация 2.0

translit = {'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 
            'Е': 'E', 'Ё': 'E', 'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 
            'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 
            'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'KH', 
            'Ц': 'TC', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH', 'Ы': 'Y', 
            'Э': 'E', 'Ю': 'IU', 'Я': 'IA', 'Ь': '', 'Ъ': ''}
inn, oout = '', ''
with open("cyrillic.txt", encoding="UTF-8") as file_in:
    for line in file_in:
        inn += line
for i in inn:
    if i.upper() in translit:
        oout += translit[i.upper()].lower().capitalize() if i == i.upper() else translit[i.upper()].lower()
    else:
        oout += i
with open("transliteration.txt", "w", encoding="UFT-8") as file_out:
    print(oout, file=file_out)

#G. Файловая статистика

with open(input(), encoding='UTF-8') as file_in:
    numbers = [int(number) for number in file_in.read().split()]
print(leng := len(numbers))
print(len([number for number in numbers if number > 0]))
print(min(numbers))
print(max(numbers))
print(full := sum(numbers))
print(f'{(full / leng):.2f}')

#H. Файловая разница

fst = input()
snd = input()
asw = input()
with open(fst, encoding='UTF-8') as file_in:
    lst1 = set([i for i in file_in.read().split()])
with open(snd, encoding='UTF-8') as file_in:
    lst2 = set([j for j in file_in.read().split()])
new = lst1 ^ lst2
with open(asw, 'w', encoding='UTF-8') as file_out:
    print('\n'.join(sorted(new)), file=file_out)

#I. Файловая чистка

fst = input()
snd = input()
with open(fst, encoding='UTF-8') as file_in:
    txt = file_in.read()
while txt.find('\t') + 1:
    txt = txt.replace('\t', '')
while txt.find('  ') + 1:
    txt = txt.replace('  ', ' ')
txt = '\n'.join(line.strip() for line in txt.split('\n') if line)
with open(snd, 'w', encoding='UTF-8') as file_out:
    file_out.write(txt)

#J. Хвост

filE = input()
enD = int(input())
n = []
with open(filE) as file:
    for line in file:
        n.append(line)
for line in n[-enD:]:
    print(line.strip())
    