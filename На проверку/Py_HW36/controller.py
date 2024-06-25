class Menu:
    def __init__(self):
        self.choice = None

    def set_choice(self):
        print('''\nЧто вы хотите сделать?
    1 - Посмотреть данные в таблице,
    2 - Обновить данные в таблице,
    3 - Добавить данные в таблицу,
    4 - Удалить данные в таблице,
    5 - Выйти''')
        self.choice = int(input('Ваш выбор - '))

    def get_choice(self):
        return self.choice


class MakeChoice:
    def __init__(self):
        self.choice = None

    def set_choice(self):
        self.choice = int(input('\nВведите номер пункта меню для взаимодействия с таблицей - '))

    def get_choice(self):
        return self.choice


# class MenuUpdate:
#     def __init__(self):
#         self.choice = None
#
#     def set_choice(self):
#         print('''\nВведите Id сделки, которую хотите обновить.''')
#         self.choice = int(input('Ваш выбор - '))
#
#     def get_choice(self):
#         return self.choice


class ChooseSalesman:
    def __init__(self, salesmen):
        self.choice = None
        self.salesmen = salesmen
        self.name = ''

    def set_choice(self):
        print('\nВыберите продавца.')
        for count, salesman in enumerate(self.salesmen, start=1):
            print(f'{count} - {salesman.get_name()} {salesman.get_surname()}')
        self.choice = int(input('\nВаш выбор - '))
        self.name += f'{self.salesmen[self.choice - 1].get_name()} {self.salesmen[self.choice - 1].get_surname()}'

    def get_choice(self):
        return self.choice

    def get_name(self):
        return self.name


class ChooseCustomer:
    def __init__(self, customers):
        self.choice = None
        self.customers = customers
        self.name = ''

    def set_choice(self):
        print('\nВыберите покупателя.')
        for count, customer in enumerate(self.customers, start=1):
            print(f'{count} - {customer.get_name()} {customer.get_surname()}')
        self.choice = int(input('\nВаш выбор - '))
        self.name += f'{self.customers[self.choice - 1].get_name()} {self.customers[self.choice - 1].get_surname()}'

    def get_choice(self):
        return self.choice

    def get_name(self):
        return self.name


class ChooseItem:
    def __init__(self, items):
        self.choice = None
        self.items = items
        self.item = ''

    def set_choice(self):
        print('\nВыберите товар.')
        for count, item in enumerate(self.items, start=1):
            print(f'{count} - {item.get_item()}')
        self.choice = int(input('\nВаш выбор - '))
        self.item += f'{self.items[self.choice - 1].get_item()}'

    def get_choice(self):
        return self.choice

    def get_item(self):
        return self.item


class SetSalesmanName:
    def __init__(self):
        self.new_name = None

    def set_name(self):
        self.new_name = input('\nВведите новое имя продавца - ')

    def get_name(self):
        return self.new_name


class SetCustomerName:
    def __init__(self):
        self.new_name = None

    def set_name(self):
        self.new_name = input('\nВведите новое имя покупателя - ')

    def get_name(self):
        return self.new_name

class SetItem:
    def __init__(self):
        self.new_item = None

    def set_item(self):
        self.new_item = input('\nВведите новое название товара - ')

    def get_item(self):
        return self.new_item


class SetPrice:
    def __init__(self):
        self.price = None

    def set_price(self):
        self.price = int(input('\nВведите сумму сделки - '))

    def get_price(self):
        return self.price
