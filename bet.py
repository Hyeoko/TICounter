class Bet:
    base = 1
    theForce = [2, 1, 2, 3, 3]
    theForceText = ['F2', 'xB', 'xF2', 'F3', 'xF3']
    theLadder = 2

    # These lists are used when recording to excel
    placeHistory = []
    sideHistory = []
    amtHistory = []
    profitHistory = []
    endMicroGameHistory = []

    currentBet = 0
    micro_game_profit = 0
    moneyCount = 0

    @classmethod
    def reset(cls):
        cls.placeHistory = []
        cls.sideHistory = []
        cls.amtHistory = []
        cls.profitHistory = []

        cls.currentBet = 0
        cls.micro_game_profit = 0
        cls.moneyCount = 0

    @classmethod
    def mistake(cls):
        del cls.placeHistory[-1]
        del cls.sideHistory[-1]
        del cls.amtHistory[-1]
        del cls.profitHistory[-1]

    @classmethod
    def undo_profit(cls):
        if len(cls.profitHistory) > 1:
            takeout = cls.profitHistory[-1] - cls.profitHistory[-2]
            cls.micro_game_profit -= takeout
            cls.moneyCount -= takeout
        elif len(cls.profitHistory) == 1:
            cls.micro_game_profit -= cls.profitHistory[-1]
            cls.moneyCount -= cls.profitHistory[-1]

    @classmethod
    def profit_reset(cls):
        cls.micro_game_profit = 0
        cls.endMicroGameHistory.append(len(cls.profitHistory) - 1)

    # # Used for display to sidebar only
    # @classmethod
    # def total_profit(cls):
    #     cls.totalProfit += cls.micro_game_profit
    #     return cls.totalProfit

    @classmethod
    def base_bet(cls):
        cls.currentBet = cls.base

    @classmethod
    def force_bet(cls, num):
        cls.currentBet = cls.theForce[num]

    @classmethod
    def ladder_bet(cls):
        cls.currentBet = cls.theLadder

    @classmethod
    def get_current_bet(cls):
        return cls.currentBet

    @classmethod
    def reset_current_bet(cls):
        cls.currentBet = 0

    @classmethod
    def bet_side(cls, side):
        if side == 'P':
            return 'P'
        elif side == 'B':
            return 'B'
        return ''

    # Profit method
    @classmethod
    def bet_result(cls, win):
        if win:
            cls.micro_game_profit += cls.currentBet
            cls.moneyCount += cls.currentBet
        else:
            cls.micro_game_profit -= cls.currentBet
            cls.moneyCount -= cls.currentBet
        return win
