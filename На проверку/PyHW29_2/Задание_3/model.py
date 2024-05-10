from abc import abstractmethod
import copy


class Book:
    def __init__(self):
        self.name = None
        self.year = None
        self.author = None
        self.id = None

    @abstractmethod
    def book(self):
        pass

    # def get_name(self):
    #     return self.name
    #
    # def get_id(self):
    #     return self.id
    #
    # def set_id(self, sid):
    #     self.id = sid
    #
    # def clone(self):
    #     return copy.copy(self)


class AnnaKarenina(Book):
    def __init__(self):
        super().__init__()
        self.name = 'Анна Каренина'
        self.year = 1877
        self.author = 'Лев Николаевич Толстой'

    def get_name(self):
        return self.name

    def book(self):
        print('')


class MasterAndMargarita(Book):
    def __init__(self):
        super().__init__()
        self.name = 'Мастер и Маргарита'
        self.year = 1940
        self.author = 'Михаил Афанасьевич Булгаков'

    def book(self):
        print('')

class NewBook(Book):
    def __init__(self):
        super().__init__()
        self.name = None
        self.year = None
        self.author = None

    def book(self):
        print('')



#######################################
#######################################


class Reader:
    def __init__(self):
        self.name = 'Данилова Екатерина Александровна'
        self.age = 21

    def __str__(self):
        return self.name

    def get_age(self):
        return self.age


class Librarian:
    def __init__(self):
        self.name = 'Иванова Виктория Анатольевна'
        self.salary = 20000

    def __str__(self):
        return self.name

    def get_salary(self):
        return self.salary
