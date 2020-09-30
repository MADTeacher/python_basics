from enum import IntEnum, Enum

class FirstEnum(IntEnum):
     GO = 1
     STOP = 2

class SecondEnum(IntEnum):
     TURN = 1
     DOWN = 2

class Color(Enum):
    RED = 1
    BLACK = 2

if __name__ == "__main__":
    print(FirstEnum == 1)
    print(FirstEnum.GO == 1)
    print(FirstEnum.GO == SecondEnum.TURN)

    print(Color.RED == SecondEnum.TURN)