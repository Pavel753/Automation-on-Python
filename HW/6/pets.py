class Pet:
    def __init__(self, n, a):
        self.name = n
        self.age = a


class Cat(Pet):
    def voise(self):
        voise = 'мяу'
        return voise


class Dog(Pet):
    def voise(self):
        voise = 'гав'
        return voise
