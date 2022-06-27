import os, json

# добавим звездочки при печати списков покупок
def add_stars(f):
    # inner - итоговая функция с новым поведение
    def inner(*args, **kwargs):
        # поведение до вызова
        print('*' * 50)
        result = f(*args, **kwargs)
        # поведение после вызова
        print('*' * 50)
        return result
    # возвращается функция inner с новым поведением
    return inner

# пополнение баланса счета
def acc_increase(acc_balance):
    acc_balance += int(input('Введите сумму пополнения: '))
    return(acc_balance)

# покупка, добавление списка покупок
def buy(acc_balance,shop_list):
    amount = int(input('Введите сумму покупки: '))
    if  amount > acc_balance:
        print('Денег недостаточно для покупки!')
    else:
        shop_list.append(input('Название покупки: ')+' '+str(amount))
        acc_balance -= amount
    return(acc_balance,shop_list)

# печать списка покупок
@add_stars
def print_history(shop_list):
    print('Список  покупок: ')
    for item in shop_list:
        print(item)

# основная программа управления  счетом

def account():

    # считываем файлы баланса и истории покупок
    try:
        fa = open('acc_bal.txt', 'r')
        # если программа запускается впервые и нет файла с балансом
        # то обрабатывая исключение создаем файлы с балансои и историей покупок
    except FileNotFoundError:
        print('Создаю счет!')
        f = open('acc_bal.txt', 'w')
        f.write('0')
        f.close()
        shop_list = []
        with open('shop_list.json', 'w') as f:
            json.dump(shop_list, f)

    fa = open('acc_bal.txt', 'r')
    acc_balance = int(fa.read())
    fa.close()
    with open('shop_list.json', 'r') as f:
        shop_list = list(json.load(f))

    while True:
        print('Баланс счета: ', acc_balance)
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        # print(acc_balance,shop_list)
        choice = input('Выберите пункт меню ')

        if choice == '1':
            acc_balance = acc_increase(acc_balance)
        elif choice == '2':
            acc_balance, shop_list = buy(acc_balance, shop_list)
        elif choice == '3':
            print_history(shop_list)
        elif choice == '4':
            # сохраняем файлы баланса и истории покупок
            fa = open('acc_bal.txt', 'w')
            fa.write(str(acc_balance))
            fa.close()
            with open('shop_list.json', 'w') as f:
                json.dump(shop_list, f)
            break
        else:
            print('Неверный пункт меню')
