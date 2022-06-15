from random import choice

class Dealer:

    def __init__(self):
        self.hand = []
        self.deal = False
        self.river = False
        self.flop = False
        self.turn = False

    def deal(self):
        for cards in range(2):
            self.hand.append(choice([i for i in range(52)]))
        self.deal = True

    def river(self):
        for cards in range(3):
            self.hand.append(choice([i for i in range(52) if i not in self.hand]))
        self.river = True

    def flop(self):
        self.hand.append(choice([i for i in range(52) if i not in self.hand]))
        self.flop = True

    def turn(self):
        self.hand.append(choice([i for i in range(52) if i not in self.hand]))
        self.turn = True
