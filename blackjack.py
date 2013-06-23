# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
player = []
dealer = []

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []

    def __str__(self):
        strHand = ""
        for c in self.hand:
            strHand += (str(c) + ", ")
        return strHand

    def add_card(self, cardN):
        self.hand += [cardN]

    def get_value(self):
        value = 0
        for r in self.hand:
            if r.rank not in ('A', 'T', 'J', 'Q', 'K'):
                value += int(r.rank)
            elif r.rank in ('T', 'J', 'Q', 'K'):
                value += 10
            elif r.rank == 'A':
                if value < 11:
                    value += 10
                value += 1
        return value

    def draw(self, canvas, pos):
        for c in self.hand:
            c.draw(canvas, [300, 300])
 
    def __len__(self):
        return len(self.hand)
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for S in SUITS:
            for R in RANKS:
                self.deck.append(Card(S,R))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()
    
    def __str__(self):
        strDeck = ""
        for c in self.deck:
            strDeck += (str(c) + ", ")
        return strDeck
    
    def __len__(self):
        return len(self.deck)


#define event handlers for buttons
def deal():
    global outcome, in_play, player, dealer, deck
    deck = Deck()
    deck.shuffle()
    dealer = Hand()
    player = Hand()
    dealer.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    in_play = True
    print str(player), str(dealer)

def hit():
    global outcome, in_play, player, dealer
    player.add_card(deck.deal_card())
    if player.get_value() > 21:
        print "You Have Busted."
        in_play = False
    print str(player), str(dealer)
    if dealer.get_value() < 17:
        dealer.add_card(deck.deal_card())
        print str(player), str(dealer)
        
def stand():
    global outcome, in_play, player, dealer
    if player.get_value() > 21:
        print "Busted"
        outcome += "Dealer"
    elif player.get_value() <= 21:
        while dealer.get_value() < player.get_value():
            dealer.add_card(deck.deal_card())
        if dealer.get_value() > 21:
            print "You win."
            outcome += "Player"
        elif dealer.get_value() >= player.get_value():
            print "You lose."
            outcome += "Dealer"
        elif dealer.get_value() < player.get_value():
            print "You win."
            outcome += "Player"
    print str(player), str(dealer)


# draw handler    
def draw(canvas):
    
    card = Card("S", "T")
    card.draw(canvas, [300, 300])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
frame.start()


# remember to review the gradic rubric