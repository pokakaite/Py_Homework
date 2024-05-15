import recipe_names, buns, sausages, sauses, toppings


class BuildHotDog:
    def __init__(self):
        self.hot_dog = None

    def set_hot_dog(self):
        self.hot_dog = []

    def add_to_hot_dog(self, ingredient):
        self.hot_dog.append(ingredient)

    def get_hot_dog(self):
        return self.hot_dog


class HotDogPrice:
    def __init__(self):
        self.price = None

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price


class HotDogName:
    def __init__(self):
        self.name = None

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


class HotDogId:
    def __init__(self):
        self.id = None

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id


class AllHotDogs:
    def __init__(self):
        self.list_hot_dogs = None

    def set_list(self):
        self.list_hot_dogs = []

    def add_to_list(self, hot_dog):
        self.list_hot_dogs.append(hot_dog)

    def get_list(self):
        return self.list_hot_dogs


standart = BuildHotDog()
mexican = BuildHotDog()
vegan = BuildHotDog()

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


def standart_recipe():
    standart.set_hot_dog()
    standart.add_to_hot_dog(buns.wheat_bun.get_name())
    standart.add_to_hot_dog(sausages.milky.get_name())
    standart.add_to_hot_dog(sauses.ketchup.get_name())
    standart.add_to_hot_dog(sauses.mayonaise.get_name())
    return standart.get_hot_dog()


def mexican_recipe():
    mexican.set_hot_dog()
    mexican.add_to_hot_dog(buns.wheat_bun.get_name())
    mexican.add_to_hot_dog(sausages.chicken.get_name())
    mexican.add_to_hot_dog(sauses.salsa.get_name())
    mexican.add_to_hot_dog(toppings.jalapeno.get_name())
    mexican.add_to_hot_dog(toppings.cheese.get_name())
    mexican.add_to_hot_dog(toppings.onion.get_name())
    return mexican.get_hot_dog()


def vegan_recipe():
    vegan.set_hot_dog()
    vegan.add_to_hot_dog(buns.rye_bun.get_name())
    vegan.add_to_hot_dog(sausages.soy.get_name())
    vegan.add_to_hot_dog(sauses.ketchup.get_name())
    vegan.add_to_hot_dog(sauses.mustard.get_name())
    vegan.add_to_hot_dog(toppings.onion.get_name())
    vegan.add_to_hot_dog(toppings.pickles.get_name())
    return vegan.get_hot_dog()

standart_recipe()
mexican_recipe()
vegan_recipe()

recipes_list = AllHotDogs()
recipes_list.set_list()
recipes_list.add_to_list(standart_recipe())
recipes_list.add_to_list(mexican_recipe())
recipes_list.add_to_list(vegan_recipe())