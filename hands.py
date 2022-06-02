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
        flush = False

        for keys in self.suit.keys():
            if self.suit[keys] >= 5:
                flush = True

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
        if len(num_lst) >= 5:
            for i in range(2):
                lst = num_lst[i:5 + i]
                lst = sorted(lst)
                if lst == list(range(min(lst), max(lst) + 1)):
                    if straight == None or straight < lst[-1]:
                        straight = lst[-1]

        if flush and straight != None:
            if straight % 13 == 13:
                return("Royal Flush", straight)
                print(1)
            else:
                return("Straight Flush", straight)
        elif best_quad != None:
            return("Four of a Kind", best_quad)
        elif best_full_house != None:
            return("Full House", best_full_house)
        elif flush:
            return("Flush")
            #have to find way to hold on flush cards to determine higher flush
        elif straight != None:
            return("Straight", straight)
        elif best_trip != None:
            return("Three of a kind", best_trip)
        elif best_pair != None:
            return("Two Pair", best_pair)
        else:
            return("Highcard", max(lst))







test = Poker([13, 12, 11, 10, 9, 8])
test.suits_and_numbers()
print(test.num)
print(test.suit)
test.determine_hand()
