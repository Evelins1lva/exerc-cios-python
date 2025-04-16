import random

class Card:
    """Representa uma carta de um baralho de pôquer."""
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f'{self.rank} of {self.suit}'

    def __lt__(self, other):
        """Define a ordem para comparação entre cartas, baseado no valor numérico do rank."""
        return self.ranks.index(self.rank) < self.ranks.index(other.rank)


class Deck:
    """Representa um baralho de pôquer."""
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Card.suits for rank in Card.ranks]
        random.shuffle(self.cards)

    def deal(self, num):
        """Distribui um número específico de cartas."""
        hand = self.cards[:num]
        self.cards = self.cards[num:]
        return hand

    def shuffle(self):
        """Embaralha o baralho."""
        random.shuffle(self.cards)
