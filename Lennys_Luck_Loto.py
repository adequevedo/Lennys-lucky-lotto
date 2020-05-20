import random
import os
class Card(object):
    def __init__(self,suit,val):
        self.suit = suit
        self.value = val
    def show(self):
        print ("{} of {}".format(self.value,self.suit))



class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1,14):
                self.cards.append(Card(s,v))
    def show(self):
        for c in self.cards:
            c.show()
    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            r = random.randint(0,i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
    def drawCard(self):
        return self.cards.pop()


class Player(object):
    def __init__(self,name):
        self.name =name
        self.hand = []
    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self
    def showHand(self):
        for card in self.hand:
            card.show()
    def discard(self):
        return self.hand.pop()

correct=0
incorrect=0
remaining =52
deck = Deck()
deck.shuffle()
print("You are Playing lennys lucky lotto")
numplayers =input("Single or double player S/D Dont select D not yet finished")
if numplayers=="D":
    player1 = Player("Player1")
    player2 = Player("Player2")
else:
    while deck.__sizeof__()>0:
        guesses=0
        print("You have ", correct ," correct and ", incorrect," incorrect with ",remaining," cards remaing")
        cardtobeguessed=deck.drawCard()
        while guesses<3:

            guess=input("What card would you like to guess")

            if int(cardtobeguessed.value)==int(guess):
                os.system('cls')
                print("ding ding ding")
                correct+=1
                remaining-=1
                guesses+=1
                print()
                break

            elif int(cardtobeguessed.value)> int(guess):
                print("HIGHER")
                guesses+=1

            elif int(cardtobeguessed.value)<int(guess):
                print("Lower")
                guesses+=1

            if guesses==3:
                os.system('cls')
                print("RRRERERERRER")
                print("The card was")
                print(cardtobeguessed.show())
                incorrect += 1
                remaining -= 1
                print()
                print()
                print()

