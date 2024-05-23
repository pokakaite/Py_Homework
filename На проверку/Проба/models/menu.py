from abc import abstractmethod


class Greeting:
    @staticmethod
    def show():
        print('\nДобро пожаловать в пекарню. Я знаю, вы желаете попробовать наши знаменитые пончики.')
        print('На выбор можем предложить:')


# приветствие


class Item:
    @abstractmethod
    def show(self):
        pass


# абстрактный класс для элементов ассортимента


class DonutItem:
    def __init__(self, donut):
        self.donut = donut

    def show(self):
        print(f'{self.donut.name} - {self.donut.price} рублей.')

    def get_donut(self):
        return f'{self.donut.name} - {self.donut.price} рублей.'


# класс для обычных пончиков-элементов ассортимента

class HandMadeDonutItem:
    def __init__(self, donut):
        self.donut = donut

    def show(self):
        print(f'{self.donut.name} - {self.donut.price} рублей '
              f'(Цена меняется в зависимости от посыпок).')

    def get_donut(self):
        return f'{self.donut.name} - {self.donut.price} рублей.'


# класс для самодельного пончика-элемента ассортимента


class ListItems:
    def __init__(self):
        self.list = []

    def add_to_list(self, item):
        self.list.append(item)

    def get_list(self):
        return self.list


# класс для создания списка элементов ассортимента


class ShowItems:
    def __init__(self, items):
        self.items = items

    def show(self):
        print()
        for count, item in enumerate(self.items, start=1):
            print(f'{count} - ', end='')
            item.show()
        print()


# вывод элементов ассортимента


class ToppingAmount:
    def __init__(self, toppings):
        self.toppings = toppings

    def show_warning(self):
        for topping in self.toppings:
            if topping.amount <= 3:
                print('\nИнформация для сотрудников:')
                print(f'Топпинга "{topping.name}" осталось {topping.amount} штук(и). Нужно пополнить запасы.\n')

    def show(self):
        for topping in self.toppings:
            print(f'Топпинга "{topping.name}" осталось {topping.amount} штук(и).')
            if topping.amount <= 3:
                print('Нужно пополнить запасы.')


class RefillTopping:
    def __init__(self):
        self.choice = None

    def if_refill(self, topping):
        if topping.amount <= 3:
            self.choice = int(input('Введите "1", чтобы пополнить запасы - '))

    def get_choice(self):
        return self.choice

    def refill(self, topping, choice):
        if choice == 1 and topping.amount <= 3:
            topping.amount += 3
            print(f'Запасы топпинга "{topping.get_name()}" успешно пополнены :)')

class Order_Item:
    def __init__(self, item):
        self.item = item


class OrderList:
    def __init__(self):
        self.order_items = []

    def add_to_order(self, item):
        self.order_items.append(item)

    def get_order(self):
        return self.order_items

    def show(self):
        print('\nВаш заказ:')
        for count, item in enumerate(self.order_items, start=1):
            print(f'{count}. {item.name}. Стоимость - {item.price} рублей.')
        if len(self.order_items) >= 3:
            print('Ваша скидка - 10%')
        print()


class ShowOrderSumm:
    def show(self, summ):
        print(f'Стоимость заказа - {summ} рублей.')


class File:
    def __init__(self):
        self.name = 'check.txt'

    def add_to_file(self, order):
        with open(self.name, 'w+', encoding='utf-8') as f:
            for count, item in enumerate(order, start=1):
                f.write(str(f'{count}. {item.get_info()}\n'))
            f.close()


class Wish:
    def show(self):
        print('Оплата прошла успешно. Приятного аппетита.')


