import random

class Poker:

    deck = [i for i in range(52)]

    random.seed(5)

    random.shuffle(deck)

    def __init__(self, hand):
        self.hand = hand
        self.suit = {}
        self.num = {}

    def suits_and_numbers(self):
        '''
        given a five card hand determines number of cards and suits
        '''

        for card in self.hand:
            self.num[card % 13]=self.num.get(card % 13, 0) + 1
            self.suit[card // 13]=self.suit.get(card // 13, 0) + 1

    def what_hand(self):
        for nums in self.num:
            if 

test = Poker([5, 5+ 13, 2])
test.suits_and_numbers()
print(test.num)
