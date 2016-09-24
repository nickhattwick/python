import itertools
import random

class Deck:
    def __init__(self):
        self.suits = ['Spades','Hearts','Diamonds','Clubs']
        self.values = range(1,14)
        self.cards = list(itertools.product(self.suits,self.values))
    def draw(self):
        
