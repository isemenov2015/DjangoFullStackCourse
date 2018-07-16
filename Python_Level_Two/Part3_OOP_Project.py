#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """

    def __init__(self):
        self.pile = []
        for s in SUITE:
            for r in RANKS:
                self.pile.append((s, r))

    def split(self):
        return (self.pile[:int(len(self.pile)/2)], self.pile[int(len(self.pile)/2):])

    def shuffle(self):
        shuffle(self.pile)

class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, cards):
        self.hand = cards

    def is_empty(self):
        return len(self.hand) == 0

    def size(self):
        return len(self.hand)

    def add(self, card):
        self.hand.append(card)

    def remove(self):
        card = self.hand[0]
        self.hand = self.hand[1:]
        return card

    def cards(self):
        return self.hand

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Player can then play cards and check if they still have cards.
    """
    def __init__(self, name, cards):
        self.name = name
        self.hand = Hand(cards)

    def bet(self):
        return self.hand.remove()

    def win(self, cards_list):
        for card in cards_list:
            self.hand.add(card)
        return len(cards_list)

    def has_cards(self):
        return self.hand.size() > 0

    def hand_size(self):
        return self.hand.size()

    def cards(self):
        return self.hand.cards()

    def get_name(self):
        return self.name;

######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

# Use the 3 classes along with some logic to play a game of war!
deck = Deck()
deck.shuffle()
cards = deck.split()
player1 = Player("One", cards[0])
player2 = Player("Two", cards[1])
print("First player has {} cards: {}".format(len(player1.cards()), player1.cards()))
print("Second player has {} cards: {}".format(len(player2.cards()), player2.cards()))
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'
round = 1
cards_stack = []
while player1.has_cards() and player2.has_cards():
    card1 = player1.bet()
    card2 = player2.bet()
    #print("Round {}. Bet made. {}: {}, {}: {}".format(round, player1.get_name(), card1, player2.get_name(), card2))
    #print("{} has {} cards, {} has {} cards".format(player1.get_name(), player1.hand_size(), player2.get_name(), player2.hand_size() ))
    #print("Stack size: {}".format(len(cards_stack)))
    if ranks.index(card1[1]) > ranks.index(card2[1]):
        #print("{} won a round".format(player1.get_name()))
        player1.win(cards_stack)
        player1.win([card1, card2])
        cards_stack = []
    elif ranks.index(card1[1]) < ranks.index(card2[1]):
        #print("{} won a round".format(player2.get_name()))
        player2.win(cards_stack)
        player2.win([card1, card2])
        cards_stack = []
    else:
        cards_stack.append(card1)
        cards_stack.append(card2)
        for i in range(3):
            if player1.has_cards():
                cards_stack.append(player1.bet())
            if player2.has_cards():
                cards_stack.append(player2.bet())
        #print("Draw. Cards stack length: {}, {}".format(len(cards_stack), cards_stack))
        #print("{}: {} cards, {}: {} cards".format(player1.get_name(), player1.hand_size(), player2.get_name(), player2.hand_size()))
        #input()
    round += 1
    if round % 1000 == 0:
        print("Round {}, Cards {}:{}".format(round, player1.hand_size(), player2.hand_size()))
if player1.has_cards():
    winner = player1
else:
    winner = player2
print("{} won the game!".format(winner.get_name()))
