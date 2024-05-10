from model import *
from view import *

if __name__ == '__main__':
    def show_info():
        # BooksCache.load()
        #
        # anna = BooksCache.get_book("1")
        # mam = BooksCache.get_book("2")
        # print(f'''\nКниги библиотеки:
        # {anna.get_id()}. {anna.get_name()}
        # {mam.get_id()}. {mam.get_name()}
        # ''')

        librarian = Librarian()
        print(f'''Информация о библиотекаре:
        ФИО - {librarian.__str__()}
        Заработная плата - {librarian.get_salary()} рублей.
        ''')

        reader = Reader()
        print(f'''Информация о читателе:
        ФИО - {reader.__str__()}
        Возраст - {reader.get_age()}
        ''')

    show_info()