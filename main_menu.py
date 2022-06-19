# главное меню
from os_func import *
from account  import *
from victory import *

menu_list = [
    '1. создать папку;',
    '2. удалить (файл/папку);',
    '3. копировать (файл/папку);',
    '4. просмотр содержимого рабочей директории;',
    '5. посмотреть только папки;',
    '6. посмотреть только файлы;',    '',
    '7. просмотр информации об ОС;',
    '8. создатель программы;',    '',
    '9. играть в викторину;',
    '10. мой банковский счет;',    '',
    '11. смена директории (*необязательный пункт);',
    '12. выход.',
]
import os
choice = 0
start_dir = os.getcwd()

# печать списка меню
def print_menu():
    print('Выберите пункт меню:')
    for i in menu_list:
        print(i)

while choice != '12':
    print_menu()
    choice = input()
    if choice == '1':
        create_dir()
    elif choice == '2':
        del_filedir()
    elif choice == '3':
        copy_filedir()
    elif choice == '4':
        show_curr_dir()
    elif choice == '5':
        show_dir()
    elif choice == '6':
        show_file()
    elif choice == '7':
        print(os.name)
    elif choice == '8':
        print('*' * 35)
        print('Создатель программы: Е.Трофимов')
        print('*' * 35)
    elif choice == '9':
        victory()
    elif choice == '10':
        account()
    elif choice == '11':
        change_dir(start_dir)
    elif choice == '12':
        print('Программа завершена')

