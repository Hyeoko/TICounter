class Board:
    player = 0
    banker = 0
    history = []
    tiHistory = []
    shoe_ti = 0

    # Resets the board for new game(shoe)
    @classmethod
    def reset(cls):
        cls.player = 0
        cls.banker = 0
        cls.history = []
        cls.tiHistory = []
        cls.shoe_ti = 0

    # Deletes last history
    @classmethod
    def mistake(cls):
        cancel = cls.history[-1]
        if cancel == 'P':
            cls.player -= 1
        elif cancel == 'B':
            cls.banker -= 1
        del cls.history[-1]
        del cls.tiHistory[-1]
        if len(cls.history) > 0:
            if cancel == cls.history[-1]:
                cls.shoe_ti += 1
            else:
                cls.shoe_ti -= 1

    # Gets the last winner
    @classmethod
    def last_winner(cls):
        return cls.history[-1]

    # Records to board the winner of the round
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

    # Update the shoe TI and return it
    @classmethod
    def calc_shoe_ti(cls):
        if len(cls.history) > 1:
            if cls.history[-2] == cls.history[-1]:
                cls.shoe_ti -= 1
            else:
                cls.shoe_ti += 1
        return cls.shoe_ti

    # Calculate Pre-TI
    @classmethod
    def calc_pre_ti(cls):
        pre_ti = 0
        if len(cls.history) > 4:
            last = cls.history[-1]
            for i in range(2, 6):
                if last != cls.history[-i]:
                    pre_ti += 1
                else:
                    pre_ti -= 1
                if i == 5:
                    break
                last = cls.history[-i]
        else:
            return 'None'
        return pre_ti

    # This is for stats page
    @classmethod
    def total_player_wins(cls):
        return cls.player

    # same here
    @classmethod
    def total_banker_wins(cls):
        return cls.banker
