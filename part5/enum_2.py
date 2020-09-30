from enum import Enum

class Color(Enum):
    def magic(self): ...

class NewColor(Color):
    BLACK = 0
    WHITE = 1
    GREEN = 99

if __name__ == "__main__":
    myColor = Enum('MyColor', 'BLACK WHITE RED BLUE')
    for it in myColor:
        print(repr(it))

    print(myColor.BLACK is myColor.BLACK)
    print(myColor.BLACK is myColor.WHITE)
    print(myColor.BLACK is not myColor.WHITE)
    print(myColor.BLACK == myColor.BLACK)
    print(myColor.BLACK != myColor.WHITE)
    print(myColor.BLACK == myColor.WHITE)
    print(myColor.BLACK == 1)