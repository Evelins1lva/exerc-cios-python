from Card import Card, Deck

class PokerHand:
    def _init_(self):
        self.cards = []
        self.label = None  

    def add_cards(self, cards):
        self.cards = cards

    def get_rank_hist(self):
        hist = {}
        for card in self.cards:
            hist[card.rank] = hist.get(card.rank, 0) + 1
        return hist

    def has_pair(self):
        hist = self.get_rank_hist()
        return list(hist.values()).count(2) >= 1

    def has_twopair(self):
        hist = self.get_rank_hist()
        return list(hist.values()).count(2) >= 2

    def has_three_of_a_kind(self):
        hist = self.get_rank_hist()
        return 3 in hist.values()

    def has_four_of_a_kind(self):
        hist = self.get_rank_hist()
        return 4 in hist.values()

    def has_full_house(self):
        hist = self.get_rank_hist()
        return 3 in hist.values() and 2 in hist.values()

    def has_flush(self):
        suits = {}
        for card in self.cards:
            suits[card.suit] = suits.get(card.suit, 0) + 1
        return any(count >= 5 for count in suits.values())

    def has_straight(self):
        valor_cartas = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                        '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

        ranks = set(valor_cartas[card.rank] for card in self.cards)
        if 14 in ranks:
            ranks.add(1)

        sorted_ranks = sorted(ranks)
        for i in range(len(sorted_ranks) - 4):
            seq = sorted_ranks[i:i+5]
            if seq[4] - seq[0] == 4 and len(seq) == 5:
                return True
        return False

    def has_straight_flush(self):
        valor_cartas = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                        '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

        suits = {}
        for card in self.cards:
            suits.setdefault(card.suit, []).append(card)

        for suited_cards in suits.values():
            if len(suited_cards) >= 5:
                ranks = set(valor_cartas[card.rank] for card in suited_cards)
                if 14 in ranks:
                    ranks.add(1)
                sorted_ranks = sorted(ranks)
                for i in range(len(sorted_ranks) - 4):
                    seq = sorted_ranks[i:i+5]
                    if seq[4] - seq[0] == 4 and len(seq) == 5:
                        return True
        return False

    def classify(self):
        if self.has_straight_flush():
            self.label = 'straight flush'
        elif self.has_four_of_a_kind():
            self.label = 'four of a kind'
        elif self.has_full_house():
            self.label = 'full house'
        elif self.has_flush():
            self.label = 'flush'
        elif self.has_straight():
            self.label = 'straight'
        elif self.has_three_of_a_kind():
            self.label = 'three of a kind'
        elif self.has_twopair():
            self.label = 'two pair'
        elif self.has_pair():
            self.label = 'pair'
        else:
            self.label = 'high card'