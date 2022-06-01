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
        given a seven card hand determines number of cards with same suit
        and or number
        '''

        for card in self.hand:
            self.num[card % 13]=self.num.get(card % 13, 0) + 1
            self.suit[card // 13]=self.suit.get(card // 13, 0) + 1

    def determine_hand(self):
        '''
        given a seven card hand determines highest hand
        '''

        


test = Poker([1,2,3,4,5])
test.suits_and_numbers()
print(test.num)
print(test.suit)
