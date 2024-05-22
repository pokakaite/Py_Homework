from abc import abstractmethod


class Greeting:
    def show(self):
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
        print(f'{self.donut.name} - {self.donut.price + sum(self.donut.topping_price)} рублей.')

    def get_donut(self):
        return f'{self.donut.name} - {self.donut.price + sum(self.donut.topping_price)} рублей.'

    def get_donut_price(self):
        return self.donut.price + sum(self.donut.topping_price)

    def get_donut_name(self):
        return self.donut.name


# класс для обычных пончиков-элементов ассортимента

class HandMadeDonutItem:
    def __init__(self, donut):
        self.donut = donut

    def show(self):
        print(f'{self.donut.name} - {self.donut.price + sum(self.donut.topping_price)} рублей '
              f'(Цена меняется в зависимости от посыпок).')

    def get_donut(self):
        return f'{self.donut.name} - {self.donut.price + sum(self.donut.topping_price)} рублей.'

    def get_donut_price(self):
        return self.donut.price + sum(self.donut.topping_price)

    def get_donut_name(self):
        return self.donut.name


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
    items = None

    @staticmethod
    def set_list(items):
        ShowItems.items = items

    @staticmethod
    def show():
        print()
        for count, item in enumerate(ShowItems.items, start=1):
            print(f'{count} - ', end='')
            item.show()

# вывод элементов ассортимента


class Order:
    def __init__(self):
        self.order_items = []

    def add_to_order(self, item):
        self.order_items.append(item)

    def get_order(self):
        return self.order_items

    def show(self):
        print('\nВаш заказ:')
        for count, item in enumerate(self.order_items, start=1):
            print(f'{count}. {item}')
        if len(self.order_items) >= 3:
            print('Ваша скидка - 10%')


class ShowOrderSumm:
    @staticmethod
    def show(summ):
        print(f'Стоимость заказа - {summ} рублей.')