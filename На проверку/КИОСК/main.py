from models import *

bun = BunIngredient()
ketchup = KetchupIngredient()
sausage = SausageIngredient()

hot_dog = StandartHotDog(bun, ketchup, sausage)
handmade_hot_dog = HandMadeHotDog(bun, sausage)

calc = Calc()
hot_dog.price = calc.calculate(hot_dog.ingredients)
handmade_hot_dog.price = calc.calculate(handmade_hot_dog.ingredients)

standart_hot_dog_item = StandartHotDog_Item(hot_dog)
handmade_hot_dog_item = HandMade_HotDog_Item(handmade_hot_dog)

cash_pay_item = CashPayItem(hot_dog.price)
card_pay_item = CardPayItem(hot_dog.price)

menu = Menu()
menu.show(standart_hot_dog_item, handmade_hot_dog_item)