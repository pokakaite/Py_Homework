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


class BasicDonat(Donut):
    def __init__(self):
        self.name = 'Стандартный пончик'
        self.price = 10
        self.toppings = []
        self.topping_price = []


    def show(self):
        print(f'\nНазвание - {self.name}. Стоимость - {self.price + sum(self.topping_price)} рублей.')

    def add_topping(self, topping):
        self.toppings.append(topping.name)
        self.topping_price.append(topping.price)


    def show_toppings(self):
        print('Состав:\nПончик,\n\tТоппинги:')
        for count, topping in enumerate(self.toppings, start=1):
            print(f'\t{count}. {topping}.')


class ChocoDonut(Donut):
    def __init__(self):
        self.name = 'Шоколадный пончик'
        self.price = 10
        self.toppings = []
        self.topping_price = []


    def show(self):
        print(f'\nНазвание - {self.name}. Стоимость - {self.price + sum(self.topping_price)} рублей.')

    def add_topping(self, topping):
        self.toppings.append(topping.name)
        self.topping_price.append(topping.price)

    def show_toppings(self):
        print('Состав:\nПончик,\n\tТоппинги:')
        for count, topping in enumerate(self.toppings, start=1):
            print(f'\t{count}. {topping}.')


class HandMadeDonut(Donut):
    def __init__(self):
        self.name = 'Пончик "Сделай сам"'
        self.price = 10
        self.toppings = []
        self.topping_price = []


    def show(self):
        print(f'\nНазвание - {self.name}. Стоимость - {self.price + sum(self.topping_price)} рублей.')

    def add_topping(self, topping):
        self.toppings.append(topping.name)
        self.topping_price.append(topping.price)

    def show_toppings(self):
        print('Состав:\nПончик,\n\tТоппинги:')
        for count, topping in enumerate(self.toppings, start=1):
            print(f'\t{count}. {topping}.')