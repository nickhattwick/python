import collections
from random import shuffle
from random import choice

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
        self.hand = []
        self.field = []
        self.dpile = []
        self.deck = collections.deque(Deck)

    def draw(self):
        x = self.deck.pop()
        self.hand.append(x)

p1 = player('P1')
p2 = player('P2')

players = (p1, p2)

for p in players:
    p.count = 0
    shuffle(p.deck)
    while (p.count < 7):
        p.draw()
        p.count += 1

print "P1: ", p1.hand
print "P2: ", p2.hand
