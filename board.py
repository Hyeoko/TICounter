class Board:
    player = 0
    banker = 0
    history = []
    tiHistory = []

    # ind = 1
    # shoeTI = 0
    # inGameTI = 0
    # preTI = 0

    @classmethod
    def reset(cls):
        cls.player = 0
        cls.banker = 0
        cls.history = []

        # cls.ind = 1
        # cls.shoeTI = 0
        cls.inGameTI = 0
        # cls.preTI = 0

    @classmethod
    def mistake(cls):
        cancel = cls.history[-1]
        if cancel == 'P':
            cls.player -= 1
        elif cancel == 'B':
            cls.banker -= 1
        del cls.history[-1]

    @classmethod
    def last_winner(cls):
        return cls.history[-1]

    @classmethod
    def winner(cls, winner):
        if winner == 'P':
            cls.player += 1
            cls.history.append('P')
            cls.tiHistory.append(cls.calc_shoe_ti())
            return 'P'
        elif winner == 'B':
            cls.banker += 1
            cls.history.append('B')
            cls.tiHistory.append(cls.calc_shoe_ti())
            return 'B'


    # Calculate shoe TI
    @classmethod
    def calc_shoe_ti(cls):
        shoe_ti = 0
        if len(cls.history) > 0:
            for i in range(1, len(cls.history)):
                if cls.history[i] != cls.history[i - 1]:
                    shoe_ti += 1
                elif cls.history[i] == cls.history[i - 1]:
                    shoe_ti -= 1
        return shoe_ti

    # Calculate Pre-TI
    @classmethod
    def calc_pre_ti(cls):
        pre_ti = 0
        if len(cls.history) > 5:
            last = cls.history[-1]
            for i in range(2, 6):
                if last != cls.history[-i]:
                    pre_ti += 1
                else:
                    pre_ti -= 1
                if i == 5:
                    break
                last = cls.history[-i]
        return pre_ti

    # This is for stats page
    @classmethod
    def total_player_wins(cls):
        return cls.player

    # same here
    @classmethod
    def total_banker_wins(cls):
        return cls.banker
