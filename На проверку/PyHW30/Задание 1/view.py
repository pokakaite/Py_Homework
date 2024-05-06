from model import *

def showAllShoes():
    print(f'''\nИнформация об обуви:\n''')
    count = 0
    for shoe in Shoes.shoes:
        count += 1
        print(f'Обувь {count}:')
        for key, value in shoe.items():
            print(f'\t\t{key} - {value}')
        print('\n')

def startView():
    print("Хотите увидеть всю обувь?")

def endView():
    print('Пока!')