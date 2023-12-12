# Игра викторина

# Записываем все вопросы, варианты ответов,ответы информацию по теме в списоки
questions = ['Какой объем памяти имела автоматическая цифровая вычислительная машина М-1?',
             'Какого числа отмечается День программиста (256 день в году) в високосный год?',
             'Мотылек замкнул крылышками контакты. Какое жаргонное слово в программировании появилось по этому случаю?',
             'Какому устройству дал имя винтовочный патрон американского происхождения?',
             'Создание какого языка программирования пока не отмечено премией Тьюринга?',
             'Как называют шуточный секрет, заложенный создателями в ПО?',
             'Идеи двоичного кодирования были заложены?',
             'Какова была тактовая частота у первой модели персонального компьютера фирмы IBM?',
             'Первая ЭВМ в СССР называлась?',
             'Первым изобретателем перфокарт был?'
             ]
answer_options = ['Выберите колличество слов - 1: 1000000/2: 1024/3: 256/4: 1000',
                  '1: 12 сентября/2: 13 сентября/3: 4 декабря/4: 1 сентября',
                  '1: error/2: bug/3: breakdown/4: mistake',
                  '1: ROM/2: CPU/3: RAM/4: HDD',
                  '1: Алгол/2: Фортран/3: Модула/4: Си',
                  '1: оладушка/2: колядка/3: пасхалка/4: сырок',
                  '1: Джоном фон Нейманом/2: Готфрид Вильгельм Лейбницом/3: Адой Лавлейс/4: Чарльзом Беббиджем',
                  '1: 4,77 ГГц/2: 8 МГц/3: 4,77 МГц/4: 8800 Гц',
                  '1: Стрела/2: МЭСМ/3: IBM PC/4: БЭСМ',
                  '1: Д. Неппер/2: В. Шиккард?/3: Ж. Жаккард/4: Б. Паскаль'
                  ]
answers = ['3', '1', '2', '4', '4', '3', '2', '3', '2', '3']
information = ['''Технические характеристики:
Система счисления: двоичная, 25 разрядов в машинном слове.
Быстродействие: 20 операций в секунду над 25-разрядными словами.
Память: 256 слов на магнитном барабане''',
               'В невисокосный год данный праздник выпадает на 13 сентября, в високосный — на 12 сентября.',
               '''По легенде, 10 сентября 1945 года учёные Гарвардского университета, 
тестировавшие вычислительнуюмашину Mark II Aiken Relay Calculator, нашли мотылька, застрявшего между контактами
электромеханического реле и Грейс Хоппер произнесла этот термин. Извлечённое насекомое было вклеено
в технический дневник, с сопроводительной надписью: «First actual case of bug being found»
(англ. «первый случай в практике, когда был обнаружен жучок»). Этот забавный факт положил
начало использованию слова «баг» в значении «ошибка»''',
               '.30-30 Winchester — винтовочный патрон американского происхождения; '
               'один из самых старых патронов, выпускаемых в настоящее время.',
               '''Премия Тьюринга — престижная награда в области информатики.
Присуждается старейшей(основана в 1947 году) Ассоциацией вычислительной техники (Association for Computing Machinery).
Считается аналогом Нобелевской премии в области информатики.''',
               '''«Пасхальное яйцо» (англ. Easter Egg) — секрет в компьютерной игре, фильме или программном обеспечении,
заложенный создателями. Пасхальные яйца играют роль своеобразных шуток для внимательных игроков или зрителей, 
но могут применяться в целях защиты авторских прав. Название происходит от популярного в США и бывших Британских 
колониях семейного мероприятия «охота за яйцами» (англ. egg hunt), устраиваемого накануне Пасхи, в котором участники 
должны с помощью подсказок найти как можно больше спрятанных по местности яиц.''',
               '''Двои́чный код — это способ представления данных в виде кода, в котором каждый разряд принимает одно из 
двух возможных значений, обычно обозначаемых цифрами 0 и 1. Разряд в этом случае называется двоичным разрядом.Одним из 
первых заинтересовался двоичной системой гениальный немецкий ученый Готфрид Вильгельм Лейбниц.''',
               '''Первый персональный компьютер стоил 1 565 долларов, был прост в использовании и занимал сравнительно 
               мало места. IBM 5150 был оснащен процессором Intel 8088 с тактовой частотой 4,77 мегагерца и 
               предустановленной оперативной памятью размером 16 или 64 килобайт.''',
               '''В 1948 году была собрана модель первого отечественного компьютера — Малая Электронная Счетная Машина(МЭСМ).
Устройство занимало почти все пространство комнаты площадью в 60 м2. Она могла производить до трех тысяч
счетно-вычислительных операций в минуту, что по меркам того времени было заоблачно много.''',
               '''Информация представлена наличием или отсутствием отверстия в определённой позиции карты из тонкого картона.
1808 год — ткацкий станок Жаккарда (управление узором), 1920-е—1950-е — бухгалтерские машины (табуляторы), 
позднее — компьютеры первого поколения (основной носитель для хранения и обработки данных). Позднее для хранения и ввода.'''
               ]
scorepoints = 0  # создаем счетчик очков

# Начинаем игру
print('Добро пожаловать в IT викторину!')
answer = input('Хотите поиграть(Да/Нет): ')

if answer.lower().replace(' ', '') == 'да':
    for i in range(len(questions)):
        print(questions[i], answer_options[i])
        answer = input('Введите номер ответа: ')
        if answer.lower().replace(' ', '') == answers[i]:
            print('Верно!', information[i], '', sep='\n')
            scorepoints += 1
        else:
            print('Не верно!', information[i], '', sep='\n')
    if scorepoints == len(questions):
        print(f'Ты молодец и набрал максимальное количество очков: {scorepoints}')
    elif scorepoints >= 0.5 * len(questions):
        print(f'Молодец. Набрал {scorepoints} очков  из {len(questions)})')
    elif scorepoints > 0:
        print(f'Ты набрал {scorepoints} очков из {len(questions)}')
    else:
        print('Ты набрал 0 очков, но узнал для себя что-то новое')

elif answer.lower().replace(' ', '') == 'нет':
    print('Очень жаль. Ждем тебя в следующий раз)')

else:
    print('Введено неверное значение. Попробуйте еще раз')
