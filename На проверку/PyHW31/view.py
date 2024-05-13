from model import *
import copy


class Recipes:
    recipes = []

    def __init__(self, hot_dog):
        self.hot_dog = hot_dog

    def add_recipe(self):
        Recipes.recipes.append(self.hot_dog)

    def get_recipes(self):
        return Recipes.recipes


class ShowNames(Recipes):
    def __init__(self):
        super().__init__(self)

    @staticmethod
    def show_names():
        count = 0
        for recipe in Recipes.recipes:
            count += 1
            for n, name in recipe.items():
                if n == 'Название':
                    print(f'{count} - {name}')


class ShowRecipes(Recipes):
    def __init__(self):
        super().__init__(self)

    @staticmethod
    def show():
        count = 0
        for recipe in Recipes.recipes:
            count += 1
            print(f'\nРецепт №{count}:')
            for ingredient, name in recipe.items():
                print(f'\t{ingredient} - {name}')


class ShowIngredients:
    def __init__(self, list_of_ingredients):
        self.list = list_of_ingredients
    def show(self):
        count = 0
        for ingredient in self.list:
            count += 1
            print(f'{count} - {ingredient}')


##menu


standart_name = Standart()
mexican_name = Mexican()
vegan_name = Vegan()

wheat = Wheat()
rye = Rye()

milky_sausage = Milky()
vegan_sausage = Vegan_Sausage()

mayonaise = Mayo()
ketchup = Ketchup()
mustard = Mustard()

onion = Onion()
jalapeno = Jalapeno()
pickles = Pickles()

def make_recipes():
    recipe1 = HotDog(standart_name.get_name(), wheat.get_name(), milky_sausage.get_name(),
                     ketchup.get_name(), onion.get_name())
    standart = Recipes(recipe1.get_hot_dog())
    standart.add_recipe()

    recipe2 = HotDog(mexican_name.get_name(), wheat.get_name(), milky_sausage.get_name(),
                     mustard.get_name(), jalapeno.get_name())
    mexican = Recipes(recipe2.get_hot_dog())
    mexican.add_recipe()

    recipe3 = HotDog(vegan_name.get_name(), rye.get_name(), vegan_sausage.get_name(),
                     ketchup.get_name(), pickles.get_name())
    vegan = Recipes(recipe3.get_hot_dog())
    vegan.add_recipe()
make_recipes()

def show_names():
    ShowNames.show_names()

def show_recipes():
    ShowRecipes.show()

def adding_to_lists():
    standart_name.add_to_names()
    mexican_name.add_to_names()
    vegan_name.add_to_names()
    wheat.add_to_buns()
    rye.add_to_buns()
    onion.add_to_toppings()
    jalapeno.add_to_toppings()
    pickles.add_to_toppings()
    milky_sausage.add_to_sausages()
    vegan_sausage.add_to_sausages()

# def show_ingredients():
#     list_names = RecipeName.names
#     list_buns = Bun.buns


def menu():
    print(f'\nДобро пожаловать в киоск. Я знаю, вы хотите попробовать наши знаменитые хот-доги.\n'
          f'Вы можете выбрать хот-дог из меню или создать свой.\n'
          f'Наши хот-доги:\n')
    show_names()
    show_recipes()

    choice = int(input('''\nВыберите, что хотите сделать.
    1 - Выбрать хот-дог из меню,
    2 - Создать свой.\n'''))

    if choice == 2:
        adding_to_lists()

menu()


