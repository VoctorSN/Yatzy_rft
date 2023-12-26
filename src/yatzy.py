from src.pips import Pips

class Yatzy:

    # No es necesario.
    # Lo mantengo para no romper la interfaz
    # publica de la clase segun los
    # casos test originales.
    def __init__(self, *dice):
        self.dice = list(dice)

    @staticmethod
    def chance(*dice):
        return sum(dice)

    @staticmethod
    def yatzy(*dice):
        return (50 if dice.count(dice[0]) == len(dice) else 0)
    
    @staticmethod
    def ones(*dice):
        return dice.count(1)

    @staticmethod
    def twos(*dice):
        return dice.count(2) * 2

    @staticmethod
    def threes(*dice):
        return dice.count(3) * 3

    def fours(self):
        return self.dice.count(4) * 4

    def fives(self):
        return self.dice.count(5) * 5

    def sixes(self):
        return self.dice.count(6) * 6

    @staticmethod
    def pair(*dice):
        for pip in Pips.reversedValues():
            if dice.count(pip >= 2):
                return 2*pip
        return 0
    
    @classmethod
    def two_pairs(cls, *dice):
        return sum(cls.__filter_pips_repeated(dice, 2)) * 2 if len(cls.__filter_pips_repeated(dice, 2)) == 2 else 0

    @classmethod
    def three_of_a_kind(cls, *dice):
        return cls.__biggest_pip_repeated(dice, 3) * 3 if dice.count(cls.__biggest_pip_repeated(dice, 3))>=3 else 0

    @classmethod
    def four_of_a_kind(cls, *dice):
        return cls.__biggest_pip_repeated(dice, 4) * 4 if dice.count(cls.__biggest_pip_repeated(dice, 4))>=4 else 0

    @classmethod
    def __biggest_pip_repeated(cls, dice, times):
        pips = cls.__filter_pips_repeated(dice, times)
        return pips[0] if pips else []

    @classmethod
    def __filter_pips_repeated(cls, dice, times):
        return list(filter(lambda pip: dice.count(pip) >= times, Pips.reversedValues()))

    @classmethod
    def small_straight(cls, *dice):
        return cls.chance(*dice) if not Pips.minus(Pips.SIX) - set(dice) else 0

    @classmethod
    def large_straight(cls, *dice):
        return cls.chance(*dice) if not Pips.minus(Pips.ONE) - set(dice) else 0

    @classmethod
    def fullHouse(cls, *dice):
        if cls.two_of_a_kind(*dice) and cls.three_of_a_kind(*dice):
            return cls.two_of_a_kind(*dice) + cls.three_of_a_kind(*dice)
        else:
            return 0

    @classmethod
    def two_of_a_kind(cls, *dice):
        PAIR = 2
        for pip in Pips.reversedValues():
            if dice.count(pip) == PAIR:
                return PAIR * pip
        return 0
