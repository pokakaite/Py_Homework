from models import *
import copy

sales = SalesFile()
calc_income = CalcIncome()
orders_summ = OrdersSumm()
show_order_summ = ShowOrderSumm()
refill = RefillTopping()
choice = Choice()


def order():
    order_list = OrderList()
    calc = Calc()
    calc_order = CalculateOrder()
    check = Check()

    sugar = Sugar()
    choco_glaze = ChocolateGlaze()
    strawberry_glaze = StrawberryGlaze()
    sprinkles = Sprinkles()

    toppings_list = [sugar, choco_glaze, strawberry_glaze, sprinkles]
    topping_amount = ToppingAmount(toppings_list)
    # топпинги и их цена

    basic_donut = BasicDonat()
    basic_donut.add_topping(sugar)
    choco_donut = ChocoDonut()
    choco_donut.add_topping(choco_glaze)
    simpsons_donut = SimpsonsDonut()
    simpsons_donut.add_topping(strawberry_glaze)
    simpsons_donut.add_topping(sprinkles)
    hand_made_donut = HandMadeDonut()
    # пончики и их составы

    basic_donut.price = calc.calculate(basic_donut)
    choco_donut.price = calc.calculate(choco_donut)
    simpsons_donut.price = calc.calculate(simpsons_donut)
    hand_made_donut.price = calc.calculate(hand_made_donut)

    donuts_list = [basic_donut, choco_donut, simpsons_donut, hand_made_donut]
    show_donuts = ShowItems(donuts_list)
    # список пончиков (для вывода в меню)

    toppings_list_items = ListItems()
    toppings_list_items.add_to_list(sugar)
    toppings_list_items.add_to_list(choco_glaze)
    toppings_list_items.add_to_list(strawberry_glaze)
    toppings_list_items.add_to_list(sprinkles)
    show_toppings = ShowItems(toppings_list_items.get_list())
    # список топпингов (для вывода в меню)

    Greeting.show()

    def start():
        show_donuts.show()
        WhichDonut.set_choice()
        donut_copy = copy.deepcopy(donuts_list[WhichDonut.get_choice() - 1])
        order_list.add_to_order(donut_copy)

        def toppings():
            IfToppings.set_choice()
            if IfToppings.get_choice() == 1:
                show_toppings.show()
                WhichTopping.set_choice()
                topping_copy = copy.deepcopy(toppings_list[WhichTopping.get_choice() - 1])
                donut_copy.add_topping(topping_copy)
                toppings_list[WhichTopping.get_choice() - 1].amount -= 1
                topping_amount.show_warning()
                refill.if_refill(toppings_list[WhichTopping.get_choice() - 1])
                refill.refill(toppings_list[WhichTopping.get_choice() - 1], refill.get_choice())
                donut_copy.price = calc.calculate(donut_copy)
                donut_copy.show()
                donut_copy.show_toppings()
                return toppings()

        toppings()
        if IfToppings.get_choice() == 2:
            IfDonut.set_choice()
            if IfDonut.get_choice() == 1:
                return start()
            else:
                order_list.show()
                show_order_summ.show(calc_order.get_order_summ(order_list.get_order()))
                check.add_to_check(order_list.get_order())

                PayChoice.set_choice()
                Wish.show()

    start()

    calc_income.calculate_income(calc_order.get_order_summ(order_list.get_order()))
    calc_income.calculate_revenue(calc_order.get_order_summ(order_list.get_order()))
    sales.add_to_file(check.get_check(), calc_income.income, calc_income.revenue)

    def menu_for_employee():
        IfMoreOrder.set_choice()
        choice.make_choice(IfMoreOrder.get_choice(),
                           order,
                           topping_amount.show,
                           sales.show,
                           print)
        if IfMoreOrder.get_choice() == 4:
            pass
        else:
            return menu_for_employee()

    menu_for_employee()


if __name__ == '__main__':
    order()
