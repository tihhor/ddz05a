import os, shutil

# создание папки
def create_dir():
    new_dir = input('Введите имя  папки: ')
    if new_dir in os.listdir(path="."):
        print('Папка/файл уже существует!')
    else:
        os.mkdir(new_dir)
    print(os.listdir(path="."))

# удаление папки или файла
def del_filedir():
    del_dir = input('Введите имя  папки: ')
    if del_dir not in os.listdir(path="."):
        print('Папка/файл не существует!')
    elif os.path.isdir(del_dir) and len(os.listdir(path=del_dir)) == 0: #удаление пустой папки
        os.rmdir(del_dir)
    elif os.path.isfile(del_dir):  # удаление файла
        os.remove(del_dir)
    else:
        shutil.rmtree(del_dir)  #удаление непустой папки

# копирование папки или файла
def copy_filedir():
    copy_from = input('Введите имя исходной папки/файла: ')
    if  copy_from not in os.listdir(path="."):
        print('Исходный папка/файл не существует!')
    else:
        copy_to = input('Введите имя целевой папки/файла: ')
        if os.path.isfile(copy_from):
            shutil.copyfile(copy_from, copy_to)   #копирование файла
        else:
            shutil.copytree(copy_from, copy_to)   #копрование папки

# содержание рабочей директории
def show_curr_dir():
    print('Рабочая директория:')
    for i in os.listdir(path="."):
        print('    ', i)

def show_dir():
    print('Папки в рабочей директорий:')
    for i in os.listdir(path="."):
        if os.path.isdir(i):
            print('    ', i)

def show_file():
    print('Файлы в рабочей директорий:')
    for i in os.listdir(path="."):
        if os.path.isfile(i):
            print('    ', i)

#изменение текущей директории
def change_dir(start_dir):
    print('Текущая директория ', os.getcwd())
    new_dir = input('Введите имя новой директории (пусто - возврат  к стартовой): ')
    if new_dir == '':
        os.chdir(start_dir)
    elif new_dir not in os.listdir(path="."):
        print('Директория не существует!')
    elif os.path.isdir(new_dir):
        os.chdir(new_dir)
    print('Новая текущая директория ', os.getcwd())
