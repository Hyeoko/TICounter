from board import Board
from bet import Bet

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.styles import Alignment, PatternFill

filename = "Practice.xlsx"


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

    board = ObjectProperty(None)

    def reset(self):
        Bet.reset()
        Board.reset()
        self.myBet = ''
        self.mySide = ''
        self.total_profit.text = "Total Profit: 0"
        self.profit.text = "Current Profit: 0"
        self.current_bet.text = "Betting: ?"
        self.total_wins.text = "P: 0     B: 0"
        self.shoe_ti.text = "Shoe TI: 0"
        self.in_game_ti.text = "In-Game TI: 0"
        self.pre_ti.text = "Pre-TI: 0"
        self.board.text = ''

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
            self.current_bet.text = 'B betting'
        elif bet == "F":
            Bet.force_bet(ind)
            self.myBet = 'F' + str(Bet.get_current_bet())
            self.current_bet.text = 'F' + str(Bet.get_current_bet()) + ' betting'
        elif bet == "L":
            Bet.ladder_bet(ind)
            self.myBet = 'L' + str(Bet.get_current_bet())
            self.current_bet.text = 'L' + str(Bet.get_current_bet()) + ' betting'
        else:
            pass
        print("Current Bet: ", Bet.currentBet)

    def bet_side(self, side):
        if self.myBet is None:
            print("You must pick your bet amount!")
        elif side == 'c':
            self.mySide = ''
            self.current_bet.text = self.myBet + ' betting '
            Bet.mistake()
        else:
            self.mySide = Bet.bet_side(side)
            self.current_bet.text += ' ' + side

    # @staticmethod
    def board_pressed(self, winner):
        last_winner = Board.winner(winner)

        # If bet was placed
        if self.mySide == 'P' or self.mySide == 'B':
            Bet.bet_result(self.mySide == last_winner)
            Bet.placeHistory.append(len(Board.history) + 2)
            Bet.sideHistory.append(self.mySide)
            Bet.amtHistory.append(self.myBet)
            Bet.profitHistory.append(Bet.profit)
            self.profit.text = 'Current Profit: ' + str(Bet.profit)
            self.mySide = ''

        # Stats on the sidebar
        self.total_wins.text = 'P: ' + str(Board.player) + '     ' + 'B: ' + str(Board.banker)

        self.shoe_ti.text = 'Shoe TI: ' + str(Board.calc_shoe_ti())
        self.pre_ti.text = 'Pre-TI: ' + str(Board.calc_pre_ti())

        # Print on ScrollView
        if last_winner == 'P':
            self.board.text += '\n   ' + last_winner
        elif last_winner == 'B':
            self.board.text += '\n                ' + last_winner

        print('Place History: ')
        print(Bet.placeHistory)
        print('Side History: ')
        print(Bet.sideHistory)
        print('Amount History: ')
        print(Bet.amtHistory)
        print('Profit History:')
        print(Bet.profitHistory)
        print("Current Bet:", Bet.currentBet)
        print('-'*20)

    def mistake(self):
        # Deletes last winner from ScrollView
        self.board.text = self.board.text.rstrip('BP')
        self.board.text = self.board.text.rstrip()

        last_bet = Bet.sideHistory[-1]

        Board.mistake()

        # Undo last betting and profit make/lost from it
        if len(Bet.placeHistory) != 0 and Bet.placeHistory[-1] == len(Board.history) + 3:
            self.mySide = last_bet
            if Bet.profitHistory[-1] > Bet.profitHistory[-2]:
                Bet.undo_won_profit()
            elif Bet.profitHistory[-1] < Bet.profitHistory[-2]:
                Bet.undo_lost_profit()
            Bet.mistake()
            self.profit.text = 'Current Profit: ' + str(Bet.profit)

            print('Place History: ')
            print(Bet.placeHistory)
            print('Side History: ')
            print(Bet.sideHistory)
            print('Amount History: ')
            print(Bet.amtHistory)
            print('Profit History:')
            print(Bet.profitHistory)
            print("Current Bet:", Bet.currentBet)
            print('-' * 20)

            # Bet.placeHistory.append(len(Board.history) + 2)
            # Bet.sideHistory.append(self.mySide)
            # Bet.amtHistory.append(self.myBet)


    @staticmethod
    def print_worksheet(worksheet):
        board = Board.history
        bet_place = Bet.placeHistory
        bet_side = Bet.sideHistory
        bet_amt = Bet.amtHistory
        bet_profit = Bet.profitHistory

        # worksheet["A1"] = "ShoeTI"
        # worksheet["B1"] = "PreTI"
        worksheet["A1"] = "Board"
        worksheet["B1"] = "Bet Side"
        worksheet["C1"] = "Bet Amt"
        worksheet["D1"] = "Profits"

        banker_fill = PatternFill(start_color='FFFF0000', end_color='FFFF0000', fill_type='solid')
        player_fill = PatternFill(start_color='FF0000FF', end_color='FF0000FF', fill_type='solid')

        for i in range(len(board)):
            # worksheet.cell(column=1, row=i + 2, value=self.shoeTi)
            # worksheet.cell(column=2, row=i + 2, value=self.preTi)

            board_cell = worksheet.cell(column=1, row=i + 2, value=board[i])
            if board[i] == 'B':
                board_cell.alignment = Alignment(horizontal='right')
                board_cell.fill = banker_fill
            else:
                board_cell.fill = player_fill
            if i < len(bet_place):
                if bet_side[i] == 'B':
                    worksheet.cell(column=2, row=bet_place[i], value=bet_side[i]).alignment = \
                        Alignment(horizontal='right')
                else:
                    worksheet.cell(column=2, row=bet_place[i], value=bet_side[i])
                worksheet.cell(column=3, row=bet_place[i], value=bet_amt[i]).alignment = Alignment(horizontal='right')
                worksheet.cell(column=4, row=bet_place[i], value=bet_profit[i])

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