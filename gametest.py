from random import shuffle

Deck = []
def addlands(xli):
    x = 0
    while x <= 20:
        xli.append ('l')
        x += 1

addlands(Deck)

Deck.extend(("2","2","2","2","2","2","3","3","3","3","3","3","4","4","4","4","5","5","6"))

class player:
    def __init__(self, name):
        self.name = name
        self.life = 20
        self.hand = []
        self.field = []
        self.lands = []
        self.dpile = []
        self.deck = Deck

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

def block():
    pass

def attack():
    x = raw_input("Which creature would you like to attack with?\n")
    if attacker in possible:
        print attacker
        block()
        y = possible.index(x)
        possible = possible.pop(y)
        choice = raw_input("Would you like to attack with another monster?\nY or N")

def plturn():
    global mana
    mana = len(p1.lands)

    print "Hand: ", p1.hand
    print "Field: ", p1.field
    print "Mana: ", mana
    def prompt():
        choice = raw_input("It's your turn. What will you do? \n LAND SUMMON ATTACK DONE\n")
        if choice.upper() == "LAND":
            x = 0
            while x < len(p1.hand):
                if p1.hand[x] == "l":
                    print "x: ", x
                    y = p1.hand.pop(x)
                    p1.lands.append(y)
                    mana = len(p1.lands)
                    print "Mana: ", mana
                    break
                else:
                    x+=1
                    print "No lands left"
            prompt()
        elif choice.upper() == "SUMMON":
            mhand = [x for x in p1.hand if x != "l"]
            mana = len(p1.lands)
            print "Monsters: ", mhand
            mchoice = raw_input("Which monster would you like to summon?\n")
            try:
                if int(mchoice) <= mana:
                    y = p1.hand.index(mchoice)
                    z = p1.hand.pop(y)
                    p1.field.append(z)
                    print p1.field
                    prompt()
                else:
                    print "You can only play monsters less than or equal to your mana"
                    prompt()
            except:
                print "That's not a card in your hand"
                prompt()

        elif choice.upper() == "ATTACK":
            possible = p1.field
            print possible
            x = raw_input("Which creature would you like to attack with?\n")
            if attacker in possible:
                print attacker
                block()
                y = possible.index(x)
                possible = possible.pop(y)

                def secondchoice():
                    choice = raw_input("Would you like to attack with another monster?\nY or N")
                    if choice.upper() == Y:
                        attack()
                    elif choice.upper() == N:
                        prompt()
                secondchoice()
            elif attacker in p1.field:
                print "You can't attack with that"
            else:
                print "That's not even a thing"

        elif choice.upper() == "DONE":
            print "Turn End.\n Opponent's Turn"
            opturn()

        elif choice.upper() == "QUIT":
            exit()

        else:
            print "That's not even a thing"
            prompt()

    prompt()

def opturn():
    print "Success"

plturn()
