class Calculator:
    def __init__(self, price, amount):
        self.price = price
        self.amount = amount

    def get_result(self):
        return self.price * self.amount