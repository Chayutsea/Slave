#---------- import library ----------#
import pygame
import random
pygame.init()

#---------- screen & window setting ----------#
width = 1280                            #set width resolution
height = 720                            #set height resolution
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Slave")     #set window caption
icon = pygame.image.load('icon.png')    #set icon
pygame.display.set_icon(icon)

#---------- class setting ----------#
class Card( object ):
    def __init__(self, value, suit, rank):
        self.value = value
        self.suit = suit
        self.rank = rank
    def __repr__(self):
        return str(self.value) + " of " + str(self.suit)
    def __lt__(self, other):
        return self.rank < other.rank

class Deck( list ):
    def __init__(self):
        suits = {"Clubs":1, "Diamonds":2, "Hearts":3, "Spades":4}
        values = {"Three":1, "Four":2, "Five":3, "Six":4, "Seven":5, "Eight":6, "Nine":7, "Ten":8,
        "Jack":9, "Queen":10, "King":11 ,"Ace":12, "Two":13 }
        rank = 1
        for value in values:
            for suit in suits:
                self.append(Card(value, suit, rank))
                rank += 1
    def deal(self):
        return self.pop()

class Player( object ):
    def __init__(self, name):
        self.name = name
        self.hand = []
    def draw(self, deck):
        self.hand.append(deck.deal())
    def showHand(self):
        for index in range(len(self.hand)):
            screen.blit(pygame.transform.scale(image(self.hand[index]), (125, 180)), (90*(index), 540))

#---------- other function ----------#

#use for finding the image path of the object
def image(obj):
    path =  "pictures/" + str(obj) + ".png"
    return pygame.image.load(path)

#---------- main game function ----------#

#prepare before game start
running = True                  #use for checking if quit the game
deck = Deck()                   #generate deck (52 cards)
random.shuffle(deck)            #shuffle deck
p1 = Player("Player 1")         #create player 1
p2 = Player("Player 2")         #create player 2
p3 = Player("Player 3")         #create player 3
p4 = Player("Player 4")         #create player 4

#deal cards to each players (13 cards for each players)
while deck:
    p1.draw(deck)
    p2.draw(deck)
    p3.draw(deck)
    p4.draw(deck)

#sort hand for each players
p1.hand.sort()
p2.hand.sort()
p3.hand.sort()
p4.hand.sort()

#start the game
while running:
    screen.fill((0, 100, 0))    #fill background with green
    p1.showHand()               #show hand for player 1 (ourself's hand)

    #check if quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    
    pygame.display.update()     #update screen