import random

suit_priority = {
    "heart": 0,
    "diamond": 1,
    "club": 2,
    "spade": 3
}

value_priority = {
    "2": 0, "3": 1, "4": 2, "5": 3, "6": 4,
    "7": 5, "8": 6, "9": 7, "10": 8,
    "J": 9, "Q": 10, "K": 11, "A": 12
}

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        suits = ["heart", "diamond", "club", "spade"]
        self.cards = [Card(value, suit) for suit in suits for value in values]
    def shuffle(self):
        if self.cards == []:
            raise ValueError("Bộ bài trống!")
        else:
            random.shuffle(self.cards)
    def deal_a_card(self):
        if self.cards == []:
            raise ValueError("Bộ bài trống!")
        else:
            return self.cards.pop()
    def sort(self):
        self.cards.sort(
        key=lambda card: (
            suit_priority[card.suit],
            value_priority[card.value]
        )
    )
    def __str__(self):
        return ", ".join(str(card) for card in self.cards)
        
if __name__ == "__main__":
    deck = Deck()
    print("Bộ bài ban đầu:")
    print(deck)

    print("Đang xáo bài...")
    deck.shuffle()
    print(deck)

    print("Rút một lá bài:")
    card = deck.deal_a_card()
    print(f"Bạn rút được: {card}")

    print("Sắp xếp lại bộ bài...")
    deck.sort()
    print(deck)