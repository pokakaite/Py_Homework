class Book:
    def __init__(self):
        self.name = None
        self.year = None
        self.author = None


class AnnaKarenina(Book):
    def __init__(self):
        super().__init__()
        self.name = 'Анна Каренина'
        self.year = 1877
        self.author = 'Лев Николаевич Толстой'


class MasterAndMargarita(Book):
    def __init__(self):
        super().__init__()
        self.name = 'Мастер и Маргарита'
        self.year = 1940
        self.author = 'Михаил Афанасьевич Булгаков'


class NewBook(Book):
    def __init__(self):
        super().__init__()
        self.name = None
        self.year = None
        self.author = None


class Reader:
    def __init__(self):
        self.name = 'Данилова Екатерина Александровна'
        self.age = 21


class Librarian:
    def __init__(self):
        self.name = 'Иванова Виктория Анатольевна'
        self.salary = 20000
