"""
Год рождения
============
Пушкин 1799
Эйнштейн 1879
Толстой 1828
Ремарк 1898
Леонардо ДаВинчи  1452
"""

from account import add_stars
# используем декоратор из списка покупок
@add_stars
def victory(victory_dict = {'Пушкина': 1799,
            'Эйнштейна': 1879,
            'Толстого': 1828,
            'Ремарка': 1898,
            'Леонардо ДаВинчи': 1452}):

    while True:
        right_answers = 0
        for name, year in victory_dict.items():
            print('Год рождения '+name+'?')
# тернарный оператор
            right_answers += 1 if check_answer(input(), str(year)) else 0
        print('Правильных ответов:', right_answers)
        print('Количество неправильных ответов:', 5-right_answers)
        print('Процент правильных ответов:', right_answers/5*100)
        print('Процент неправильных ответов:', (5-right_answers)/5*100)

        if input('Новая игра? ') != 'Да':
            break

    print('Игра окончена!')

def check_answer(in_ans, right_ans):
    return(in_ans == right_ans)
