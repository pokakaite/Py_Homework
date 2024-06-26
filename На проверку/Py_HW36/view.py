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
            13: 'Отображение средней суммы покупки для конкретного продавца',
            14: 'Отображение средней суммы покупки для конкретного покупателя'
        }


class ShowChoicesMenu:
    @staticmethod
    def show(choices):
        print()
        for key, value in choices.items():
            print(f'{key} - {value}')


class Show:
    def __init__(self, conn, cursor, table):
        self.conn = conn
        self.cursor = cursor
        self.table = table

    def show_table(self):
        print('-' * 105)
        print(
            f'| {'Id':^4} | {self.table.column_salesman:^25} | {self.table.column_customer:^25} | {self.table.column_item:^25} | {self.table.column_price:^10} |')
        print('-' * 105)

        for count, string in enumerate(self.cursor.fetchall(), start=1):
            print(f'| {count:^4} | {string[0]:^25} | {string[1]:^25} | {string[2]:^25} | {string[3]:^10} |')
            print('-' * 105)


class ShowAllSales(Show):
    def show(self):
        self.conn.commit()
        self.cursor.execute(f"""SELECT * FROM {self.table.table_name}""")


class ShowSalesOneSalesman(Show):
    def show(self, salesman):
        self.conn.commit()
        self.cursor.execute(f'''SELECT Salesman, Customer, Item, Price
                        FROM {self.table.table_name}
                        WHERE Salesman = "{salesman}"''')


class ShowMaxSumSale(Show):
    def show(self):
        self.conn.commit()
        self.cursor.execute(f'''SELECT Salesman, Customer, Item, MAX(Price)
                    FROM {self.table.table_name}''')


class ShowMinSumSale(Show):

    def show(self):
        self.conn.commit()
        self.cursor.execute(f'''SELECT Salesman, Customer, Item, MIN(Price)
                    FROM {self.table.table_name}''')


class ShowMaxSumSaleOneSalesman(Show):

    def show(self, salesman):
        self.conn.commit()
        self.cursor.execute(f'''SELECT Salesman, Customer, Item, MAX(Price)
                    FROM {self.table.table_name}
                    WHERE Salesman = "{salesman}"''')


class ShowMinSumSaleOneSalesman(Show):

    def show(self, salesman):
        self.conn.commit()
        self.cursor.execute(f'''SELECT Salesman, Customer, Item, MIN(Price)
                    FROM {self.table.table_name}
                    WHERE Salesman = "{salesman}"''')


class ShowMaxSumSaleOneCustomer(Show):

    def show(self, customer):
        self.conn.commit()
        self.cursor.execute(f'''SELECT Salesman, Customer, Item, MAX(Price)
                    FROM {self.table.table_name}
                    WHERE Customer = "{customer}"''')


class ShowMinSumSaleOneCustomer(Show):

    def show(self, customer):
        self.conn.commit()
        self.cursor.execute(f'''SELECT Salesman, Customer, Item, MIN(Price)
                    FROM {self.table.table_name}
                    WHERE Customer = "{customer}"''')


class ShowOneSalesmanMaxSumSales(Show):
    def show(self):

        self.conn.commit()
        self.cursor.execute(f'''SELECT Salesman, SUM(Price) AS SP
                                FROM {self.table.table_name}
                                GROUP BY Salesman
                                ORDER BY SP DESC
                                ''')

        for string in self.cursor.fetchall():
            print(f'\nПродавец с максимальной суммой продаж по всем сделкам - {string[0]} (Сумма: {string[1]})')
            return

class ShowOneSalesmanMinSumSales(Show):
    def show(self):
        self.conn.commit()
        self.cursor.execute(f'''SELECT Salesman, SUM(Price) AS SP
                                FROM {self.table.table_name}
                                GROUP BY Salesman
                                ORDER BY SP
                                ''')

        for string in self.cursor.fetchall():
            print(f'\nПродавец с минимальной суммой продаж по всем сделкам - {string[0]} (Сумма: {string[1]})')
            return

class ShowOneCustomerMaxSumSales(Show):
    def show(self):

        self.conn.commit()
        self.cursor.execute(f'''SELECT Customer, SUM(Price) AS SP
                                FROM {self.table.table_name}
                                GROUP BY Customer
                                ORDER BY SP DESC
                                ''')

        for string in self.cursor.fetchall():
            print(f'\nПокупатель с максимальной суммой покупок по всем сделкам - {string[0]} (Сумма: {string[1]})')
            return

class ShowOneCustomerMinSumSales(Show):
    def show(self):

        self.conn.commit()
        self.cursor.execute(f'''SELECT Customer, SUM(Price) AS SP
                                FROM {self.table.table_name}
                                GROUP BY Customer
                                ORDER BY SP
                                ''')

        for string in self.cursor.fetchall():
            print(f'\nПокупатель с минимальной суммой покупок по всем сделкам - {string[0]} (Сумма: {string[1]})')
            return


class ShowAvgSumSalesOneSalesman(Show):

    def show(self, salesman):
        self.conn.commit()
        self.cursor.execute(f'''SELECT Salesman, AVG(Price)
                        FROM {self.table.table_name}
                        WHERE Salesman = "{salesman}"''')
        for string in self.cursor.fetchall():
            print(f'\nСредняя сумма покупки для продавца {string[0]} - {string[1]} рублей.')


class ShowAvgSumSalesOneCustomer(Show):

    def show(self, customer):
        self.conn.commit()
        self.cursor.execute(f'''SELECT Customer, AVG(Price)
                        FROM {self.table.table_name}
                        WHERE Customer = "{customer}"''')
        for string in self.cursor.fetchall():
            print(f'\nСредняя сумма покупки для покупателя {string[0]} - {string[1]} рублей.')


class UpdateData(Show):
    def update(self, salesman, new_salesman, customer, new_customer, item, new_item, price):
        self.conn.commit()
        self.cursor.execute(f"""UPDATE {self.table.table_name}
                            SET Salesman = '{new_salesman}',
                            Customer = '{new_customer}',
                            Item = '{new_item}',
                            Price = {price}
                            WHERE Salesman = '{salesman}' AND
                            Customer = '{customer}' AND
                            Item = '{item}'""")

        self.cursor.execute(f'''SELECT * FROM {self.table.table_name}''')


class AddData(Show):
    def add(self, new_salesman, new_customer, new_item, price):
        self.conn.commit()
        self.cursor.execute(f"""INSERT INTO {self.table.table_name}
                            VALUES (
                            '{new_salesman}', '{new_customer}', '{new_item}', '{price}')""")

        self.cursor.execute(f'''SELECT * FROM {self.table.table_name}''')


class DeleteData(Show):
    def delete(self, salesman, customer, item, price):
        self.conn.commit()
        self.cursor.execute(f"""DELETE FROM {self.table.table_name}
                            WHERE Salesman = '{salesman}' AND
                            Customer = '{customer}' AND
                            Item = '{item}' AND
                            Price = {price}""")

        self.cursor.execute(f'''SELECT * FROM {self.table.table_name}''')
