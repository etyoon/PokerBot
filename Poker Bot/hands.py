import random
from cards import Dealer
'''

'''

card = {}
value_lst = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J','Q', 'K', 'A']
key = 0
for i in range(52):
    card[i] = value_lst[key]
    if key < 12:
        key += 1
    else:
        key = 0

class Poker:

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

    def is_straight(self, hand):
        '''
        deteremines if there is a straight on the board
        hand: lst of numbers on the board
        '''
        straight = None
        if len(hand) >= 5:
            for i in range(3):
                lst = hand[i:5 + i]
                lst = sorted(lst)
                if lst == list(range(min(lst), max(lst) + 1)):
                    if len(lst) == 5:
                        if straight == None or straight < lst[-1]:
                            straight = lst[-1]
                elif lst[:4] == [0, 1, 2, 3]:
                    if 12 in hand:
                        if straight == None:
                            straight = lst[3]
        return straight


    def determine_hand(self):
        '''
        given a seven card hand determines highest hand
        '''
        flush = False

        for keys in self.suit.keys():
            if self.suit[keys] >= 5:
                flush = True
                suit = keys

        best_pair = None
        best_trip = None
        best_quad = None
        best_full_house = None
        for keys, values in self.num.items():
            if values == 2:
                if best_pair == None or best_pair < keys:
                    best_pair = keys
            if values == 3:
                if best_trip == None or best_trip < keys:
                    best_trip = keys
            if values == 4:
                if best_trip == None or best_quad < keys:
                    best_quad = keys
            if best_trip != None and best_pair != None:
                best_full_house = (best_trip, best_pair)

        straight = None
        num_lst = []
        for keys in self.num.keys():
            num_lst.append(keys)
        straight = self.is_straight(num_lst)

        rv = []
        if flush:
            nums = [i for i in self.hand if i // 13 == suit]
            straight_flush = self.is_straight(nums)
            if straight_flush != None:
                if straight_flush % 13 == 12:
                    return("Royal Flush")
                else:
                    return("Straight Flush", card.get(straight_flush))
            else:
                for i in nums:
                    rv.append(card.get(i))
                return ("Flush", rv)
        elif best_quad != None:
            return("Four of a Kind", card.get(best_quad))
        elif best_full_house != None:
            full, house = best_full_house
            return("Full House", (card.get(full), card.get(house)))
        elif straight != None:
            return("Straight", card.get(straight))
        elif best_trip != None:
            return("Three of a kind", card.get(best_trip))
        elif best_pair != None:
            return("Two Pair", card.get(best_pair))
        else:
            return("Highcard", card.get(max(num_lst)))

test = Dealer()
test.deal()
test.river()
test.flop()
test.turn()
trial = Poker(test.hand)
trial.suits_and_numbers()
print(trial.suit)
print(trial.num)
print(trial.determine_hand())
