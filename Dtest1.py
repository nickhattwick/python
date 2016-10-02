import random

Deck = []
def addlands(xli):
    x = 0
    while x <= 20:
        xli.append ('l')
        x += 1

addlands(Deck)

Deck.extend((2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,5,5,6))


class player:
    def __init__(self, name):
        self.name = name
        self.life = 20
        self.deck = Deck
        self.field = []
        self.hand = []
        self.pile = []


def Game():
    P1 = player('Player 1')
    P2 = player('Player 2')


    random.shuffle(P1.deck)
    random.shuffle(P2.deck)

    x = P1.deck[0,7]
    P1.hand.extend(x)
    y = P2.deck[0,7]
    P2.hand.extend(y)

    print P1.hand

Game
