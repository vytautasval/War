import random
import time

class WarGame:
    def __init__(self):
        self.deck = []
        self.p1_deck = []
        self.p2_deck = []

    def initialize_deck(self):
        self.deck = ["Ac", "Ad", "Ah", "As", "2c", "2d", "2h", "2s", "3c", "3d", "3h", "3s",
                    "4c", "4d", "4h", "4s", "5c", "5d", "5h", "5s", "6c", "6d", "6h", "6s",
                    "7c", "7d", "7h", "7s", "8c", "8d", "8h", "8s", "9c", "9d", "9h", "9s",
                    "10c", "10d", "10h", "10s", "Jc", "Jd", "Jh", "Js", "Qc", "Qd", "Qh", "Qs",
                    "Kc", "Kd", "Kh", "Ks"]
    def deal_cards(self):
        while self.deck:
            p1_pick = random.choice(self.deck)
            self.p1_deck.append(p1_pick)
            self.deck.remove(p1_pick)

            p2_pick = random.choice(self.deck)
            self.p2_deck.append(p2_pick)
            self.deck.remove(p2_pick)

        return self.p1_deck, self.p2_deck

    def calculate_strength(self, card):
        card_relation = {"2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6,
                         "8": 7, "9": 8, "10": 9, "J": 10, "Q": 11, "K": 12, "A": 13}

        return card_relation[card[:-1]]

    def base_move(self):
        p1_card = self.p1_deck[0]
        p2_card = self.p2_deck[0]
        print(f"Player 1 has drawn {p1_card}.")
        print(f"Player 2 has drawn {p2_card}.")
        self.p2_deck.remove(p2_card)
        self.p1_deck.remove(p1_card)

        p1_str = self.calculate_strength(p1_card)
        p2_str = self.calculate_strength(p2_card)

        time.sleep(2)
        if p1_str > p2_str:
            self.p1_deck.append(p1_card)
            self.p1_deck.append(p2_card)
            print(f"Player 1 has won this round. They have taken {p1_card} and {p2_card}.")
            print(f"Player 1 has {len(self.p1_deck)} cards left. Player 2 has {len(self.p2_deck)}.")
            return self.p1_deck, self.p2_deck
        elif p2_str > p1_str:
            self.p2_deck.append(p2_card)
            self.p2_deck.append(p1_card)
            print(f"Player 2 has won this round. They have taken {p2_card} and {p1_card}.")
            print(f"Player 2 has {len(self.p2_deck)} cards left. Player 1 has {len(self.p1_deck)}.")
            return self.p1_deck, self.p2_deck
        elif p1_str == p2_str:
            print("War!")
            return True

def main():
    card_game = WarGame()
    card_game.initialize_deck()

    p1_deck, p2_deck = card_game.deal_cards()

    while len(p1_deck) or len(p2_deck) != 52:
        result = card_game.base_move()
        if result == True:
            ... #Goes into war and war_move
        else:
            continue

if __name__ == "__main__":
    main()