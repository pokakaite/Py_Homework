class Menu:
    def __init__(self):
        self.choice = None

    def show(self):
        print('''\nЧто вы хотите сделать?
    1 - Посмотреть данные в таблице,
    2 - Выйти.''')

    def set_choice(self):
        self.choice = int(input('Ваш выбор - '))


class MakeChoice:
    def __init__(self):
        self.choice = None

    def set_choice(self):
        self.choice = int(input('\nВведите номер пункта меню для взаимодействия с таблицей - '))

    def get_choice(self):
        return self.choice


class ChooseSalesman:
    choice = None

    @staticmethod
    def set_choice(salesmen):
        print('\nВыберите продавца.')
        for count, salesman in enumerate(salesmen, start=1):
            print(f'{count} - {salesman.get_name()} {salesman.get_surname()}')
        ChooseSalesman.choice = int(input('\nВаш выбор - '))

    @staticmethod
    def get_choice():
        return ChooseSalesman.choice


class ChooseCustomer:
    choice = None

    @staticmethod
    def set_choice(customers):
        print('\nВыберите покупателя.')
        for count, customer in enumerate(customers, start=1):
            print(f'{count} - {customer.get_name()} {customer.get_surname()}')
        ChooseCustomer.choice = int(input('\nВаш выбор - '))

    @staticmethod
    def get_choice():
        return ChooseCustomer.choice
