print('Вас приветствует программа, которая выводит количество одинаковых чисел среди 3-х введённых!')
first = int(input('Введи первое целое число: '))
second = int(input('Введи второе целое число: '))
third = int(input('Введи третье целое число: '))
if first == second == third:
    print('Одинаковых чисел:', 3)
elif first == second or first == third or second == third:
    print('Одинаковых чисел:', 2)
else:
    print('Одинаковых чисел:', 0)
