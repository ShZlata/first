#A. Список квадратов

[num ** 2 for num in range(a, b + 1)]

#B. Таблица умножения 2.0

[[(i + 1) * (j + 1) for j in range(n)] for i in range(n)]

#C. Длины всех слов

[len(slovo) for slovo in sentence.split()]

#D. Множество нечетных чисел

{num for num in numbers if num % 2 == 1}

#E. Множество всех полных квадратов

{num for num in numbers if (int(num ** 0.5)) ** 2 == num}
