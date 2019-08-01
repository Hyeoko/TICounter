class Board:
    player = 0
    banker = 0
    history = []

    ind = 1
    shoeTI = 0
    inGameTI = 0
    preTI = 0

    @classmethod
    def last_winner(cls):
        return cls.history[-1]

    @classmethod
    def winner(cls, winner):
        if winner == 'P':
            cls.player += 1
            cls.history.append('P')
            # Scroll to new line
            # Show player win circle
            return 'P'
        elif winner == 'B':
            cls.banker += 1
            cls.history.append('B')
            # Scroll to new line
            # Show banker win circle
            return 'B'
        pass

    # Calculate shoe TI
    @classmethod
    def calc_shoe_ti(cls):
        if len(cls.history) > 1:
            if cls.history[cls.ind] != cls.history[cls.ind - 1]:
                cls.shoeTI += 1
                cls.ind += 1
            elif cls.history[cls.ind] == cls.history[cls.ind - 1]:
                cls.shoeTI -= 1
                cls.ind += 1
        return cls.shoeTI

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
