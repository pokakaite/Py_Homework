from abc import abstractmethod


class Salesmen:
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_surname(self):
        pass


class Salesman_1:
    def __init__(self):
        self.name = 'Екатерина'
        self.surname = 'Данилова'

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname


class Salesman_2:
    def __init__(self):
        self.name = 'Татьяна'
        self.surname = 'Данилова'

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname


class Salesman_3:
    def __init__(self):
        self.name = 'Ирина'
        self.surname = 'Данилова'

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname


class Table_Salesmen:
    def __init__(self):
        self.table_name = 'Salesmen'
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

    def insert_into(self, conn, cursor, salesman):
        conn.commit()
        cursor.execute(f"""INSERT INTO {self.table_name} values ('{salesman.name}', '{salesman.surname}')""")

    def select_all(self, conn, cursor):
        conn.commit()
        cursor.execute(f"""SELECT * FROM {self.table_name}""")
