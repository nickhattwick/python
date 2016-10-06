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
        self.blockers = []
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

def prompt():
    choice = raw_input("It's your turn. What will you do? \n LAND SUMMON ATTACK DONE\n")
    if choice.upper() == "LAND":
        playland()
    elif choice.upper() == "SUMMON":
        summon()
    elif choice.upper() == "ATTACK":
        attack()
    elif choice.upper() == "DONE":
        print "Turn End.\n Opponent's Turn"
        p1.blockers = list(p1.field)
        opturn()

    elif choice.upper() == "QUIT":
        exit()

    else:
        print "That's not even a thing"
        prompt()

def playland():
    x = 0
    while x < len(p1.hand):
        if p1.hand[x] == "l":
            print "x: ", x
            y = p1.hand.pop(x)
            p1.lands.append(y)
            mana = len(p1.lands)
            print "Mana: ", mana
            prompt()
        else:
            x+=1
    print "No lands in hand"
    prompt()

def summon():
    mhand = [x for x in p1.hand if x != "l"]
    mana = len(p1.lands)
    print "Monsters: ", mhand
    mchoice = raw_input("Which monster would you like to summon?\n")
    if int(mchoice) <= mana:
        y = p1.hand.index(mchoice)
        z = p1.hand.pop(y)
        p1.field.append(z)
        p1.blockers.append(z)
        print p1.field
        prompt()
    elif mchoice in p1.hand:
        print "You can only play monsters less than or equal to your mana"
        prompt()
    else:
        print "That's not a card in your hand"
        prompt()

def block():
    print "block is go"


def attack():
    print p1.blockers
    if not p1.blockers:
        print "there's nothing there"
        opturn()
    else:
        x = raw_input("Which creature would you like to attack with?\n")
        if str(x) in p1.blockers:
            block()
            y = p1.blockers.index(x)
            p1.blockers.pop(y)
            secatkchoice()
        elif x in p1.field:
            print "You can't attack with that"
            prompt()
        elif not p1.blockers:
            print "There's nothing there"
            prompt()
        else:
            print "That's not even a thing"
            prompt()

def secatkchoice():
    choice = raw_input("Would you like to attack with another monster?\nY or N\n")
    if choice.upper() == "Y":
        attack()
    elif choice.upper() == "N":
        opturn()
    else:
        print "That's not a thing..."
        secatkchoice()

def whoblocks():
    print "Attack Phase"
    x = 0
    while x < len(p2.blockers):
        print "A", p2.blockers[x], "is attacking you."
        if not p1.blockers:
            p1.life = p1.life - int(p2.blockers[x])
            print "LP: ", p1.life
            if p1.life <= 0:
                print "Game Over"
                exit()
            else:
                x = x + 1
        else:
            choice = raw_input("Will you block? Y or N\n")
            if choice.upper() == "Y":
                print p1.blockers
                y = raw_input("Who will you block with?\n")
                if y in p1.blockers:
                    if y > p2.blockers[x]:
                        z = p2.field.index(p2.blockers[x])
                        c = p2.field.pop(z)
                        p2.dpile.append(c)
                        print "OP's monster was destroyed"
                    elif p2.blockers[x] > y:
                        z = p1.field.index(y)
                        c = p1.field.pop(z)
                        p1.dpile.append(c)
                        print "Your ", y, " was destroyed"
                    else:
                        z = p2.field.index(p2.blockers[x])
                        c = p2.field.pop(z)
                        p2.dpile.append(c)
                        h = p1.field.index(y)
                        g = p1.field.pop(h)
                        p1.dpile.append(g)
                        print "It's a draw, both creatures were destroyed"
                    x = x + 1

                elif y in p1.field:
                    print "You can't block with that"
                    whoblocks()
                else:
                    print "That's not even a thing"
                    whoblocks()
            elif choice.upper() == "N":
                p1.life = p1.life - int(p2.blockers[x])
                print "LP: ", p1.life
                if p1.life <= 0:
                    print "Game Over"
                    exit()
                else:
                    x = x + 1

            else:
                print "That's not even a thing"
                whoblocks()


def opland():
    x = 0
    while x < len(p1.hand):
        if p2.hand[x] == "l":
            print "x: ", x
            y = p2.hand.pop(x)
            p2.lands.append(y)
            opmana = len(p2.lands)
            print "OP has ", opmana, " lands"
            break
        else:
            x+=1
    opsummon()

def opsummon():
    print "in summon phase test"
    mhand = [x for x in p2.hand if x != "l"]
    opmana = len(p2.lands)
    rhand = sorted(mhand, reverse=True)
    x = 0
    while x < len(rhand) and opmana > 0:
        if int(rhand[x]) <= opmana:
            a = rhand[x]
            b = p2.hand.index(a)
            c = p2.hand.pop(b)
            rhand.pop(x)
            print "OP summons ", a
            p2.field.append(c)
            opmana = opmana - int(a)
        else:
            x = x + 1

    print "OP's field: ", p2.field
    p2.blockers = list(p2.field)
    if not p2.blockers:
        print "End of OP's turn"
        plturn()
    else:
        whoblocks()


def plturn():
    p1.draw()
    mana = len(p1.lands)
    p1.blockers = list(p1.field)
    print "Hand: ", p1.hand
    print "Field: ", p1.field
    print "Mana: ", mana

    prompt()

def opturn():
    print "Opponent's Turn"
    p2.draw()
    print "OP has ", len(p2.hand), " cards in hand"
    opland()

plturn()
