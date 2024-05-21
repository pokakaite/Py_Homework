from models import *

sugar = Sugar()
choco_glaze = ChocolateGlaze()
sprinkles = Sprinkles()
# топпинги и их цена


basic_donut = BasicDonat()
choco_donut = ChocoDonut()
choco_donut.add_topping(choco_glaze)
hand_made_donut = HandMadeDonut()
# пончики и их составы


donut_item = DonutItem(basic_donut)
choco_donut_item = DonutItem(choco_donut)
hand_made_donut_item = HandMadeDonutItem(hand_made_donut)
# пончики как элементы ассортимента (для вывода в меню)


donuts_list = ListItems()
donuts_list.add_to_list(donut_item)
donuts_list.add_to_list(choco_donut_item)
donuts_list.add_to_list(hand_made_donut_item)
# список пончиков (для вывода в меню)


toppings_list = ListItems()
toppings_list.add_to_list(sugar)
toppings_list.add_to_list(choco_glaze)
toppings_list.add_to_list(sprinkles)

# список топпингов (для вывода в меню)


greeting = Greeting()
choice_making = ChoiceMaking()
choice_making2 = ChoiceMaking2()

########################
greeting.show()  # приветствие
ShowItems.set_list(donuts_list.get_list())  # создаём список пончиков-элементов
ShowItems.show()  # вывод элементов списка в меню
WhichDonut.set_choice()  # приложение спрашивает, какой пончик хочет покупатель
choice_making.make_choice(
    WhichDonut.get_choice(), IfToppings.set_choice, IfToppings.set_choice, IfToppings.set_choice)
# приложение спрашивает, не хочет ли покупатель добавить топпинги
ShowItems().set_list(toppings_list.get_list())  # создаём список топпингов-элементов
choice_making.make_choice(
    IfToppings.get_choice(), ShowItems.show)
# приложение показывает список топпингов

WhichTopping.set_choice()

choice_making2.make_choice(WhichDonut.get_choice(),
                           toppings_list.get_list()[WhichTopping.get_choice() - 1],
                           basic_donut.add_topping,
                           choco_donut.add_topping,
                           hand_made_donut.add_topping) # добавляем топпинг в пончик

choice_making.make_choice(WhichDonut.get_choice(),
                          basic_donut.show,
                          choco_donut.show,
                          hand_made_donut.show) # показываем информацию о пончике

choice_making.make_choice(WhichDonut.get_choice(),
                          basic_donut.show_toppings,
                          choco_donut.show_toppings,
                          hand_made_donut.show_toppings) # показываем топпинги пончика