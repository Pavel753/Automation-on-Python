# Функции
# def name_func():
def hello_world():
    print("Hello World")


hello_world()


def add_2_and_2():
    result = 2 + 2
    print(result)


add_2_and_2()


def add_2(number):
    print(number ** 2)


add_2(3)  # 10
add_2(5)


# функция, которая прибавляет к любому числу число n

def add_number(number, n=2):
    print(number + n)


add_number(5)
add_number(5, 8)


# Local. Global
def sum1():
    a = 1  # локальные переменные
    b = 2
    c = a + b
    print("Сумма:", c)


sum1()


def local():
    a = 1  # local
    print(a)


a = 2
local()
print(a)

# Что выведет программа в результате выполнения функции?
a = 1


def func():
    print(a)
    a = 2
    a += 3


print(func())

# Global
a = 1  # определены вне функции
b = 2


def sum2():
    c = a + b  # Используем глобальные переменные
    print("Сумма:", c)


def sub():
    d = a - b  # Используем глобальные переменные
    print("Разница:", d)


sum2()
sub()


# Local vs Global
def hello():
    a = "Привет!"
    print(a)


hello()
a = "Отлично!"  # глобальная переменная
print(a)

# Keyword Global
a = 1


def func():
    a = a + 2
    print(a)


func()

# Меняем значение global
а = 1


def func():
    global a
    a = a + 2
    print(a)


func()


# *args **kwargs
def func(a, b, c):
    print('a =', a)
    print('b =', b)
    print('c =', c)


func(1, 2, 3)
func(3, 2, 1)

# Обратимся по имени
func(a=1, b=2, c=3)
func(c=3, b=2, a=1)

# *
a = [1, 2, 3]
b = [a, 4, 5, 6]
print(b)

a = [1, 2, 3]
b = [*a, 4, 5, 6]
print(b)

print(a)
print(*a)


#
def func(*args, **kwargs):
    print(type(args))
    print(type(kwargs))


func()


# *args
def func(*nums):
    sum1 = 0
    for n in nums:
        sum1 += n

    return sum1


print(func())
print(func(1))
print(func(1, 2))
print(func(1, 2, 3))


# Два примера
def func(*args):
    for arg in args:
        print(arg)


func('Hello', 'My ', 'name is', 'Kate')


def func(arg1, *args):
    print("Первый аргумент:", arg1)
    for arg in args:
        print("Следующий аргумент *args :", arg)


func('Hello', 'My ', 'name is', 'Kate')


# **kwargs
def intro(**kwargs):
    for key, value in kwargs.items():
        print("{} is {}".format(key, value))


intro(Firstname="Kate", Language="Python", Age=25)


# Итераторы и генераторы, оператор yield
# 1
def add_number(number, n=2):
    print(number + n)


print(add_number(2))


# 2
def add_number(number, n=2):
    print(number + n)
    return None


print(add_number(2))


# 3
def add_number(number, n=2):
    result = number + n
    return result


print(add_number(2))


# Простой генератор
def first_generator():
    yield 2
    yield 4
    yield 8


# Код для проверки first_generator()
for value in first_generator():
    print(value)


# Генератор
def num_degree():
    n = 2
    while True:  # Бесконечный цикл для генерации степеней 2
        yield n
        n *= 2  # При последующем обращении к  num_degree() выполнение кода продолжится с этого места


for num in num_degree():  # Код для проверки num_degree()
    if num > 256:
        break  # Прервись здесь
    print(num)

# Итератор
pets = ("dog", "cat", "finch")
iterate = iter(pets)
print(next(iterate))
print(next(iterate))
print(next(iterate))

# Строка-итератор
iter_str = "Kate"
iterate = iter(iter_str)
print(next(iterate))
print(next(iterate))
print(next(iterate))
print(next(iterate))

# Цикл с итератором
pets = ("dog", "cat", "finch")
for x in pets:
    print(x)

# *
iter_str = "Kate"
for x in iter_str:
    print(x)


# Декоратор
def decorator(func):
    def wrapper():
        print('Это просто оболочка')
        func()

    return wrapper


def basic():
    print('Наша основная функция')


wrapped = decorator(basic)
print('Начало программы')
basic()
wrapped()
print('Конец программы')


# @
def decorator(func):
    '''Основная функция'''
    print('Декоратор')

    def wrapper():
        print('Исполнить до функции', func.__name__)
        func()
        print('Исполнить после функции', func.__name__)

    return wrapper


@decorator
def wrapped():
    print('Наша обернутая функция')


print('Здесь старт программы...')
wrapped()
print('Здесь конец программы')

# Функция map
L = ['DOG', 'CAT', 'FINCH']
print(list(map(str.lower, L)))

# Lambda функции
list(map(lambda x: x ** 2, range(1, 6)))

# Задача 1
# Написать функцию, которая будет перемножать любое количество переданных ей аргументов.

# Задача 2
# Выведите длину каждого элемента в списке.
# a = ["123", "1234", "4567", "987654"]

# Задача 3
# Отфильтруйте из заданного списка только четные элементы.
[-2, -3, 0, 1, -1, 2, 4]
