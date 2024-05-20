from models import *

# присваивание значений. работа приложения.

bun = BunIngredient()
ketchup = KetchupIngredient()
mustard = MustardIngredient()
mayonaise = MayonaiseIngredient()
sausage = SausageIngredient()
vegan_sausage = VeganSausageIngredient()
jalapeno = JalapenoIngredient()
onion = OnionIngredient()
pickles = PickleIngredient()


hot_dog = StandartHotDog()
hot_dog.ingredients(bun, ketchup, mayonaise, sausage)
vegan_hot_dog = VeganHotDog()
vegan_hot_dog.ingredients(bun, ketchup, vegan_sausage)
spicy_hot_dog = SpicyHotDog()
spicy_hot_dog.ingredients(bun, mustard, sausage, jalapeno)
handmade_hot_dog = HandMadeHotDog(bun, sausage)

standart_hot_dogs = [hot_dog, vegan_hot_dog, spicy_hot_dog]
ingredients = [ketchup, mayonaise, mustard, jalapeno, onion, pickles]

calc = Calc()
hot_dog.price = calc.calculate(hot_dog.ingredients)
vegan_hot_dog.price = calc.calculate(vegan_hot_dog.ingredients)
spicy_hot_dog.price = calc.calculate(spicy_hot_dog.ingredients)
handmade_hot_dog.price = calc.calculate(handmade_hot_dog.ingredients)

standart_hot_dog_item = StandartHotDogItem(hot_dog)
vegan_hot_dog_item = StandartHotDogItem(vegan_hot_dog)
spicy_hot_dog_item = StandartHotDogItem(spicy_hot_dog)
handmade_hot_dog_item = HandMadeHotDogItem(handmade_hot_dog)

greeting = Greeting()
show_hot_dog_items = ShowHotDogItems()
show_ingredients = ShowIngredients()
show_order_items = ShowOrderItems()

choose_hot_dog = ChooseHotDog()
get_chosen_hot_dog = ChosenHotDog()
ask_for_topping = AskForTopping()
choose_topping = ChooseTopping()
show_order = ShowOrder()
continue_toppings = ContinueToppings()
continue_hot_dogs = ContinueHotDogs()

greeting.set_choice()  # приветствие

if greeting.get_choice() == 1:
    show_hot_dog_items.get_items(standart_hot_dog_item, vegan_hot_dog_item, spicy_hot_dog_item)
    show_ingredients.get_items(ketchup, mayonaise, mustard, jalapeno, onion, pickles)

    def func_hot_dogs():
        choose_between(make_dict(show_hot_dog_items.show,
                                 show_ingredients.show), greeting.get_choice())

        choose_hot_dog.set_choice()
        show_order.show()
        choose_between(make_dict(hot_dog.show, vegan_hot_dog.show, spicy_hot_dog.show), choose_hot_dog.get_choice())
        # show_order_items.get_items(choose_between(make_dict(hot_dog.show, vegan_hot_dog.show, spicy_hot_dog.show),
        #                                           choose_hot_dog.get_choice()))
        # show_order_items.show()

        def func_toppings():
            show_ingredients.show()
            choose_topping.set_choice()
            add_topping(standart_hot_dogs, choose_hot_dog.get_choice(), ingredients, choose_topping.get_choice())

            continue_toppings.set_choice()
            choose_between(make_dict(show_ingredients.show), continue_toppings.get_choice())
            if continue_toppings.get_choice() == 1:
                return func_toppings()
            else:
                continue_hot_dogs.set_choice()
                choose_between(make_dict(func_hot_dogs, None), continue_hot_dogs.get_choice())

        ask_for_topping.set_choice()
        choose_between(make_dict(func_toppings, continue_hot_dogs.set_choice), ask_for_topping.get_choice())

        if continue_hot_dogs.get_choice() == 1:
            func_hot_dogs()



    func_hot_dogs()




if greeting.get_choice() == 2:
    show_hot_dog_items.get_items(standart_hot_dog_item, vegan_hot_dog_item, spicy_hot_dog_item)
    show_ingredients.get_items(ketchup, mustard, mayonaise, jalapeno, onion, pickles)

    choose_between(make_dict(show_hot_dog_items.show,
                             show_ingredients.show), greeting.get_choice())