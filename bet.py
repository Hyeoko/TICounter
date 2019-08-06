class Bet:
    base = 1
    theForce = [2, 3, 5, 8]
    theLadder = [2, 1, 2, 3, 4, 5]

    # These lists are used when recording to excel
    placeHistory = []
    sideHistory = []
    amtHistory = []
    profitHistory = []

    currentBet = 0
    totalProfit = 0
    profit = 0

    @classmethod
    def reset(cls):
        cls.placeHistory = []
        cls.sideHistory = []
        cls.amtHistory = []
        cls.profitHistory = []

        cls.currentBet = 0
        cls.totalProfit = 0
        cls.profit = 0

    @classmethod
    def mistake(cls):
        del cls.placeHistory[-1]
        del cls.sideHistory[-1]
        del cls.amtHistory[-1]
        del cls.profitHistory[-1]
        # del cls.profitHistory[-1]

    @classmethod
    def undo_lost_profit(cls):
        if len(cls.profitHistory) > 1:
            cls.profit -= cls.profitHistory[-1] - cls.profitHistory[-2]
        else:
            cls.profit -= cls.profitHistory[-1]

    @classmethod
    def undo_won_profit(cls):
        if len(cls.profitHistory) > 1:
            cls.profit -= cls.profitHistory[-1] - cls.profitHistory[-2]
        else:
            cls.profit -= cls.profitHistory[-1]

    @classmethod
    def profit_reset(cls):
        cls.profit = 0

    # Used for display to sidebar only
    @classmethod
    def total_profit(cls):
        cls.totalProfit += cls.profit
        return cls.totalProfit

    @classmethod
    def base_bet(cls):
        cls.currentBet = cls.base

    @classmethod
    def force_bet(cls, num):
        cls.currentBet = cls.theForce[num]

    @classmethod
    def ladder_bet(cls, num):
        cls.currentBet = cls.theLadder[num]

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
            cls.profit += cls.currentBet
        else:
            cls.profit -= cls.currentBet

