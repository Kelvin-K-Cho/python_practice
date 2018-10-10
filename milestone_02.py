import random

suits = ("Spades", "Hearts", "Clubs", "Diamonds")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11
}

playing = True

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:

    def __init__(self, suits, ranks):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        array = []
        for card in self.deck:
            array.append(str(card))
        return str(array)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.suit == "Ace":
            self.aces += 1

    def adjust_for_aces(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0
