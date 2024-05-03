from view import *
from model import *

def start():
    choice = int(input('''\nЧто вы хотите сделать?
    1 - Добавить товар в корзину,
    2 - Оплатить покупки,
    3 - Уйти из магазина
    '''))
    if choice == 1:
        Grocery.addToBusket()
        return start()
    if choice == 2:
        return toPay()
    if choice == 3:
        return toQuit()

if __name__ == "__main__":
    start()
