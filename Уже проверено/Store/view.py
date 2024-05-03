from model import *

def menu():
    product = input("\nВведите название товара, который добавить в корзину - ")
    amount = int(input("Введите количество товара - "))
    items = []

    for i in products_list:
        for item in i:
            items.append(item)

    if product not in items:
        print(f'\nК сожалению, товар под названием "{product}" не представлен в нашем магазине :(')
    else:
        for i in products_list:
            for item, price in i.items():
                if product == item:
                    Grocery.busket.append({product: amount})
                    Grocery.summ.append(price * amount)
                    print(f'\nТовар "{product}" добавлен в корзину в количестве {amount} шт.')
                    print(f'Ваша корзина:')
                    count = 0
                    for i in Grocery.busket:
                        count += 1
                        for item, amount in i.items():
                            print(f'{count}. {item} - {amount} шт.')
                    print(f'\nСумма товаров - {sum(Grocery.summ)} рублей.')

def toPay():
    if Grocery.money() < sum(Grocery.summ):
        print('У вас не хватает денег :( Очень жаль!')
    else:
        print('Спасибо за покупку. Ждём вас снова')

def toQuit():
    print('\nДо свидания! Ждём вас снова!')