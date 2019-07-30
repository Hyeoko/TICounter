class Board:
    player = 0
    banker = 0
    history = []

    shoeTI = 0
    inGameTI = 0
    preTI = 0

    @classmethod
    def last_winner(cls):
        return cls.history[-1]

    @classmethod
    def player_win(cls):
        cls.player += 1
        cls.history.append('P')
        # Scroll to new line
        # Show player win circle
        return 'P'

    @classmethod
    def banker_win(cls):
        cls.banker += 1
        cls.history.append('B')
        # Scroll to new line
        # Show banker win circle
        return 'B'

    # Calculate shoe TI
    @classmethod
    def calc_shoe_ti(cls):
        if len(cls.history) != 0:
            if cls.history[-2] != cls.history[-1]:
                cls.shoeTI += 1
            else:
                cls.shoeTI -= 1
        return cls.shoeTI

    # Calculate Pre-TI
    @classmethod
    def calc_pre_ti(cls):
        if len(cls.history) > 5:
            last = cls.history[-1]
            for i in range(2, 6):
                if last != cls.history[-i]:
                    cls.preTI += 1
                else:
                    cls.preTI -= 1
                last = cls.history[-i]
        return cls.preTI

    # This is for stats page
    @classmethod
    def total_player_wins(cls):
        return cls.player

    # same here
    @classmethod
    def total_banker_wins(cls):
        return cls.banker
