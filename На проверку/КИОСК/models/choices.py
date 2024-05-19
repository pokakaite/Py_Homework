from abc import abstractmethod


# вопросы приложения клиенту, вывод ответа


class Choice:
    def __init__(self):
        self.choice = None

    @abstractmethod
    def set_choice(self):
        pass

    @abstractmethod
    def get_choice(self):
        pass


class Greeting:

    def set_choice(self):
        print('''Добро пожаловать в киоск по продаже хот-догов.
        Вы можете выбрать из трёх стандартных хот-догов или создать свой.
        1 - Выбрать из стандартных.
        2 - Создать свой.''')
        self.choice = int(input('Ваш выбор - '))

    def get_choice(self):
        return self.choice


class StandartOrHandMade:
    def set_choice(self):
        print('Введите номер хот-дога, который хотите попробовать.')
        self.choice = int(input('Ваш выбор - '))

    def get_choice(self):
        return self.choice


class AddIngredient:
    def set_choice(self):
        print('''Желаете добавить топпинги?
        1 - Да
        2 - Нет''')
        self.choice = int(input('Ваш выбор - '))

    def get_choice(self):
        return self.choice
