import json

# открытие txt файла с помощью with
with open('5_Interstellar.txt', encoding="utf8") as MyFile:
    for line in MyFile:
        print(line)

# открытие файла с помощью for ... in
myFile = open('5_Interstellar.txt', encoding="utf8")
for line in myFile:
    print(line)

# открытие json файла с помощью with
with open('5-response_1700209207400.json', encoding='utf8') as to_json:
    print(to_json.read())

# запись документа в json
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
