class HotDog:
    def __init__(self):
        self.name = None
        self.bun = None
        self.sausage = None

    def __repr__(self):
        return ('\nНазвание хот-дога - {0.name}\n'
                'Булочка - {0.bun}\n'
                'Сосиска - {0.sausage}\n').format(self)