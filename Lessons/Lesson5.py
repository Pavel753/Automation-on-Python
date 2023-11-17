
# myFile = open(filename.txt)
# myFile = open(filename.txt, 'r')
# myFile = open(filename.txt, 'r’, encoding=”utf8”)

# Режим                                                               Обозначение
#
# 'r'                                      Открытие на чтение
#
# 'w'                                     Открытие на запись. Если файл уже существует, то содержимое файла удаляется.
#
#                                         Если файла не существует — создаётся новый.
#
# 'x'                                   Открытие на запись. Если файла не существует — всё работает, иначе — исключение.
#
# 'a'                                    Открытие на дозапись, информация добавляется в конец файла.
#
# 'b'                                    Открытие в двоичном режиме.
#
# 't'                                    Открытие в текстовом режиме.
#
# '+'                                     Открытие на чтение и дозапись, информация добавляется в конец файла.

# Метод read() — сохраняет всё содержимое файла как строку.
#
# Если в метод read() передать число, то вернётся указанное число символов.

myFile = open('NewFile.txt', encoding="utf8")
print(myFile.read())

myFile = open('NewFile.txt', encoding="utf8")
print(myFile.read(4))

myFile = open('NewFile.txt', encoding="utf8")
print(myFile.readline())

myFile = open('NewFile.txt', encoding="utf8")
print(myFile.readlines())

myFile = open('NewFile.txt', encoding="utf8")
for line in myFile:
    print(line)

# Запись в файл
w_file = "Python"
myFile = open('First_File.txt', 'w')
for index in w_file:
    myFile.write(index + '\n')
myFile.close()  # Закрываем файл!

myFile = open('First_File.txt', encoding="utf8")
for line in myFile:
    print(line)

# With
with open('NewFile.txt', encoding="utf8") as MyFile:
    for line in MyFile:
        print(line)

# Задача
alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphaUp = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
number = int(input('Введите число, на которое нужно сдвинуть текст: '))

summary = ''


def changeChar(char):
    if char in alpha:
        return alpha[(alpha.index(char) + number) % len(alpha)]
    elif char in alphaUp:
        return alphaUp[(alphaUp.index(char) + number) % len(alphaUp)]
    else:
        return char


with open("NewFile.txt", encoding="utf8") as myFile:
    for line in myFile:
        for char in line:
            summary += changeChar(char)

with open("First_File.txt", 'w', encoding="utf8") as myFile:
    myFile.write(summary)

with open('First_File.txt', encoding="utf8") as MyFile:
    for line in MyFile:
        print(line)

# Абсолютный путь к файлу
# C:\Users\a.zavaruyeva\Desktop\NewFile.txt
myFile = open('C:\Users\a.zavaruyeva\Desktop\NewFile.txt', 'r', encoding="utf8")

print("AQA\test")  # AQA	est

# r от слова raw, т.е r – это сырые # строки (необработанные строки)
myFile = open(r'C:\Users\a.zavaruyeva\Desktop\NewFile.txt', 'r', encoding="utf8")
for line in myFile:
    print(line)

# Относительный путь
myFile = open('NewFile.txt', encoding="utf8")
print(myFile.read())

# Работа с JSON файлами
# {
#     "firstname": "Катя",
#     "lastname": "Артемьева",
#     "isAlive": true,
#     "age": 25,
#     "address": {
#         "streetAddress": "Независимости, 62",
#         "city": "Минск",
#
#     },
#     "phoneNumbers": [
#         {
#             "type": "mob",
#             "number": "+375292222222"
#         },
#         {
#             "type": "office",
#             "number": null
#         }
#     ],
#
# }

import json

with open("test.json", encoding="utf8") as myFile:
    decoder = json.load(myFile)

print(decoder)
print(type(decoder))

# Преобразование словаря в json

import json

decoder = {
    'firstname': 'Катя',
    'lastname': 'Артемьева',
    'isAlive': True,
    'age': 25,
    'address': {
        'streetAddress': 'Независимостиб 69',
        'city': 'Минск'
    },
    'phoneNumbers': [
        {
            'type': 'mob',
            'number': '+375292222222'
        },
        {
            'type': 'office',
            'number': None
        }
    ]

}

with open('toJson.json', 'w', encoding='utf8') as to_json:
    json.dump(decoder, to_json, ensure_ascii=False, indent=4)

with open('toJson.json', encoding='utf8') as to_json:
    print(to_json.read())
