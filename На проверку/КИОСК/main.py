from models import *

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

standart_hot_dog_item = StandartHotDog_Item(hot_dog)
vegan_hot_dog_item = StandartHotDog_Item(vegan_hot_dog)
spicy_hot_dog_item = StandartHotDog_Item(spicy_hot_dog)
handmade_hot_dog_item = HandMade_HotDog_Item(handmade_hot_dog)

price = hot_dog.price

cash_pay_item = CashPayItem(price)
card_pay_item = CardPayItem(price)

menu = Menu()
menu.greeting()
show_ingredients = ShowIngredients()
if menu.get_choice() == 1:
    menu.show(standart_hot_dog_item, vegan_hot_dog_item, spicy_hot_dog_item)
else:
    show_ingredients.show(ketchup, mustard, jalapeno, onion, pickles)