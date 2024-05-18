class Calc:
    def __init__(self):
        self.result = 0

    def calculate(self, items):
        self.result = 0
        for item in items:
            self.result += item.price * item.amount
        return self.result
