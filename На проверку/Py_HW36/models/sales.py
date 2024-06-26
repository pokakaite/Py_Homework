class Table_Sales:
    def __init__(self):
        self.table_name = 'Sales'
        self.column_salesman = 'Salesman'
        self.column_customer = 'Customer'
        self.column_item = 'Item'
        self.column_price = 'Price'
        self.data_type_text = 'text'
        self.data_type_money = 'money'


    def create_table(self, cursor):
        cursor.execute(f"""
                    CREATE table {self.table_name} (
                    {self.column_salesman} {self.data_type_text},
                    {self.column_customer} {self.data_type_text},
                    {self.column_item} {self.data_type_text},
                    {self.column_price} {self.data_type_money}
                    )
                    """)

    def insert_into(self, conn, cursor, salesman, customer, item):
        conn.commit()
        cursor.execute(f"""INSERT INTO {self.table_name} VALUES ('{salesman.name} {salesman.surname}',
        '{customer.name} {customer.surname}', '{item.name}', '{item.price}')""")

    def show_all(self, conn, cursor):
        conn.commit()
        cursor.execute(f"""SELECT * FROM {self.table_name}""")

        print('-' * 105)
        print(
            f'| {'Id':^4} | {self.column_salesman:^25} | {self.column_customer:^25} | {self.column_item:^25} | {self.column_price:^10} |')
        print('-' * 105)

        for count, string in enumerate(cursor.fetchall(), start=1):
            print(f'| {count:^4} | {string[0]:^25} | {string[1]:^25} | {string[2]:^25} | {string[3]:^10} |')
            print('-' * 105)