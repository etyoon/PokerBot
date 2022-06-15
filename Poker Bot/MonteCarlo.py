from hands import Poker
import random
from cards import Dealer

simulation = Dealer()
simulation.deal()
simulation.hand
for i in range(3):
    simulation.deal()
    simulation.river()
    simulation.flop()
    simulation.turn()
    print(simulation.hand)
