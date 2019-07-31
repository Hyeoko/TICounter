from board import Board
from bet import Bet

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.styles import Alignment

filename = "sample.xlsx"


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
            Bet.placeHistory.append(len(Board.history) + 2)
            Bet.sideHistory.append(self.mySide)
            Bet.amtHistory.append(self.myBet)

    # @staticmethod
    def board_pressed(self, winner):
        last_winner = Board.winner(winner)
        if self.mySide == 'P' or self.mySide == 'B':
            Bet.bet_result(self.mySide == last_winner)
            Bet.profitHistory.append(Bet.profit)
            self.mySide = ''
        # print("My bet: ", self.myBet)
        print(Board.history)
        print("My Profit:", Bet.profit)
        # Bet.reset_current_bet()

    @staticmethod
    def print_worksheet(worksheet):
        board = Board.history
        betPlace = Bet.placeHistory
        betSide = Bet.sideHistory
        betAmt = Bet.amtHistory
        betProfit = Bet.profitHistory

        worksheet["A1"] = "Board"
        worksheet["B1"] = "Bet Side"
        worksheet["C1"] = "Bet Amt"
        worksheet["D1"] = "Profits"

        for i in range(len(board)):
            if board[i] == 'B':
                worksheet.cell(column=1, row=i + 2, value=board[i]).alignment = Alignment(horizontal='right')
            else:
                worksheet.cell(column=1, row=i + 2, value=board[i])
            if i < len(betPlace):
                if betSide[i] == 'B':
                    worksheet.cell(column=2, row=betPlace[i], value=betSide[i]).alignment = Alignment(
                        horizontal='right')
                else:
                    worksheet.cell(column=2, row=betPlace[i], value=betSide[i])
                worksheet.cell(column=3, row=betPlace[i], value=betAmt[i])
                worksheet.cell(column=4, row=betPlace[i], value=betProfit[i])

    def export_to_excel(self):
        try:
            wb = load_workbook(filename=filename)
            ws = wb.create_sheet("newSheet")
            self.print_worksheet(ws)
            wb.save(filename)
        except FileNotFoundError:
            workbook = Workbook()
            worksheet = workbook.active
            self.print_worksheet(worksheet)
            workbook.save(filename)


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