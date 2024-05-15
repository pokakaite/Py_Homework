import recipe_names, buns, sausages, sauses, toppings


class HotDog:
    def __init__(self):
        self.name = None
        self.price = None
        self.recipe = None
        self.id = None


class HotDogPrice(HotDog):
    def __init__(self):
        super().__init__()

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price


class HotDogName(HotDog):
    def __init__(self):
        super().__init__()

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


class HotDogId(HotDog):
    def __init__(self):
        super().__init__()

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id


class HotDogRecipe(HotDog):
    def __init__(self):
        super().__init__()

    def set_recipe(self):
        self.recipe = []

    def add_to_recipe(self, ingredient):
        self.recipe.append(ingredient)

    def get_recipe(self):
        return self.recipe

    def show_recipe(self):
        for i in self.recipe:
            print(i)


class AllHotDogs:
    def __init__(self):
        self.list_hot_dogs = None

    def set_list(self):
        self.list_hot_dogs = []

    def add_to_list(self, hot_dog):
        self.list_hot_dogs.append(hot_dog)

    def get_list(self):
        return self.list_hot_dogs


class ShowHotDog:
    def __init__(self, name, price, recipe, id):
        self.name = name
        self.price = price
        self.recipe = recipe
        self.id = id

    def show_id(self):
        print(f'Рецепт №{self.id}\n')

    def show_name(self):
        print(f'Название - {self.name}\n')

    def show_recipe(self):
        for i in self.recipe:
            print(i)
        print('\n')

    def show_price(self):
        print(f'Цена - {self.price}\n')


standart_recipe = HotDogRecipe()
mexican_recipe = HotDogRecipe()
vegan_recipe = HotDogRecipe()

standart_recipe.set_recipe()
standart_recipe.add_to_recipe(buns.wheat_bun.get_name())
standart_recipe.add_to_recipe(sausages.milky.get_name())
standart_recipe.add_to_recipe(sauses.ketchup.get_name())
standart_recipe.add_to_recipe(sauses.mayonaise.get_name())

mexican_recipe.set_recipe()
mexican_recipe.add_to_recipe(buns.wheat_bun.get_name())
mexican_recipe.add_to_recipe(sausages.chicken.get_name())
mexican_recipe.add_to_recipe(sauses.salsa.get_name())
mexican_recipe.add_to_recipe(toppings.jalapeno.get_name())
mexican_recipe.add_to_recipe(toppings.cheese.get_name())
mexican_recipe.add_to_recipe(toppings.onion.get_name())

vegan_recipe.set_recipe()
vegan_recipe.add_to_recipe(buns.rye_bun.get_name())
vegan_recipe.add_to_recipe(sausages.soy.get_name())
vegan_recipe.add_to_recipe(sauses.ketchup.get_name())
vegan_recipe.add_to_recipe(sauses.mustard.get_name())
vegan_recipe.add_to_recipe(toppings.onion.get_name())
vegan_recipe.add_to_recipe(toppings.pickles.get_name())

standart_price = HotDogPrice()
standart_price.set_price(150)
mexican_price = HotDogPrice()
mexican_price.set_price(180)
vegan_price = HotDogPrice()
vegan_price.set_price(200)

standart_name = HotDogName()
standart_name.set_name(recipe_names.standart.get_name())
mexican_name = HotDogName()
mexican_name.set_name(recipe_names.mexican.get_name())
vegan_name = HotDogName()
vegan_name.set_name(recipe_names.vegan.get_name())

standart_id = HotDogId()
standart_id.set_id(1)
mexican_id = HotDogId()
mexican_id.set_id(2)
vegan_id = HotDogId()
vegan_id.set_id(3)

recipes_list = AllHotDogs()
recipes_list.set_list()
recipes_list.add_to_list(standart_recipe.get_recipe())
recipes_list.add_to_list(mexican_recipe.get_recipe())
recipes_list.add_to_list(vegan_recipe.get_recipe())

standart = HotDog()
