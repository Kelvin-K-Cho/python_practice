import random
import copy

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
        if self.count() == 0:
            self.deck = []
            for suit in suits:
                for rank in ranks:
                    self.deck.append(Card(suit, rank))
            self.shuffle()
        return self.deck.pop()

    def count(self):
        return len(self.deck)

class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def __str__(self):
        array = []
        for card in self.cards:
            array.append(str(card))
        return str(array)

    def add_card(self, card):
        if card.rank == "Ace":
            self.aces += 1
        self.value += values[card.rank]
        self.cards.append(card)

    def adjust_for_aces(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

    def reset(self):
        self.cards = []
        self.value = 0
        self.aces = 0

class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += (2 * self.bet)
        self.bet = 0

    def lose_bet(self):
        self.bet = 0

    def push_bet(self):
        self.total += self.bet
        self.bet = 0

    def take_bet(self):
        while True:
            try:
                print(f"Your current total: {self.total}")
                bet = int( input("Please enter your bet: ") )
                if self.total - bet < 0:
                    raise ValueError
            except:
                print("Please enter a valid amount that does not exceed your current total.")
            else:
                break
        self.bet = bet
        self.total -= self.bet
        return self.bet

class Bank(Chips):

    def take_bet(self, bet):
        try:
            if self.total < 0:
                raise ValueError
        except:
            return False
        self.bet = bet
        self.total -= self.bet
        return self.bet

class Player:

    def __init__(self, hand, chips):
        self.hand = hand
        self.chips = chips

    def hit(self, deck):
        card = deck.deal()
        self.hand.add_card(card)
        self.hand.adjust_for_aces()

    def hit_or_stand(self, deck):
        global playing
        while True:
            try:
                option = int( input("Hit or Stand? (enter 1 or 0): ") )
                if option == 1 or option == 0:
                    pass
                else:
                  raise ValueError
            except:
                print("Try again.")
            else:
                if option == 1:
                    self.hit(deck)
                else:
                    playing = False
                break

    def show_hand(self):
        return self.hand

    def bust(self):
        self.chips.lose_bet()

    def win(self):
        self.chips.win_bet()

    def bet(self):
        return self.chips.take_bet()

    def push(self):
        self.chips.push_bet()

class Dealer(Player):

    def bet(self, amount):
        return self.chips.take_bet(amount)

    def show_hand(self):
        if len(self.hand.cards) == 0:
            return []
        hidden = copy.deepcopy(self.hand.cards)
        hidden[0] = "x"
        self.hand.cards = hidden
        return self.hand


print("Welcome to Blackjack.")
deck = Deck(suits, ranks)
deck.shuffle()
player = Player( Hand(), Chips() )
dealer = Dealer( Hand(), Bank() )

while True:

    if player.chips.total <= 0:
        print("Sorry, you've lost")
        break

    if dealer.chips.total <= 0:
        print("Congratulations, you've won.")
        break

    amount = player.bet()

    counter = dealer.bet(amount)

    if counter == False:
        print("Congratulations, you've won.")
        break

    for _ in range(2):
        player.hit(deck)
        dealer.hit(deck)

    print(f"Player's hand: {player.show_hand()}")

    print(f"Dealer's hand: {dealer.show_hand()} \n")

    while playing:

        print(f"Player's hand: {player.show_hand()}")

        player.hit_or_stand(deck)

        if player.hand.value > 21:
            playing = False


    if player.hand.value > 21:
        pass
    else:
        while dealer.hand.value < 17:
            print(f"\nDealer's hand: {dealer.show_hand()}")
            dealer.hit(deck)

    if player.hand.value > 21:
        print(f"\nDealer's hand: {dealer.show_hand()}")
        print(f"Player's hand: {player.show_hand()}")
        player.bust()
        dealer.win()
    elif dealer.hand.value > 21:
        print(f"\nDealer's hand: {dealer.show_hand()}")
        print(f"Player's hand: {player.show_hand()}")
        dealer.bust()
        player.win()
    elif player.hand.value == dealer.hand.value:
        print(f"\nDealer's hand: {dealer.show_hand()}")
        print(f"Player's hand: {player.show_hand()}")
        player.push()
        dealer.push()
    elif player.hand.value > dealer.hand.value:
        print(f"\nDealer's hand: {dealer.show_hand()}")
        print(f"Player's hand: {player.show_hand()}")
        player.win()
        dealer.bust()
    else:
        print(f"\nDealer's hand: {dealer.show_hand()}")
        print(f"Player's hand: {player.show_hand()}")
        dealer.win()
        player.bust()

    dealer.hand.reset()
    player.hand.reset()

    playing = True
