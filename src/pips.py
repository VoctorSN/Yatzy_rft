"""
File that contains the class Pips
"""

from enum import Enum, unique

@unique
class Pips(Enum):
    """
    Pips class with the posible values for dice
    """

    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6

if __name__ == "__main__":
    for num in Pips.__members__.values():
        print(num)
        print(num.value)
    print(Pips.__members__.values())
