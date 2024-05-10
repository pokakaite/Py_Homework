import getpass

from model import *
import time
import copy


class AddToCollection:
    collection = []

    def __init__(self, book):
        self.book = book

    def add_book(self):
        AddToCollection.collection.append(self.book)

    def get_collection(self):
        return AddToCollection.collection


class ShowCollection(AddToCollection):
    def __init__(self):
        super().__init__(self)

    def show(self):
        count = 0
        for book in AddToCollection.collection:
            count += 1
            print(f'\t{count}. {book}')


class AddNewBook:
    def __init__(self):
        self.name = None

    def add_name(self):
        self.name = input('Введите название книги - ')
        return self.name

    def get_name(self):
        return self.name


class DeleteBook():
    def __init__(self, book, collection):
        self.book = book
        self.collection = collection

    def delete_book(self):
        self.collection.pop(self.book - 1)


class ChangeBook(AddToCollection):
    def __init__(self, old_book):
        super().__init__(self)
        self.old_book = old_book
        self.new_book = None

    def get_new_book(self):
        self.new_book = input('Введите название новой книги - ')

    def change_book(self):
        AddToCollection.collection.pop(self.old_book - 1)
        AddToCollection.collection.append(self.new_book)


class Save:
    def __init__(self, info):
        self.file_name = 'save.txt'
        self.info = info

    def to_save(self):
        with open(self.file_name, 'w+', encoding='UTF-8') as f:
            f.write(str(self.info))
            f.write('\n')


class Load:
    def __init__(self):
        self.file_name = 'save.txt'
        self.info = None

    def to_load(self):
        with open(self.file_name, 'r+', encoding='UTF-8') as f:
            self.info = f.read()
            print(self.info)
            return self.info


class Log:
    def __init__(self, info):
        self.name = 'log_file.txt'
        self.time = time.time()
        self.user = getpass.getuser()
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
            f.write('Коллекция книг: ')
            f.write(str(self.info))
            f.write('\n\n')


class Search:
    def __init__(self, collection):
        self.book = None
        self.collection = collection

    def get_name(self):
        self.book = input('Введите название книги, которую хотите найти - ')
        return self.book

    def to_search(self):
        if self.book in self.collection:
            for i in range(len(self.collection)):
                if self.book == self.collection[i]:
                    print(f'Такая книга есть в библиотеке и находится под номером - {i + 1}')
        else:
            print(f'Такой книги нет в библиотеке.')


def books():
    anna = AnnaKarenina()
    book_1 = AddToCollection(anna.get_name())
    book_1.add_book()

    mam = MasterAndMargarita()
    book_2 = AddToCollection(mam.get_name())
    book_2.add_book()

    oblomov = copy.deepcopy(anna)
    oblomov.name = 'Обломов'
    book_3 = AddToCollection(oblomov.get_name())
    book_3.add_book()

    fathers_and_sons = copy.deepcopy(anna)
    fathers_and_sons.name = 'Отцы и дети'
    book_4 = AddToCollection(fathers_and_sons.get_name())
    book_4.add_book()


def show_collection():
    print('\nКниги библиотеки:')
    show = ShowCollection()
    show.show()


def delete_book(index):
    delete = DeleteBook(index, AddToCollection.collection)
    delete.delete_book()


def change_book(index):
    change = ChangeBook(index)
    change.get_new_book()
    change.change_book()


def to_save():
    save = Save(AddToCollection.collection)
    save.to_save()


def to_load():
    load = Load()
    load.to_load()


def to_log():
    log = Log(AddToCollection.collection)
    log.log_file()


def to_search():
    search = Search(AddToCollection.collection)
    search.get_name()
    search.to_search()

books()

def menu():
    show_collection()
    choice = int(input('''\nЧто вы хотите сделать?
    1 - Удалить книгу,
    2 - Изменить книгу,
    3 - Сохранить информацию о книгах в файл,
    4 - Загрузить информацию из файла,
    5 - Найти книгу в библиотеке,
    6 - Выйти
    '''))

    if choice == 1:
        which = int(input('Введите номер книги, которую хотите удалить - '))
        delete_book(which)
        to_log()

    if choice == 2:
        which = int(input('Введите номер книги, которую хотите изменить - '))
        change_book(which)
        to_log()

    if choice == 3:
        to_save()
        to_log()

    if choice == 4:
        to_load()
        to_log()

    if choice == 5:
        to_search()
        to_log()

    if choice == 6:
        pass

    return menu()

