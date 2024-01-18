"""
File that contains the class Pips
"""

from enum import Enum, unique

@unique
class Pips(Enum):
    """
    Pips class with the posible values for dice
    """

    UNO = 1
    DOS = 2
    TRES = 3
    CUATRO = 4
    CINCO = 5
    SEIS = 6

if __name__ == "__main__":
    for num in Pips.__members__.values():
        print(num)
        print(num.value)
    print(Pips.__members__.values())
