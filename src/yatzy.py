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
        return 50 if (len(dice) == 1 and sorted(dice[0])[0] == sorted(dice[0])[-1]) or (len(dice) > 1 and sorted(dice)[0] == sorted(dice)[-1]) else 0
        
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
        return max([x for x in set(dice) if dice.count(x) >= 2], default=0) * 2
    
    @classmethod
    def two_pairs(cls, *dice):
        return sum(cls.__filter_pips_repeated(dice, 2)) * 2 if len(cls.__filter_pips_repeated(dice, 2)) == 2 else 0

    @classmethod
    def three_of_a_kind(cls, *dice):
        return cls.__biggest_pip_repeated(dice, 3) * 3 if dice.count(cls.__biggest_pip_repeated(dice, 3)) >= 3 else 0

    @classmethod
    def four_of_a_kind(cls, *dice):
        return cls.__biggest_pip_repeated(dice, 4) * 4 if dice.count(cls.__biggest_pip_repeated(dice, 4)) >= 4 else 0

    @classmethod
    def __biggest_pip_repeated(cls, dice, times):
        return cls.__filter_pips_repeated(dice, times)[0] if cls.__filter_pips_repeated(dice, times) else []

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
        return cls.two_of_a_kind(*dice) + cls.three_of_a_kind(*dice) if cls.two_of_a_kind(*dice) and cls.three_of_a_kind(*dice) else 0

    @classmethod
    def two_of_a_kind(*dice):
        return next((2 * pip for pip in set(dice) if dice.count(pip) == 2), 0)
    
    

