from model import *

class BooksCache:
    cache = {}

    @staticmethod
    def load():
        anna = AnnaKarenina()
        anna.set_id('1')
        BooksCache.cache[anna.get_id()] = anna

        mam = MasterAndMargarita()
        mam.set_id('2')
        BooksCache.cache[mam.get_id()] = mam

    @staticmethod
    def get_book(sid):
        book = BooksCache.cache.get(sid, None)
        return book.clone()


class Input:
    def __init__(self):
        self.input = None

    def to_input(self):
        self.input = input({})


class Delete:
    def __init__(self):
        self.info = None

    def to_delete(self):
        pass


class Change:
    def __init__(self):
        self.info = None

    def to_change(self):
        self.info = input('Введите новую информацию:\n')
        return self.info


class Save:
    def __init__(self):
        self.file_name = None
        self.info = None

    def to_save(self):
        with open(self.file_name, 'a+', encoding='UTF-8') as f:
            f.write(self.info)
            f.write('\n')


class Load:
    def __init__(self):
        self.file_name = None
        self.info = None

    def to_load(self):
        with open(self.file_name, 'r+', encoding='UTF-8') as f:
            self.info = f.read()
            return self.info


class Log:
    def __init__(self, name, time, user, info):
        self.name = name
        self.time = time
        self.user = user
        self.info = info

    def __str__(self):
        return self.name

    def log_file(self):
        with open(self.name, 'a+', encoding='UTF-8') as f:
            f.write('Время получения данных - ')
            f.write(str(self.time))
            f.write(', Имя пользователя - ')
            f.write(str(self.user))
            f.write('\n')
            f.write('Информация: ')
            f.write(str(self.info))
            f.write('\n\n')


class Search:
    def __init__(self):
        self.info = None

    def to_search(self):
        pass


class Show:
    def __init__(self):
        self.info = None

    def to_show(self):
        print(self.info)


def menu():

    print('\n\tКниги библиотеки:\n')
    BooksCache.load()

    anna = BooksCache.get_book("1")
    mam = BooksCache.get_book("2")
    print(f'{anna.get_id()}. {anna.get_name()}')
    print(f'{mam.get_id()}. {mam.get_name()}')
    print()
    print('\tИнформация о библиотекаре:\n')
    librarian = Librarian()
    print(f'ФИО - {librarian.__str__()}')
    print(f'Заработная плата - {librarian.get_salary()} рублей.')
    print()
    print('\tИнформация о читателе:\n')
    reader = Reader()
    print(f'ФИО - {reader.__str__()}')
    print(f'Возраст - {reader.get_age()}')

menu()
