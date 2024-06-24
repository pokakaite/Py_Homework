class Menu:
    def __init__(self):
        self.choice = None

    def show(self):
        print('''\nЧто вы хотите сделать?
    1 - Посмотреть данные в таблице,
    2 - Выйти.''')

    def set_choice(self):
        self.choice = int(input('Ваш выбор - '))


class ChoicesDict:
    def __init__(self):
        self.choices = {
            1: 'Отображение всех сделок',
            2: 'Отображение сделок конкретного продавца',
            3: 'Отображение максимальной по сумме сделки',
            4: 'Отображение минимальной по сумме сделки',
            5: 'Отображение максимальной по сумме сделки для конкретного продавца',
            6: 'Отображение минимальной по сумме сделки для конкретного продавца',
            7: 'Отображение максимальной по сумме сделки для конкретного покупателя',
            8: 'Отображение минимальной по сумме сделки для конкретного покупателя',
            9: 'Отображение продавца, у которого максимальная сумма продаж по всем сделкам',
            10: 'Отображение продавца, у которого минимальная сумма продаж по всем сделкам',
            11: 'Отображение покупателя, у которого максимальная сумма продаж по всем сделкам',
            12: 'Отображение покупателя, у которого минимальная сумма продаж по всем сделкам',
            13: 'Отображение средней суммы покупки для конкретного покупателя',
            14: 'Отображение средней суммы покупки для конкретного покупателя'
        }


class ShowChoicesMenu:
    @staticmethod
    def show(choices):
        print()
        for key, value in choices.items():
            print(f'{key} - {value}')


class MakeChoice:
    def __init__(self):
        self.choice = None

    def set_choice(self):
        self.choice = int(input('\nВведите номер пункта меню для взаимодействия с таблицей - '))

    def get_choice(self):
        return self.choice

# def show_sales_of_salesman(conn, cursor, sales, salesman):
#     conn.commit()
#     cursor.execute(f"""SELECT Salesman, Customer, Item, Price
#                     FROM {sales.table_name}
#                     WHERE Salesman = '{salesman.name} {salesman.surname}'""")
#     # for string in sales.table_name:
#     # print(cursor.fetchall())


# class GetAllSales:
#     def get_all_sales(self, conn, cursor, table):
#         conn.commit()
#         cursor.execute(f"""SELECT * FROM {table.table_name}""")
#
# class ShowAllSales:
#     def show(self, cursor, table):
#         print('+' * 98)
#         print(
#             f'| {table.column_salesman:^25} | {table.column_customer:^25} | {table.column_item:^25} | {table.column_price:^10} |')
#         print('+' * 98)
#
#         for string in cursor.fetchall():
#             print(f'| {string[0]:^25} | {string[1]:^25} | {string[2]:^25} | {string[3]:^10} |')
#             print('-' * 98)
