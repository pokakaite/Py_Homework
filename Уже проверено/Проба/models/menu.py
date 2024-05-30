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
        print()
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


class Check:
    def __init__(self):
        self.name = 'check.txt'

    def add_to_check(self, order):
        self.order = order
        with open(self.name, 'w+', encoding='utf-8') as f:
            for count, item in enumerate(self.order, start=1):
                f.write(str(f'{count}. {item.get_info()}\n'))
            f.close()

    def get_check(self):
        with open(self.name, 'r+', encoding='utf-8') as f:
            self.info = f.read()
            f.close()
            return self.info


class OrdersSumm:
    def __init__(self):
        self.orders_summ = []

    def add_to_orders_summ(self, order_summ):
        self.orders_summ.append(order_summ)

    def get_orders_summ(self):
        return self.orders_summ


class SalesFile:
    def __init__(self):
        self.name = 'sales.txt'
        self.count = 0

    def add_to_file(self, order, income, revenue):
        with open(self.name, 'a+', encoding='utf-8') as f:
            self.count += 1
            f.write(str(f'\n\t\tЗаказ №{self.count}:\n'))
            f.write(str(order))
            f.write(str(f'Выручка: {revenue} рублей.\n'))
            f.write(str(f'Прибыль: {income} рублей.\n'))
            f.close()

    def show(self):
        with open(self.name, 'r+', encoding='utf-8') as f:
            self.info = f.read()
            print(self.info)
            f.close()


class Wish:

    @staticmethod
    def show():
        print('\nОплата прошла успешно. Приятного аппетита.\n')
