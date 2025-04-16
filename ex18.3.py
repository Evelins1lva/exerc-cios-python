from Card import Card, Deck
from PokerHand import PokerHand

def main():
    # Simulação de 10.000 mãos de pôquer
    simulate(10000)

def simulate(n=10000):
    counts = {}
    for _ in range(n):
        # Cria o baralho e embaralha
        deck = Deck()
        deck.shuffle()

        # Da as cartas para a mão
        hand = PokerHand()
        hand.add_cards(deck.deal(7))  # Distribuindo 7 cartas

        # Classifica a mão
        hand.classify()

        # Conta as classificações
        label = hand.label
        counts[label] = counts.get(label, 0) + 1

    # Exibe as probabilidades das classificações
    for label in sorted(counts, key=lambda x: counts[x], reverse=True):
        freq = counts[label] / n
        print(f'{label:20s}: {freq:.4f}')


if __name__ == "__main__":
    main()
