from abc import abstractmethod

class Donut:
    @abstractmethod
    def show(self):
        pass

class BasicDonat:
    def __init__(self):
        self.name = 'Стандартный пончик'
        self.price = 10
        self.topping = None

    def show(self):
        print(f'{self.name} - {self.price} - {self.topping}')


class ChocoDonut:
    def __init__(self):
        self.name = 'Шоколадный пончик'
        self.price = 20
        self.topping = None

    def show(self):
        print(f'{self.name} - {self.price} - {self.topping}')