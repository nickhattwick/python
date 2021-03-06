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
        self.playedland = False
        self.mana = 0

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
    if not p1.playedland:
        while x < len(p1.hand):
            if p1.hand[x] == "l":
                print "x: ", x
                y = p1.hand.pop(x)
                p1.lands.append(y)
                p1.mana = len(p1.lands)
                print "Mana: ", p1.mana
                p1.playedland = True
                prompt()
            else:
                x+=1
        print "No lands in hand"
        prompt()
    else:
        print "You've already played a land this turn"
        prompt()

def summon():
    mhand = [x for x in p1.hand if x != "l"]
    print "Monsters: ", mhand
    mchoice = raw_input("Which monster would you like to summon?\n")
    if str(mchoice) in mhand:
        if int(mchoice) <= p1.mana:
            y = p1.hand.index(mchoice)
            z = p1.hand.pop(y)
            p1.field.append(z)
            p1.blockers.append(z)
            p1.mana = p1.mana - int(mchoice)
            print p1.field
            print "Mana Left: ", p1.mana
            prompt()
        else:
            print "You can only play monsters less than or equal to your mana"
            prompt()
    else:
        print "That's not a card in your hand"
        prompt()

def block():
    if not p2.blockers:
        p2.life = p2.life - int(atk)
        print "OP LP: ", p2.life
        if p2.life <= 0:
            print "You Win!"
            exit()
    elif max(p2.blockers) >= atk:
        blk = [x for x in p2.blockers if x >= atk]
        if min(blk) > atk:
            a = min(blk)
            b = p2.blockers.index(a)
            p2.blockers.pop(b)
            c = p1.blockers.index(atk)
            d = p1.field.index(atk)
            p1.blockers.pop(c)
            p1.field.pop(d)
            p1.dpile.append(atk)
            print "Opponent blocked with ", blk, ". Your ", atk, "was destroyed."
        else:
            blist = sorted(p2.blockers)
            x = 0
            while x < len(blist):
                if blist[x] >= atk:
                    a = blist[x]
                    b = p2.blockers.index(a)
                    p2.blockers.pop(b)
                    c = p1.blockers.index(atk)
                    d = p1.field.index(atk)
                    p1.blockers.pop(c)
                    p1.field.pop(d)
                    p1.dpile.append(atk)
                    print "Opponent blocked with ", a, ". Your ", atk, "was destroyed."
                    break
                else:
                    x = x + 1
    elif atk > p2.life:
        bmin = min(p2.blockers)
        x = p2.blockers.index(bmin)
        a = p2.field.index(bmin)
        y = p2.field.pop(a)
        p2.blockers.pop(x)
        p2.dpile.append(y)
        print "OP blocked with ", bmin
        print "OP's ", bmin, " was destroyed"

    else:
        p2.life = p2.life - int(atk)
        print "OP LP: ", p2.life
        if p2.life <= 0:
            print "You Win!"
            exit()

def attack():
    if not p1.blockers:
        print "there's nothing there"
        opturn()
    else:
        print "Your Attackers: ", p1.blockers
        print "OP's Blockers: ", p2.blockers
        global atk
        atk = raw_input("Which creature would you like to attack with?\n")
        if str(atk) in p1.blockers:
            block()
            y = p1.blockers.index(atk)
            p1.blockers.pop(y)
            secatkchoice()
        elif atk in p1.field:
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
            p2.blockers.pop(x)
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
                        a = p1.blockers.index(y)
                        p1.blockers.pop(a)
                        p2.blockers.pop(x)
                        p2.dpile.append(c)
                        print "OP's monster was destroyed"
                    elif p2.blockers[x] > y:
                        z = p1.field.index(y)
                        c = p1.field.pop(z)
                        p1.blockers.pop(y)
                        p2.blockers.pop(x)
                        p1.dpile.append(c)
                        print "Your ", y, " was destroyed"
                    else:
                        z = p2.field.index(p2.blockers[x])
                        c = p2.field.pop(z)
                        p2.dpile.append(c)
                        h = p1.field.index(y)
                        g = p1.field.pop(h)
                        p1.blockers.pop(y)
                        p2.blockers.pop(x)
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
            p2.mana = len(p2.lands)
            print "OP has ", p2.mana, " lands"
            break
        else:
            x+=1
    opsummon()

def opsummon():
    print "in summon phase test"
    mhand = [x for x in p2.hand if x != "l"]
    p2.mana = len(p2.lands)
    rhand = sorted(mhand, reverse=True)
    x = 0
    while x < len(rhand) and p2.mana > 0:
        if int(rhand[x]) <= p2.mana:
            a = rhand[x]
            b = p2.hand.index(a)
            c = p2.hand.pop(b)
            rhand.pop(x)
            print "OP summons ", a
            p2.field.append(c)
            p2.mana = p2.mana - int(a)
        else:
            x = x + 1

    print "OP's field: ", p2.field
    p2.blockers = list(p2.field)
    if not p2.blockers:
        print "End of OP's turn"
    else:
        whoblocks()
    plturn()


def plturn():
    p1.playedland = False
    p1.draw()
    p1.mana = len(p1.lands)
    p1.blockers = list(p1.field)
    print "Hand: ", p1.hand
    print "Field: ", p1.field
    print "Mana: ", p1.mana

    prompt()

def opturn():
    print "Opponent's Turn"
    p2.draw()
    print "OP has ", len(p2.hand), " cards in hand"
    opland()

plturn()
