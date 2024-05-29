class Field:
    def __init__(self):
        self.space_1 = ' '
        self.space_2 = ' '
        self.space_3 = ' '
        self.space_4 = ' '
        self.space_5 = ' '
        self.space_6 = ' '
        self.space_7 = ' '
        self.space_8 = ' '
        self.space_9 = ' '

    def make_field(self):
        print(f''' {self.space_1} | {self.space_2} | {self.space_3}
---+---+---
 {self.space_4} | {self.space_5} | {self.space_6}
---+---+---
 {self.space_7} | {self.space_8} | {self.space_9}''')

field = Field()