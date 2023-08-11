import random
import time

class Player_1():
    ...
class Player_2():
    ...

def main():
    p1_deck, p2_deck = deck_dealer()
    while len(p1_deck) or len(p2_deck) != 52:
        if base_move(p1_deck, p2_deck) == True:
            ... #Goes into war and war_move
        else:
            continue

#Performs the base move of a card draw and comparison of values.
def base_move(p1_deck, p2_deck):
    p1_card = p1_deck[0]
    p2_card = p2_deck[0]
    print(f"Player 1 has drawn {p1_card}.")
    print(f"Player 2 has drawn {p2_card}.")
    p2_deck.remove(p2_card)
    p1_deck.remove(p1_card)


    for rank, strenght in card_comprehension().items():
        if rank == p1_card.rstrip("cdhs"):
            p1_str = strenght
        if rank == p2_card.rstrip("cdhs"):
            p2_str = strenght

    return round_resolution_check(p1_str, p2_str, p1_card, p2_card, p1_deck, p2_deck)


def round_resolution_check(p1_str, p2_str, p1_card, p2_card, p1_deck, p2_deck):
    if isinstance(strength_comparison(p1_str, p2_str, p1_card, p2_card, p1_deck, p2_deck), bool):
        return True
    else:
        p1_deck, p2_deck = strength_comparison(p1_str, p2_str, p1_card, p2_card, p1_deck, p2_deck)
        return p1_deck, p2_deck

def strength_comparison(p1_str, p2_str, p1_card, p2_card, p1_deck, p2_deck):
    time.sleep(2)
    if p1_str > p2_str:
        p1_deck.append(p1_card)
        p1_deck.append(p2_card)
        print(f"Player 1 has won this round. They have taken {p1_card} and {p2_card}.")
        print(f"Player 1 has {len(p1_deck)} cards left. Player 2 has {len(p2_deck)}.")
        return p1_deck, p2_deck
    elif p2_str > p1_str:
        p2_deck.append(p2_card)
        p2_deck.append(p1_card)
        print(f"Player 2 has won this round. They have taken {p2_card} and {p1_card}.")
        print(f"Player 2 has {len(p2_deck)} cards left. Player 2 has {len(p1_deck)}.")
        return p1_deck, p2_deck
    elif p1_str == p2_str:
        print("War!")
        return True


def deck_dealer():
    deck = ["Ac", "Ad", "Ah", "As", "2c", "2d", "2h", "2s", "3c", "3d", "3h", "3s",
        "4c", "4d", "4h", "4s", "5c", "5d", "5h", "5s", "6c", "6d", "6h", "6s",
        "7c", "7d", "7h", "7s", "8c", "8d", "8h", "8s", "9c", "9d", "9h", "9s",
        "10c", "10d", "10h", "10s", "Jc", "Jd", "Jh", "Js", "Qc", "Qd", "Qh", "Qs",
        "Kc", "Kd", "Kh", "Ks"]
    p1_deck = []
    p2_deck = []

    for c in range(len(deck)):
        if len(deck) > 0:
            p1_pick = random.choice(deck)
            p1_deck.append(p1_pick)
            deck.remove(p1_pick)

            p2_pick = random.choice(deck)
            p2_deck.append(p2_pick)
            deck.remove(p2_pick)

    return p1_deck, p2_deck

def card_comprehension():
    card_relation = {"2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6,
                     "8": 7, "9": 8, "10": 9, "J": 10, "Q": 11, "K": 12, "A": 13}

    return card_relation

if __name__ == "__main__":
    main()