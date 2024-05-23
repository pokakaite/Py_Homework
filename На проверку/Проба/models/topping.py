from abc import abstractmethod

class Topping:
    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_price(self):
        pass


class Sugar(Topping):
    def __init__(self):
        self.name = 'Сахарная посыпка'
        self.price = 5
        self.amount = 5

    def show(self):
        print(f'{self.name}. Стоимость - {self.price} рублей.')

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price


class ChocolateGlaze(Topping):
    def __init__(self):
        self.name = 'Шоколадная глазурь'
        self.price = 10
        self.amount = 5

    def show(self):
        print(f'{self.name}. Стоимость - {self.price} рублей.')

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price


class StrawberryGlaze(Topping):
    def __init__(self):
        self.name = 'Клубничная глазурь'
        self.price = 10
        self.amount = 5

    def show(self):
        print(f'{self.name}. Стоимость - {self.price} рублей.')

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price


class Sprinkles(Topping):
    def __init__(self):
        self.name = 'Разноцветная посыпка'
        self.price = 5
        self.amount = 5

    def show(self):
        print(f'{self.name}. Стоимость - {self.price} рублей.')

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price