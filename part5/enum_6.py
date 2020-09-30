from enum import Enum

class Color(Enum):
    BLACK = 0
    WHITE = 1
    RED = 2
    BLUE = 3

class CarBrand(Enum):
    LADA = 0
    FORD = 1
    KAMAZ = 2

class Car(Enum):
    MY_WORK_CAR = ("e006xx127", Color.BLUE, CarBrand.KAMAZ)
    MY_HOME_CAR = ("Н126уx172", Color.WHITE, CarBrand.LADA)
    MY_WIFE_CAR = ("Н125уx001", Color.BLACK, CarBrand.FORD)

    def __init__(self, number, color, brand):
        self.number = number
        self.color = color
        self.brand = brand

if __name__ == "__main__":
    for it in Car:
        print(repr(it))

    print(Car.MY_HOME_CAR.number)
    print(Car.MY_HOME_CAR.brand.name)
    print(Car.MY_HOME_CAR.brand.value)
    print(Car.MY_HOME_CAR.color.name)
    print(Car.MY_HOME_CAR.color.value)
    print(Car.MY_WORK_CAR.color is Color.BLUE)
    print(Car.MY_WORK_CAR.color is Color.RED)