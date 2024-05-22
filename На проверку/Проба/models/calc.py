class CalculateOrder:
    def __init__(self):
        self.order_summ = []

    def add_to_order_summ(self, donut_price):
        self.order_summ.append(donut_price)

    def get_order_summ(self):
        if len(self.order_summ) >= 3:
            return sum(self.order_summ) - sum(self.order_summ) * 0.1
        else:
            return sum(self.order_summ)