from abc import abstractmethod


class Greeting:
    def show(self):
        print('Наши пончики:')


class Item:
    @abstractmethod
    def show(self):
        pass


class DonutItem:
    def __init__(self, donut):
        self.donut = donut
    def show(self):
        print(f'{self.donut.name} - {self.donut.price} рублей.')


class ListItems:
    def __init__(self):
        self.list = []

    def add_to_list(self, item):
        self.list.append(item)

    def get_list(self):
        return self.list



class ShowItems:
    def show(self, items):
        count = 0
        for item in items:
            count += 1
            print(f'{count} - ', end='')
            item.show()