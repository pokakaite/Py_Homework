class AddToList:
    def __init__(self):
        self.ingredient = None
        self.list = None

    def set_list(self):
        self.list = []

    def add_to_list(self, ingredient):
        self.list.append(ingredient)

    def get_list(self):
        return self.list