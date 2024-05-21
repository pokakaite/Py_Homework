from abc import abstractmethod


class Greeting:
    def show(self):
        print('\nДобро пожаловать в пекарню. Я знаю, вы желаете попробовать наши знаменитые пончики.')
        print('На выбор можем предложить:\n')


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


# класс для обычных пончиков-элементов ассортимента

class HandMadeDonutItem:
    def __init__(self, donut):
        self.donut = donut

    def show(self):
        print(f'{self.donut.name} - {self.donut.price + sum(self.donut.topping_price)} рублей '
              f'(Цена меняется в зависимости от посыпок).')


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
        for count, item in enumerate(ShowItems.items, start=1):
            print(f'{count} - ', end='')
            item.show()

# вывод элементов ассортимента
