def paren_checker(string):
    stack = []  # объявляем стек
    pars = {")": "(", "]": "[", "}": "{"}  # Добавляем словарь

    for s in string:
        if s in pars.values():
            stack.append(s)  # добавляем скобку в стек
        elif s in pars.keys():
            # если находим закрывающую скобку, то проверяем,
            # пуст ли стек, и является ли верхний элемент открывающей скобкой
            if len(stack) > 0 and stack[-1] == pars[s]:
                stack.pop()  # удаляем из стека
            else:  # иначе завершаем функцию с False
                return False
    return len(stack) == 0


# Проверяем работу проверки фигурных скобок
string_1 = '}ghbdtn { *'
string_2 = '{dsa}'
print(f'string_1 = {paren_checker(string_1)}', f'string_2 = {paren_checker(string_2)}', sep='\n')

