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
        print p1.field
        prompt()
    elif mchoice in p1.hand:
        print "You can only play monsters less than or equal to your mana"
        prompt()
    else:
        print "That's not a card in your hand"
        prompt()

def block():
    print "Block-test: Success"

def attack():
    global possible
    possible = p1.field
    print possible
    if not possible:
        print "there's nothing there"
        prompt()
    else:
        x = raw_input("Which creature would you like to attack with?\n")
        if str(x) in possible:
            block()
            y = possible.index(x)
            possible = possible.pop(y)
            secatkchoice()
        elif x in p1.field:
            print "You can't attack with that"
            prompt()
        elif not possible:
            print "There's nothing there"
            prompt()
        else:
            print "That's not even a thing"
            prompt()

def secatkchoice():
    choice = raw_input("Would you like to attack with another monster?\nY or N")
    if choice.upper() == "Y":
        attack()
    elif choice.upper() == "N":
        prompt()
    else:
        print "That's not a thing..."
        secatkchoice()

def opland():
    x = 0
    while x < len(p1.hand):
        if p2.hand[x] == "l":
            print "x: ", x
            y = p2.hand.pop(x)
            p2.lands.append(y)
            opmana = len(p2.lands)
            print "OP has ", opmana, " lands"

        else:
            x+=1
    opsummon()

def opsummon():
    mhand = [x for x in p2.hand if x != "l"]
    opmana = len(p2.lands)
    rhand = sorted(mhand, reverse=True)
    x = 0
    while x < len(rhand):
        if int(rhand[x]) <= opmana:
        #PICK UP HERE

    mchoice = max(mhand)

    y = p2.hand.index(mchoice)
    z = p2.hand.pop(y)
    p2.field.append(z)
    Print "OP summons "
    print "OP's field: ", p2.field

def plturn():
    global mana
    mana = len(p1.lands)
    p1.draw()
    print "Hand: ", p1.hand
    print "Field: ", p1.field
    print "Mana: ", mana

    prompt()

def opturn():
    print "Opponent's Turn"
    p2.draw()
    print "OP has ", len(p2.hand), " cards in hand"


plturn()
