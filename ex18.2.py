import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f'{self.rank} of {self.suit}'

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def __repr__(self):
        return f'Hand: {", ".join(str(card) for card in self.cards)}'

class Deck:
    def __init__(self):
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        random.shuffle(self.cards)

    def deal_hands(self, num_hands, cards_per_hand):
        total_cards_needed = num_hands * cards_per_hand
        if len(self.cards) < total_cards_needed:
            raise ValueError("Not enough cards in the deck to deal the hands.")

        hands = []
        for _ in range(num_hands):
            hand = Hand()
            for _ in range(cards_per_hand):
                card = self.cards.pop()
                hand.add_card(card)
            hands.append(hand)
        return hands

# Exemplo de uso
deck = Deck()
try:
    hands = deck.deal_hands(3, 5)
    for i, hand in enumerate(hands, 1):
        print(f'Hand {i}: {hand}')
except ValueError as e:
    print(e)
