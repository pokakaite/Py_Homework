from models import *

greeting = Greeting()
choice_making = ChoiceMaking()
choice_making2 = ChoiceMaking2()
order = Order()
calc_order = CalculateOrder()
show_order_summ = ShowOrderSumm()


def menu_order():
    show_order_summ.show(calc_order.get_order_summ())


def lol():
    return


########################
def start():
    greeting.show()  # приветствие

    def donuts():
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

        ShowItems.set_list(donuts_list.get_list())  # создаём список пончиков-элементов
        ShowItems.show()  # вывод элементов списка в меню
        WhichDonut.set_choice()  # приложение спрашивает, какой пончик хочет покупатель
        IfToppings.set_choice()  # приложение спрашивает, не хочет ли покупатель добавить топпинги
        choice_making.make_choice(IfToppings.get_choice(), print, menu_order)

        def add_to_order():
            choice_making2.make_choice(IfDonut.get_choice(),
                                       donuts_list.get_list()[WhichDonut.get_choice() - 1].get_donut(),
                                       order.add_to_order,
                                       order.add_to_order,
                                       order.add_to_order)  # добавляем пончик в заказ
            choice_making2.make_choice(IfDonut.get_choice(),
                                       donuts_list.get_list()[WhichDonut.get_choice() - 1].get_donut_price(),
                                       calc_order.add_to_order_summ,
                                       calc_order.add_to_order_summ,
                                       calc_order.add_to_order_summ)  # добавляем стоимость пончика в заказ
            choice_making.make_choice(IfDonut.get_choice(), donuts, order.show)

        def toppings():
            ShowItems().set_list(toppings_list.get_list())  # создаём список топпингов-элементов
            choice_making.make_choice(IfToppings.get_choice(), ShowItems.show, IfDonut.set_choice)
            # приложение показывает список топпингов или спрашивает, хочет ли клиент еще пончик
            add_to_order()

            choice_making.make_choice(IfDonut.get_choice(), donuts, menu_order)
            choice_making.make_choice(IfDonut.get_choice(), WhichTopping.set_choice, lol)

            choice_making2.make_choice(WhichDonut.get_choice(),
                                       toppings_list.get_list()[WhichTopping.get_choice() - 1],
                                       basic_donut.add_topping,
                                       choco_donut.add_topping,
                                       hand_made_donut.add_topping)  # добавляем топпинг в пончик

            choice_making.make_choice(WhichDonut.get_choice(),
                                      basic_donut.show,
                                      choco_donut.show,
                                      hand_made_donut.show)  # показываем информацию о пончике

            choice_making.make_choice(WhichDonut.get_choice(),
                                      basic_donut.show_toppings,
                                      choco_donut.show_toppings,
                                      hand_made_donut.show_toppings)  # показываем топпинги пончика

            IfToppings.set_choice()
            choice_making.make_choice(IfToppings.get_choice(), toppings, IfDonut.set_choice)
            choice_making.make_choice(IfDonut.get_choice(), donuts, print)

            add_to_order()

        toppings()

    donuts()

    menu_order()


if __name__ == '__main__':
    start()
