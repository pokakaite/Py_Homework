from main import *

greeting.set_choice()
if greeting.get_choice() == 1:
    show_hot_dog_items.get_items(hot_dog, vegan_hot_dog, spicy_hot_dog)
    show_ingredients.get_items(ketchup, mayonaise, mustard, jalapeno, onion, pickles)


    def func_hot_dogs():
        choose_between(make_dict(show_hot_dog_items.show,
                                 show_ingredients.show), greeting.get_choice())

        choose_hot_dog.set_choice()
        order.show()
        choose_between(make_dict(hot_dog.show, vegan_hot_dog.show, spicy_hot_dog.show), choose_hot_dog.get_choice())
        order.add_to_order(
            choose_between_hot_dogs(make_dict(hot_dog, vegan_hot_dog, spicy_hot_dog), choose_hot_dog.get_choice()))

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

order.show()
file.add_to_file(order.order_items)
pay.add_to_sum(order.order_items)
pay.show(order.order_items)
