# Написать функцию, которая будет перемножать любое количество переданных ей аргументов.

def pr_num(*args):
    pr = 1  # Устанавливам начальное значение счетчика
    for num in args:  # Перемножаем переданные аргументы
        pr *= num
    return pr


print(pr_num(2, 4, 6))  # Пример выполнения
