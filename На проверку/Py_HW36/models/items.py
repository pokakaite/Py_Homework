from abc import abstractmethod


class Item:
    @abstractmethod
    def get_item(self):
        pass

    @abstractmethod
    def get_price(self):
        pass


class Lamp:
    def __init__(self):
        self.name = 'Галогенная лампа'
        self.price = 250

    def get_item(self):
        return self.name

    def get_price(self):
        return self.price


class Xenon:
    def __init__(self):
        self.name = 'Ксеноновая лампа'
        self.price = 400

    def get_item(self):
        return self.name

    def get_price(self):
        return self.price


class Headlight:
    def __init__(self):
        self.name = 'Фара'
        self.price = 1500

    def get_item(self):
        return self.name

    def get_price(self):
        return self.price


class TableItems:
    def __init__(self):
        self.table_name = 'Items'
        self.column_name = 'Name'
        self.column_price = 'Price'
        self.data_type_text = 'text'
        self.data_type_integer = 'money'


    def create_table(self, cursor):
        cursor.execute(f"""
                    CREATE table {self.table_name} (
                    {self.column_name} {self.data_type_text},
                    {self.column_price} {self.data_type_integer}
                    )
                    """)

    def insert_into(self, conn, cursor, item):
        conn.commit()
        cursor.execute(f"""INSERT INTO {self.table_name} values ('{item.name}', '{item.price}')""")

    def select_all(self, conn, cursor):
        conn.commit()
        cursor.execute(f"""SELECT * FROM {self.table_name}""")