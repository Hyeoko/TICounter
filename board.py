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
        count = 1
        while len(cls.history) != 0 and count < len(cls.history):
            if cls.history[count - 1] != cls.history[count]:
                cls.shoeTI += 1
            else:
                cls.shoeTI -= 1
            count += 1
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
                if i == 5:
                    break
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
