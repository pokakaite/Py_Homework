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

class Show:
    @staticmethod
    def show_table(cursor, table):
        print('-' * 98)
        print(
            f'| {table.column_salesman:^25} | {table.column_customer:^25} | {table.column_item:^25} | {table.column_price:^10} |')
        print('-' * 98)

        for string in cursor.fetchall():
            print(f'| {string[0]:^25} | {string[1]:^25} | {string[2]:^25} | {string[3]:^10} |')
            print('-' * 98)

class ShowAllSales:
    @staticmethod
    def show(conn, cursor, table):
        conn.commit()
        cursor.execute(f"""SELECT * FROM {table.table_name}""")
        Show.show_table(cursor, table)


class ShowSalesOneSalesman:
    @staticmethod
    def show(conn, cursor, table, salesmen, salesman):
        conn.commit()

        cursor.execute(f'''SELECT Salesman, Customer, Item, Price
                        FROM {table.table_name}
                        WHERE Salesman = "{salesmen[salesman - 1].get_name()} {salesmen[salesman - 1].get_surname()}"''')
        Show.show_table(cursor, table)


class ShowMaxSumSale:

    @staticmethod
    def show(conn, cursor, table):
        conn.commit()
        cursor.execute(f'''SELECT Salesman, Customer, Item, MAX(Price)
                    FROM {table.table_name}''')
        Show.show_table(cursor, table)


class ShowMinSumSale:
    @staticmethod
    def show(conn, cursor, table):
        conn.commit()
        cursor.execute(f'''SELECT Salesman, Customer, Item, MIN(Price)
                    FROM {table.table_name}''')
        Show.show_table(cursor, table)



class ShowMaxSumSaleOneSalesman:

    @staticmethod
    def show(conn, cursor, table, salesmen, salesman):
        conn.commit()
        cursor.execute(f'''SELECT Salesman, Customer, Item, MAX(Price)
                    FROM {table.table_name}
                    WHERE Salesman = "{salesmen[salesman - 1].get_name()} {salesmen[salesman - 1].get_surname()}"''')
        Show.show_table(cursor, table)


class ShowMinSumSaleOneSalesman:

    @staticmethod
    def show(conn, cursor, table, salesmen, salesman):
        conn.commit()
        cursor.execute(f'''SELECT Salesman, Customer, Item, MIN(Price)
                    FROM {table.table_name}
                    WHERE Salesman = "{salesmen[salesman - 1].get_name()} {salesmen[salesman - 1].get_surname()}"''')
        Show.show_table(cursor, table)


class ShowMaxSumSaleOneCustomer:

    @staticmethod
    def show(conn, cursor, table, customers, customer):
        conn.commit()
        cursor.execute(f'''SELECT Salesman, Customer, Item, MAX(Price)
                    FROM {table.table_name}
                    WHERE Customer = "{customers[customer - 1].get_name()} {customers[customer - 1].get_surname()}"''')
        Show.show_table(cursor, table)


class ShowMinSumSaleOneCustomer:

    @staticmethod
    def show(conn, cursor, table, customers, customer):
        conn.commit()
        cursor.execute(f'''SELECT Salesman, Customer, Item, MIN(Price)
                    FROM {table.table_name}
                    WHERE Customer = "{customers[customer - 1].get_name()} {customers[customer - 1].get_surname()}"''')
        Show.show_table(cursor, table)


class ShowMaxSumSalesOneSalesman:

    @staticmethod
    def show(conn, cursor, table):
        conn.commit()
        cursor.execute(f'''SELECT Salesman, SUM(Price) AS SP
                    FROM {table.table_name}
                    GROUP BY Salesman''')

        print('-' * 98)
        print(
            f'| {table.column_salesman:^25} | | {table.column_price:^10} |')
        print('-' * 98)
        for string in cursor.fetchall():
            print(f'| {string[0]:^25} | {string[1]:^25} |')
            print('-' * 98)

