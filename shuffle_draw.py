from random import shuffle

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
        self.hand = []
        self.deck = Deck

p1 = player('P1')

count = 0
while (count < 7):
    x = p1.deck.pop()
    p1.hand.append(x)
    count += 1

print p1.hand
