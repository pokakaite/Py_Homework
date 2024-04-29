from model import *

def showAllShoes():
    print(f'''\nИнформация об обуви:\n''')
    for shoe in shoes:
        for key, value in shoe.items():
            print(f'{key} - {value}')
        print('\n')

def startView():
    print("Хотите увидеть всю обувь?")

def endView():
    print('Пока!')