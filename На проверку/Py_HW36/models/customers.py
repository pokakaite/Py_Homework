from abc import abstractmethod


class Customers:
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_surname(self):
        pass


class Customer1:
    def __init__(self):
        self.name = 'Иван'
        self.surname = 'Иванов'

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname


class Customer2:
    def __init__(self):
        self.name = 'Александр'
        self.surname = 'Александров'

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname


class Customer3:
    def __init__(self):
        self.name = 'Василий'
        self.surname = 'Васильев'

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname


class TableCustomers:
    def __init__(self):
        self.table_name = 'Customers'
        self.column_name = 'Name'
        self.column_surname = 'Surname'
        self.data_type_text = 'text'

    def create_table(self, cursor):
        cursor.execute(f"""
                    CREATE table {self.table_name} (
                    {self.column_name} {self.data_type_text},
                    {self.column_surname} {self.data_type_text}
                    )
                    """)

    def insert_into(self, conn, cursor, customer):
        conn.commit()
        cursor.execute(f"""INSERT INTO {self.table_name} values ('{customer.name}', '{customer.surname}')""")

    def select_all(self, conn, cursor):
        conn.commit()
        cursor.execute(f"""SELECT * FROM {self.table_name}""")