from enum import Enum, auto

class Color(Enum):
    BLACK = 0
    WHITE = 1
    RED = 2
    BLUE = 3


# class TestEnum(Enum):
#     ONE = 0
#     ONE = 1


class TestNewEnum(Enum):
    ZERO = auto()
    ONE = auto()
    TWO = auto()

if __name__ == "__main__":
    print(Color.BLACK)
    print(Color.BLACK.name)
    print(Color.BLACK.value)

    for it in Color:
        print(it)

    for it in TestNewEnum:
        print(repr(it))