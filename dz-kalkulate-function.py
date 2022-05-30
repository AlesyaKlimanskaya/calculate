# простейший "Калькулятор" с применением функции
# Вариант №1
# def s_f(a, b):
#     return a + b
# def d_f(a, b):
#     return a - b
# def p_f(a, b):
#     return a * b
# def c_f(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return 'Деление на 0. Ошибка!!!'
# def e_f(a, b):
#     return a ** b
# while True:
#     c = input('Введите операцию(+,-,*,/,**,0): ')
#     if c not in '+,-,*,/,**,0':
#         print('Не верно введена операция!!!')
#         continue
#     elif c == '0':
#         print('Программа завершена')
#         break
#     try:
#         a = float(input('Введите первое число: '))
#     except ValueError:
#         print('Вы ввели не число!')
#         continue
#     try:
#         b = float(input('Введите второе число: '))
#     except ValueError:
#         print('Вы ввели не число!')
#         continue
#     if c == '+':
#         print(s_f(a, b))
#     elif c == '-':
#         print(d_f(a, b))
#     elif c == '*':
#         print(p_f(a, b))
#     elif c == '/':
#         print(c_f(a, b))
#     elif c == '**':
#         print(e_f(a, b))

# Вариант №2
def calculate_f(a, b, c):
    if c == '+':
        return a + b
    if c == '-':
        return a - b
    if c == '*':
        return a * b
    if c == '/':
        try:
            return a / b
        except ZeroDivisionError:
            return 'Деление на 0. Ошибка!!!'
    if c == '**':
        return a ** b
while True:
    c = input('Введите операцию(+,-,*,/,**,0): ')
    if c not in '+,-,*,/,**,0':
        print('Не верно введена операция!!!')
        continue
    elif c == '0':
        print('Программа завершена')
        break
    try:
        a = float(input('Введите первое число: '))
    except ValueError:
        print('Вы ввели не число!')
        continue
    try:
        b = float(input('Введите второе число: '))
    except ValueError:
        print('Вы ввели не число!')
        continue
    print(calculate_f(a, b, c))






