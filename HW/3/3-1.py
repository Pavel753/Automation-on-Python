# 1. Напишите программу, которая запрашивает два числа. Выведите их среднее геометрическое, или сообщение об ошибке,
# если это сделать невозможно
from math import *

try:
    num1, num2 = (
        float(input('Введите первое число: ')),
        float(input('Введите второе число: ')))  # Получаем 2 числа
    try:
        sr_ge = sqrt(num1 * num2)  # Выводим их среднее геометрическое
        print(sr_ge)
    except ValueError:
        print('У этих чисел не может быть среднего геометрического')
except ValueError:
    print('Вы ввели не число, попробуйте еще раз')
