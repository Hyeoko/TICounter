from board import Board
from bet import Bet
import random


Bet.base_bet()

while True:
    myBet = ''
    if random.random() < 0.5:
        myBet = Bet.bet_player()
    else:
        myBet = Bet.bet_banker()

    if random.random() < 0.5:
        Board.player_win()
        if Board.player_win() == myBet:
            Bet.bet_result(True)
        else:
            Bet.bet_result(False)
    else:
        Board.banker_win()
        if Board.banker_win() == myBet:
            Bet.bet_result(True)
        else:
            Bet.bet_result(False)

    if len(Board.history) > 50:
        break

print(Board.history)
print("Shoe TI:", Board.calc_shoe_ti())
print("Pre-TI:", Board.calc_pre_ti())

print("My Profit:", Bet.profit)