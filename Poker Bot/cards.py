from random import choice

class Dealer:

    def __init__(self):
        self.hand = []

    def deal(self):
        for cards in range(2):
            self.hand.append(choice([i for i in range(52) if i not in self.hand]))

    def river(self):
        for cards in range(3):
            self.hand.append(choice([i for i in range(52) if i not in self.hand]))

    def flop(self):
        self.hand.append(choice([i for i in range(52) if i not in self.hand]))

    def turn(self):
        self.hand.append(choice([i for i in range(52) if i not in self.hand]))
