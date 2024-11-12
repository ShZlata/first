#A. Рекурсивный сумматор

def recursive_sum(*n):
    while n[1:]:
        return n[0] + recursive_sum(*n[1:])
    return n[0]

#B. Рекурсивный сумматор цифр

def recursive_digit_sum(n):
    while n >= 10:
        return n % 10 + recursive_digit_sum(n // 10)
    return n

#C. Многочлен N-ой степени

def make_equation(*n):
    if len(n) == 1:
        return f'{n[0]}'
    else:
        return f'({make_equation(*n[:-1])}) * x + {n[-1]}'

#D. Декор результата

def answer(f):
    def code(*args, **kwargs):
        return f'Результат функции: {f(*args, ** kwargs)}'
    return code

#E. Накопление результата

def result_accumulator(f):
    lst = []
    
    def func(*args, method='accumulate', **kwargs):
        if method == 'accumulate':
            lst.append(f(*args, **kwargs))
        elif method == 'drop':
            lst.append(f(*args, **kwargs))
            result = lst[:]
            lst.clear()
            return result
    return func
