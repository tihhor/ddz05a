import os
from victory import *

vic_dict = {'Пушкина': 1799,
            'Эйнштейна': 1879,
            'Толстого': 1828,
            'Ремарка': 1898,
            'Леонардо ДаВинчи': 1452}
# тест для чистой функции
def test_check_answer():
    assert check_answer('1799', str(vic_dict.get('Пушкина')))
    assert check_answer('1828', str(vic_dict.get('Толстого')))
    assert check_answer('1452', str(vic_dict.get('Леонардо ДаВинчи')))

# тест для грязной функции
def test_create_dir(new_dir = 'new_dir'):
    if new_dir in os.listdir(path="."):
        print('Папка/файл уже существует!')
    else:
        os.mkdir(new_dir)

    assert new_dir in os.listdir(path=".")
