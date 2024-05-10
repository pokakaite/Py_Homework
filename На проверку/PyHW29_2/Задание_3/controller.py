from model import *
from view import *

if __name__ == '__main__':
    def show_info():
        anna = AnnaKarenina()
        print(anna.book_info())


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