Deck = []
def addlands(xli):
    x = 0
    while x <= 20:
        xli.append ('l')
        x += 1

addlands(Deck)

Deck.extend((2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,5,5,6))
print Deck
print len(Deck)

def Game():
    class player:
        life = 20
        deck = Deck

        def __init__(self, name):
            self.name = name

P1 = player('Player 1')
p2 = player('Player 2')
