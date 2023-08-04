# random numbr selecting in a die

from random import randint

class Die():

    def __init__(self,numb_sides=6):
        self.numb_sides=numb_sides

    def roll(self):
        return randint(1,self.numb_sides)
