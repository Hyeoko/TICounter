from board import Board
from bet import Bet

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class Screen(Widget):
    myBet = ObjectProperty(None)
    mySide = ObjectProperty(None)

    # @staticmethod
    def bet_pressed(self, bet, ind=None):
        if bet == 'B':
            Bet.base_bet()
        elif bet == "F":
            Bet.force_bet(ind)
        elif bet == "L":
            Bet.ladder_bet(ind)
        else:
            pass
        self.myBet = Bet.get_current_bet()
        print("Current Bet:", Bet.get_current_bet())

    def bet_side(self, side):
        if self.myBet is None:
            print("You must pick your bet amount!")
        else:
            self.mySide = Bet.bet_side(side)

    # @staticmethod
    def board_pressed(self, winner):
        last_winner = Board.winner(winner)
        if self.mySide == 'P' or self.mySide == 'B':
            Bet.bet_result(self.mySide == last_winner)
            self.mySide = ''
        # print("My bet: ", self.myBet)
        print(Board.history)
        print("My Profit:", Bet.profit)
        # Bet.reset_current_bet()


class TICounterApp(App):
    def build(self):
        return Screen()


if __name__ == "__main__":
    TICounterApp().run()
#
# Bet.base_bet()
#
# while True:
#     myBet = ''
#     if random.random() < 0.5:
#         myBet = Bet.bet_player()
#     else:
#         myBet = Bet.bet_banker()
#
#     if random.random() < 0.5:
#         Board.player_win()
#         Bet.bet_result(Board.player_win() == myBet)
#         # if Board.player_win() == myBet:
#         #     Bet.bet_result(True)
#         # else:
#         #     Bet.bet_result(False)
#     else:
#         Board.banker_win()
#         Bet.bet_result(Board.player_win() == myBet)
#         # if Board.banker_win() == myBet:
#         #     Bet.bet_result(True)
#         # else:
#         #     Bet.bet_result(False)
#
#     if len(Board.history) > 50:
#         break
#
# print(Board.history)
# print("Shoe TI:", Board.calc_shoe_ti())
# print("Pre-TI:", Board.calc_pre_ti())
#
# print("My Profit:", Bet.profit)