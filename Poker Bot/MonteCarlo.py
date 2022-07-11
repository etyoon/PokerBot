from random import choice
from cards import Dealer
from hands import Poker

values = {}
values["Highcard"] = 1
values["Two Pair"] = 2
values["Three of a kind"] = 3
values["Straight"] = 4
values["Full House"] = 5
values["Four of a Kind"] = 6
values["Flush"] = 7
values["Straight Flush"] = 8
values["Royal Flush"] = 9


class MonteCarlo:

    def __init__(self, hand):
        self.hand = hand

    def simulation(self):
        sum = 0
        for cards in range(3):
            lst = []
            for i in self.hand:
                lst.append(i)
            while len(lst) < 7:
                lst.append(choice([i for i in range(52) if i not in lst]))
            sim = Poker(lst)
            print(sim.repr_hand())
            hand_str = sim.determine_hand()
            print(hand_str)
            sum += self.ev(hand_str)
        return sum


    def ev(self, tuple):
        total = values.get(tuple[0])
        if isinstance(tuple[1], list):
            total += max(tuple[1]) * .6
            for i in tuple[1]:
                if i != max(tuple[1]):
                    total += i * .1
        elif tuple[0] == "Full House":
            total += (tuple[1][0] *.8) + (tuple[1][1] * .2)
        else:
            total += int(tuple[1]) * .1
        return total * .1

test = Dealer()
test.deal()
sim = MonteCarlo([1,2,4,6,9])
print(sim.simulation())
