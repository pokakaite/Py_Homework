class Calc:
    def __init__(self):
        self.result = 0

    def calculate(self, item):
        item.price = 10
        self.result = item.price + sum(item.topping_price)
        return self.result


class CalculateOrder:
    def get_order_summ(self, order_items):
        list_prices = []
        for item in order_items:
            list_prices.append(item.price)

        if len(list_prices) >= 3:
            return sum(list_prices) - sum(list_prices) * 0.1
        else:
            return sum(list_prices)