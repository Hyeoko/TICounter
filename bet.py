class Bet:
    base = 1
    theForce = [2, 3, 5, 8]
    theLadder = [2, 1, 2, 3, 4, 5]
    currentBet = 0
    profit = 0

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
        #Save bet on the prep line

    #profit method
    @classmethod
    def bet_result(cls, win):
        if win:
            cls.profit += cls.currentBet
        else:
            cls.profit -= cls.currentBet

