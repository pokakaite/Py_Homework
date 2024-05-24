from abc import abstractmethod


class Donut:
    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def add_topping(self, topping):
        pass

    @abstractmethod
    def show_toppings(self):
        pass

    @abstractmethod
    def get_info(self):
        pass


class BasicDonat(Donut):
    def __init__(self):
        self.name = 'Стандартный пончик'
        self.price = 10
        self.toppings = []
        self.topping_price = []


    def show(self):
        print(f'{self.name}. Стоимость - {self.price} рублей.')

    def add_topping(self, topping):
        self.toppings.append(topping.name)
        self.topping_price.append(topping.price)


    def show_toppings(self):
        print('\tСостав:\n\t1. Пончик,\n\t2. Топпинги:')
        for count, topping in enumerate(self.toppings, start=1):
            print(f'\t\t{count}. {topping}.')
        print()

    def get_info(self):
        return f'''Название - {self.name}. Стоимость - {self.price} рублей.
        Состав:\n\t1. Пончик,\n\t2. Топпинги:
        {[i for i in self.toppings]}\n'''



class ChocoDonut(Donut):
    def __init__(self):
        self.name = 'Шоколадный пончик'
        self.price = 10
        self.toppings = []
        self.topping_price = []


    def show(self):
        print(f'{self.name}. Стоимость - {self.price} рублей.')

    def add_topping(self, topping):
        self.toppings.append(topping.name)
        self.topping_price.append(topping.price)

    def show_toppings(self):
        print('\tСостав:\n\t1. Пончик,\n\t2. Топпинги:')
        for count, topping in enumerate(self.toppings, start=1):
            print(f'\t\t{count}. {topping}.')
        print()

    def get_info(self):
        return f'''Название - {self.name}. Стоимость - {self.price} рублей.
        Состав:\n\t1. Пончик,\n\t2. Топпинги:
        {[i for i in self.toppings]}\n'''


class SimpsonsDonut(Donut):
    def __init__(self):
        self.name = 'Пончик "Из Симпсонов"'
        self.price = 10
        self.toppings = []
        self.topping_price = []


    def show(self):
        print(f'{self.name}. Стоимость - {self.price} рублей.')

    def add_topping(self, topping):
        self.toppings.append(topping.name)
        self.topping_price.append(topping.price)

    def show_toppings(self):
        print('\tСостав:\n\t1. Пончик,\n\t2. Топпинги:')
        for count, topping in enumerate(self.toppings, start=1):
            print(f'\t\t{count}. {topping}.')
        print()

    def get_info(self):
        return f'''Название - {self.name}. Стоимость - {self.price} рублей.
        Состав:\n\t1. Пончик,\n\t2. Топпинги:
        {[i for i in self.toppings]}\n'''

class HandMadeDonut(Donut):
    def __init__(self):
        self.name = 'Пончик "Сделай сам"'
        self.price = 10
        self.toppings = []
        self.topping_price = []


    def show(self):
        print(f'{self.name}. Стоимость - {self.price} рублей (Цена меняется в зависимости от топпингов).')

    def add_topping(self, topping):
        self.toppings.append(topping.name)
        self.topping_price.append(topping.price)

    def show_toppings(self):
        print('\tСостав:\n\t1. Пончик,\n\t2. Топпинги:')
        for count, topping in enumerate(self.toppings, start=1):
            print(f'\t\t{count}. {topping}.')
        print()

    def get_info(self):
        return f'''Название - {self.name}. Стоимость - {self.price} рублей.
        Состав:\n\t1. Пончик,\n\t2. Топпинги:
        {[i for i in self.toppings]}\n'''