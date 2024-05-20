from models import *

# ингредиенты
bun = BunIngredient()
ketchup = KetchupIngredient()
mustard = MustardIngredient()
mayonaise = MayonaiseIngredient()
sausage = SausageIngredient()
vegan_sausage = VeganSausageIngredient()
jalapeno = JalapenoIngredient()
onion = OnionIngredient()
pickles = PickleIngredient()
# ингредиенты


# добавление ингредиентов в хот-дог
hot_dog = StandartHotDog()
hot_dog.ingredients(bun, ketchup, mayonaise, sausage)
vegan_hot_dog = VeganHotDog()
vegan_hot_dog.ingredients(bun, ketchup, vegan_sausage)
spicy_hot_dog = SpicyHotDog()
spicy_hot_dog.ingredients(bun, mustard, sausage, jalapeno)
handmade_hot_dog = HandMadeHotDog(bun, sausage)
# добавление ингредиентов в хот-дог


# списки хот-догов, ингредиентов
standart_hot_dogs = [hot_dog, vegan_hot_dog, spicy_hot_dog]
ingredients = [ketchup, mayonaise, mustard, jalapeno, onion, pickles]
# списки хот-догов, ингредиентов


# подсчёт стоимости хот-догов
calc = Calc()
hot_dog.price = calc.calculate(hot_dog.ingredients)
vegan_hot_dog.price = calc.calculate(vegan_hot_dog.ingredients)
spicy_hot_dog.price = calc.calculate(spicy_hot_dog.ingredients)
handmade_hot_dog.price = calc.calculate(handmade_hot_dog.ingredients)
# подсчёт стоимости хот-догов


standart_hot_dog_item = StandartHotDogItem(hot_dog)
vegan_hot_dog_item = StandartHotDogItem(vegan_hot_dog)
spicy_hot_dog_item = StandartHotDogItem(spicy_hot_dog)
handmade_hot_dog_item = HandMadeHotDogItem(handmade_hot_dog)

# функции. взаимодействие с клиентом
greeting = Greeting()
show_hot_dog_items = ShowHotDogItems()
show_ingredients = ShowIngredients()
choose_hot_dog = ChooseHotDog()
get_chosen_hot_dog = ChosenHotDog()
ask_for_topping = AskForTopping()
choose_topping = ChooseTopping()
continue_toppings = ContinueToppings()
continue_hot_dogs = ContinueHotDogs()
order = Order()
pay = Pay()
file = AddToFile()
# функции. взаимодействие с клиентом

