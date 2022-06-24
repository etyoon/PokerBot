from hands import Poker
import random
from cards import Dealer

start = Dealer()
start.deal()
start.hand
for i in range(3):
    simulation.hand = start.hand
    if start.river:
        simulation.river()
    if start.flop:
        simulation.flop()
    if start.turn:
        simulation.turn()
    simulation = Dealer()
