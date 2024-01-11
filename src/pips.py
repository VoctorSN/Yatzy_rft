from enum import Enum, unique

@unique
class Pips(Enum):

    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6

if __name__ == "__main__":
    for num in Pips.__members__.values():
        print(num)
        print(num._value_)
    print(Pips.__members__.values())
