from models import *

# присваивание значений. работа приложения.

bun = BunIngredient()
ketchup = KetchupIngredient()
mustard = MustardIngredient()
sausage = SausageIngredient()
vegan_sausage = VeganSausageIngredient()
jalapeno = JalapenoIngredient()
onion = OnionIngredient()
pickles = PickleIngredient()


hot_dog = StandartHotDog()
hot_dog.ingredients(bun, ketchup, sausage)
vegan_hot_dog = VeganHotDog(bun, ketchup, vegan_sausage)
spicy_hot_dog = SpicyHotDog(bun, mustard, sausage, jalapeno)
handmade_hot_dog = HandMadeHotDog(bun, sausage)

calc = Calc()
hot_dog.price = calc.calculate(hot_dog.ingredients)
vegan_hot_dog.price = calc.calculate(vegan_hot_dog.ingredients)
spicy_hot_dog.price = calc.calculate(spicy_hot_dog.ingredients)
handmade_hot_dog.price = calc.calculate(handmade_hot_dog.ingredients)

standart_hot_dog_item = StandartHotDogItem(hot_dog)
vegan_hot_dog_item = StandartHotDogItem(vegan_hot_dog)
spicy_hot_dog_item = StandartHotDogItem(spicy_hot_dog)
handmade_hot_dog_item = HandMadeHotDogItem(handmade_hot_dog)

show_hot_dog_items = ShowHotDogItems()
greeting = Greeting()
show_ingredients = ShowIngredients()
choose_hot_dog = ChooseHotDog()
standart_hot_dogs = [hot_dog, vegan_hot_dog, spicy_hot_dog]
get_chosen_hot_dog = ChosenHotDog()
ask_for_topping = AskForTopping()
choose_topping = ChooseTopping()
ingredients = [ketchup, mustard, jalapeno, onion, pickles]

greeting.set_choice()  # приветствие

if greeting.get_choice() == 1:
    show_hot_dog_items.get_items(standart_hot_dog_item, vegan_hot_dog_item, spicy_hot_dog_item)
    show_ingredients.get_items(ketchup, mustard, jalapeno, onion, pickles)

    choose_between(make_dict(show_hot_dog_items.show,
                             show_ingredients.show), greeting.get_choice())

    choose_hot_dog.set_choice()
    choose_between(make_dict(hot_dog.show, vegan_hot_dog.show, spicy_hot_dog.show), choose_hot_dog.get_choice())

    ask_for_topping.set_choice()
    choose_between(make_dict(show_ingredients.show), ask_for_topping.get_choice())

    choose_topping.set_choice()
    add_topping(standart_hot_dogs, choose_hot_dog.get_choice(), ingredients, choose_topping.get_choice())

if greeting.get_choice() == 2:
    show_hot_dog_items.get_items(standart_hot_dog_item, vegan_hot_dog_item, spicy_hot_dog_item)
    show_ingredients.get_items(ketchup, mustard, jalapeno, onion, pickles)

    choose_between(make_dict(show_hot_dog_items.show,
                             show_ingredients.show), greeting.get_choice())