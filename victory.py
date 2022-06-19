"""
Год рождения

Пушкин 1799
Эйнштейн 1879
Толстой 1828
Ремарк 1898
Леонардо ДаВинчи  1452
"""
def victory():

    while True:
        right_answers = 0
        if input('Год рождения Пушкина? ') == '1799':
            right_answers += 1

        if input('Год рождения Эйншейна? ') == '1879':
            right_answers += 1

        if input('Год рождения Толстого? ') == '1828':
            right_answers += 1

        if input('Год рождения Ремарка? ') == '1898':
            right_answers += 1

        if input('Год рождения Леонардо ДаВинчи? ') == '1452':
            right_answers += 1

        print('Правильных ответов:', right_answers)
        print('Количество неправильных ответов:', 5-right_answers)
        print('Процент правильных ответов:', right_answers/5*100)
        print('Процент неправильных ответов:', (5-right_answers)/5*100)

        if input('Новая игра? ') != 'Да':
            break

    print('Игра окончена!')

