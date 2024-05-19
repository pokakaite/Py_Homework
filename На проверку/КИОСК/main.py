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

hot_dog = StandartHotDog(bun, ketchup, sausage)
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

price = hot_dog.price

cash_pay_item = CashPayItem(price)
card_pay_item = CardPayItem(price)

show_hot_dog_items = ShowHotDogItems()
greeting = Greeting()
show_ingredients = ShowIngredients()
standart_or_handmade = StandartOrHandMade()
standart_hot_dogs = [hot_dog, vegan_hot_dog, spicy_hot_dog]
get_chosen_hot_dog = ChosenHotDog()
add_ingredients = AddIngredient()

greeting.set_choice()
if greeting.get_choice() == 1:
    show_hot_dog_items.show(standart_hot_dog_item, vegan_hot_dog_item, spicy_hot_dog_item)
    standart_or_handmade.set_choice()
    # print(get_chosen_hot_dog.get_chosen_hot_dog(standart_or_handmade.get_choice(), standart_hot_dogs)
    add_ingredients.set_choice()
    if add_ingredients.get_choice() == 1:
        show_ingredients.show(ketchup, mustard, jalapeno, onion, pickles)
    else:
        pass
else:
    show_ingredients.show(ketchup, mustard, jalapeno, onion, pickles)
