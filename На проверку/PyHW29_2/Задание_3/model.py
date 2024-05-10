class Book:
    def __init__(self):
        self.name = None

    def get_name(self):
        return self.name


class AnnaKarenina(Book):
    def __init__(self):
        super().__init__()
        self.name = 'Анна Каренина'


class MasterAndMargarita(Book):
    def __init__(self):
        super().__init__()
        self.name = 'Мастер и Маргарита'


class Reader:
    def __init__(self):
        self.name = 'Данилова Екатерина Александровна'


class Librarian:
    def __init__(self):
        self.name = 'Иванова Виктория Анатольевна'
