import random

class Player_1():
    ...
class Player_2():
    ...

def main():
    p1_deck, p2_deck = deck_dealer()
    while len(p1_deck) or len(p2_deck) != 52:
        if card_turner ==

def base_move(p1_deck, p2_deck):
    p1_card = p1_deck[0]
    p2_card = p2_deck[0]
    p2_deck.remove(p2_card)
    p1_deck.remove(p1_card)

    p1_str = 0
    p2_str = 0
    for rank, strenght in card_comprehension().items():
        if rank == p1_card.rstrip(["c", "d", "h", "s"]):
            p1_str = strenght
            break
        if rank == p2_card.rstrip(["c", "d", "h", "s"]):
            p2_str = strenght
            break

    strength_comparison(p1_str, p2_str, p1_card, p2_card, p1_deck, p2_deck)

def strength_comparison(p1_str, p2_str, p1_card, p2_card, p1_deck, p2_deck):
    if p1_str > p2_str:
        p1_deck.append(p1_card, p2_card)
        return p1_deck, p2_deck
    elif p2_str > p1_str:
        p2_deck.append(p2_card, p1_card)
        return p1_deck, p2_deck
    elif p1_str == p2_str:
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