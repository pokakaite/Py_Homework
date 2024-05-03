from model import *

def showTheRecipe(startView):
    print('\n')
    for key, value in Recipe.recipes[startView - 1].items():
        print(f'\t\t{key} - {value}')
    print('\n')

def startView():
    count = 0
    for recipe in Recipe.recipes:
        count += 1
        for name, value in recipe.items():
            if name == 'Название рецепта':
                print(f'{count}. {value}')
    print(f'Какой рецепт хотите посмотреть?')
    choice = int(input('Введите номер рецепта (Если хотите выйти, введите любую другую цифру) - '))
    return choice


def endView():
    print('Пока!')