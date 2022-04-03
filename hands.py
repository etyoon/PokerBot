import random

deck = [i for i in range(52)]

random.seed(5)

random.shuffle(deck)


def suits_and_numbers(hand):
    '''
    given a five card hand determines number of cards and suits
    '''
    num = {}
    suit = {}
    for card in hand:
        num[card % 13]=num.get(card % 13, 0) + 1
        suit[card // 13]=suit.get(card // 13, 0) + 1
    return(num, suit)



def hands(hand):
    '''
    given a five card hand, determine what you have
    '''
    
