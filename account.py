# пополнение баланса  счета
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
def print_history(shop_list):
    print('Список  покупок: ')
    for item in shop_list:
        print(item)

# основная программа управления  счетом
def account():
    acc_balance = 0
    shop_list = []
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
            break
        else:
            print('Неверный пункт меню')
