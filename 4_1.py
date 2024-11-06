#A. Функциональное приветствие

def print_hello(name):
    print(f'Hello, {name}!')

#B. Функциональный НОД

def gcd(n, m):
    while m != 0:
        n, m = m, n % m
    return n

#C. Длина числа

def number_length(number):
    return len(str(abs(number)))
    
#D. Имя of the month

def month(n, lng):
    months = {'en': ['January', 'February', 'March', 'April', 'May', 'June',
                     'July', 'August', 'September', 'October', 'November', 'December'], 
              'ru': ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
                     'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']}
    return months[lng][n - 1]

#E. Числовая строка

def split_numbers(stroka):
    return tuple([int(number) for number in stroka.split()])
