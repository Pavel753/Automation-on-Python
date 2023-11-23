# Напишите программу, которая запрашивает у пользователя число минут и выводит их в виде дни: часы:минуты

minutes_in = int(input('Введите количество минут: '))

days = minutes_in // 1440
hours = minutes_in % 1440 // 60
minutes = minutes_in % 60

print(days, hours, minutes, sep=':')