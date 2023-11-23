# Принципы программирования
#
# YAGNI — You Ain’t Gonna Need It.
# KISS —  Keep It Simple, Stupid.
# DRY — Don’t Repeat Yourself.

# SOLID — Single responsibility principle                       Принцип единственной ответственности
# /Open/closed principle                                        Принцип открытости/закрытости
# /Liskov substitution principle                                Принцип подстановки Барбары Лисков
# /Interface segregation principle                              Принцип разделения интерфейса
# /Dependency inversion principle                               Принцип инверсии зависимостей

# Основу ООП составляют два понятия — классы и объекты

# объекты класса обладают свойствами и поведением (методами)

# МЕТОДЫ                                                         СВОЙСТВА
# существо.дышать()                                            существо.рост = 190
# существо.есть()                                              существо.имя = “Степан”
# существо.спать()                                             существо.должность = “Студент”
# существо.двигаться()                                         существо.возраст = 19
# существо.размножаться()

# ПРИНЦИПЫ ООП
# Наследование
# Новый класс описывается на основе уже существующего (родительского),
# то есть не только перенимает все свойства родительского класса, но ещё и получает новые.

# Абстракция
# Выделение главных, наиболее значимых характеристик предмета и отбрасывание второстепенных, незначительных.

# Инкапсуляция
# Позволяет объединить данные и методы, работающие с ними, в классе и скрыть детали реализации от пользователя.

# Полиморфизм
# Позволяет иметь множество реализаций одного интерфейса.

# КЛАССЫ
class PythonStudents:
    pass


first = PythonStudents()
first.name = "Kate"

second = PythonStudents()
second.name = "Stepan"

print(first.name)
print(second.name)


class Students:
    language = "Python"
    spec = "Auto"


Kate = Students()
print(Kate.language)


# Магический метод __init__
class StudentsQa:
    def __init__(self, name, group):
        self.name = name
        self.group = group


first = StudentsQa(name="Kate", group="Python")
second = StudentsQa(name="Stepan", group="Java")

print(first.name, ',', first.group)
print(second.group)


# Методы
class QaL:
    def __init__(self, course, language, number_of_students):
        self.course = course
        self.language = language
        self.number_of_students = number_of_students

    def is_available(self):
        return True if self.number_of_students < 10 else False


aqa_on_python = QaL("aqa", "python", 10)
print(aqa_on_python.is_available())


# Наследование

class QaL:
    course_quantity = 10

    def __init__(self, name, language, students_in_group):

        self.name = name
        self.language = language
        self.students_in_group = students_in_group

    def is_available(self):
        return True if self.students_in_group < 10 else False


class AQA(QaL):  # Дочерний класс
    pass


group1 = AQA(name="aqa_on_python", language="python", students_in_group=5)
print(group1.course_quantity)
print(group1.is_available())
print(group1.language)


class Table:
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h


class DeskTable(Table):
    def square(self):
        return self.width * self.length


t1 = Table(1.5, 2, 0.75)
t2 = DeskTable(1, 0.5, 0.75)
print(t2.square())
print(t1.square())


# Поное переопределение

class Table:
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h


class DeskTable(Table):
    def square(self):
        return self.width * self.length


class ComputerTable(DeskTable):
    def square(self, monitor=0.0):
        return self.width * self.length - monitor


t3 = ComputerTable(2, 1.5, 1.75)
print(t3.square(0.5))


# Полиморфизм
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b
