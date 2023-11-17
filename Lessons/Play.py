print('Привет!')
answer = input('Готов к игре? (yes/no):')
score = 0
total_questions = 3

if answer.lower() == 'yes':
    answer = input('Вопрос 1: Какой ЯП ты изучаешь?')
    if answer.lower() == 'python':
        score += 1
        print('Отличный выбор!')
    else:
        print('Штош...:(')

    answer = input('Вопрос 2: Планируешь ли ты стать автоматизатором?')
    if answer.lower() == 'yes':
        score += 1
        print('Правильное решение!')
    else:
        print('Подумай ещё раз')

    answer = input('Вопрос 3: Тебе нравится учиться?')
    if answer.lower() == 'yes':
        score += 1
        print('Я рад!')
    else:
        print('Как жаль')

print('Спасибо, что поиграли со мной. Вы ответили на', score, 'вопроса правильно!')
mark = (score / total_questions) * 1000
print('Заработано:', mark)
print('Пока!')
