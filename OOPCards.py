import random

class Card:
    suits = ['\u2666', '\u2665', '\u2663', '\u2660']
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] 


    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{Card.ranks[self.rank]} of {Card.suits[self.suit]}"
    
    def __lt__(self, other):
        if self.rank == other.rank:
            return self.suit < other.suit
        else:
            return self.rank < other.rank

class Deck:

    def __init__(self):
        self.deck = []
        for suit in range(4):
            for rank in range(13):
                self.deck.append(Card(suit, rank))
        self.shuffle()
    
    def __len__(self):
        return len(self.deck)
    
    def add_card(self, card):
        self.deck.append(card)
    
    def pop_card(self):
        return self.deck.pop()
    
    def shuffle(self):
        random.shuffle(self.deck)

deck = Deck()

class Hand(Deck):

    def __init__(self, label):
        self.deck = []
        self.label = label
        self.win_count = 0
    
    def __str__(self):
        return self.label + ': ' + ' '.join([str(card) for card in self.deck])
    
    def get_label(self):
        return self.label
    
    def get_win_count(self):
        return self.win_count
    
    def round_winner(self):
        self.win_count = self.win_count + 1

hand = Hand("Player")

hand.add_card(deck.pop_card())
hand.add_card(deck.pop_card())
hand.add_card(deck.pop_card())
hand.add_card(deck.pop_card())
hand.add_card(deck.pop_card())

print(hand)