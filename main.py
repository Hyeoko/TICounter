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
from openpyxl.styles import Alignment, PatternFill

filename = "sample.xlsx"


class Screen(Widget):
    myBet = ObjectProperty(None) # This is used for Excel
    mySide = ObjectProperty(None)

    total_profit = ObjectProperty(None)
    profit = ObjectProperty(None)
    current_bet = ObjectProperty(None)

    total_wins = ObjectProperty(None)

    shoe_ti = ObjectProperty(None)
    in_game_ti = ObjectProperty(None)
    pre_ti = ObjectProperty(None)

    # @staticmethod
    def bet_pressed(self, bet, ind=None):
        if bet == 'B':
            Bet.base_bet()
            # This base bet indicates that new game is starting
            if len(Bet.profitHistory) != 0:
                Bet.profit_reset()
                self.total_profit.text = 'Total Profit: ' + str(Bet.total_profit())
                self.profit.text = 'Current Profit: ' + str(Bet.profit)
            self.myBet = 'B'
            self.current_bet.text = 'Betting: B'
        elif bet == "F":
            Bet.force_bet(ind)
            self.myBet = 'F' + str(Bet.get_current_bet())
            self.current_bet.text = 'Betting: F' + str(Bet.get_current_bet())
        elif bet == "L":
            Bet.ladder_bet(ind)
            self.myBet = 'L' + str(Bet.get_current_bet())
            self.current_bet.text = 'Betting: L' + str(Bet.get_current_bet())
        else:
            pass

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
            self.profit.text = 'Current Profit: ' + str(Bet.profit)
            self.mySide = ''

        self.total_wins.text = 'P: ' + str(Board.player) + '     ' + 'B: ' + str(Board.banker)

        self.shoe_ti.text = 'Shoe TI: ' + str(Board.calc_shoe_ti())
        self.pre_ti.text = 'Pre-TI: ' + str(Board.calc_pre_ti())
        # print("My bet: ", self.myBet)
        print(Board.history)
        print("My Profit:", Bet.profit)
        # Bet.reset_current_bet()

    # @staticmethod
    def print_worksheet(self, worksheet):
        board = Board.history
        bet_place = Bet.placeHistory
        bet_side = Bet.sideHistory
        bet_amt = Bet.amtHistory
        bet_profit = Bet.profitHistory

        worksheet["A1"] = "ShoeTI"
        worksheet["B1"] = "PreTI"
        worksheet["C1"] = "Board"
        worksheet["D1"] = "Bet Side"
        worksheet["E1"] = "Bet Amt"
        worksheet["F1"] = "Profits"

        banker_fill = PatternFill(start_color='FFFF0000', end_color='FFFF0000', fill_type='solid')
        player_fill = PatternFill(start_color='FF0000FF', end_color='FF0000FF', fill_type='solid')

        for i in range(len(board)):
            # worksheet.cell(column=1, row=i + 2, value=self.shoeTi)
            # worksheet.cell(column=2, row=i + 2, value=self.preTi)

            board_cell = worksheet.cell(column=3, row=i + 2, value=board[i])
            if board[i] == 'B':
                board_cell.alignment = Alignment(horizontal='right')
                board_cell.fill = banker_fill
            else:
                board_cell.fill = player_fill
            if i < len(bet_place):
                if bet_side[i] == 'B':
                    worksheet.cell(column=4, row=bet_place[i], value=bet_side[i]).alignment = \
                        Alignment(horizontal='right')
                else:
                    worksheet.cell(column=4, row=bet_place[i], value=bet_side[i])
                worksheet.cell(column=5, row=bet_place[i], value=bet_amt[i]).alignment = Alignment(horizontal='right')
                worksheet.cell(column=6, row=bet_place[i], value=bet_profit[i])

    def export_to_excel(self):

        # When filename already exist
        try:
            wb = load_workbook(filename=filename)
            ws = wb.create_sheet("Sheet")
            self.print_worksheet(ws)
            wb.save(filename)
        # Create new file
        except FileNotFoundError:
            workbook = Workbook()
            worksheet = workbook.active
            self.print_worksheet(worksheet)
            workbook.save(filename)


class TICounterApp(App):
    title = "TICounter"

    def build(self):
        self.root = Screen()
        return self.root


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