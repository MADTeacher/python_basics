class Number:
    def __init__(self, val):
        self.value = val

    def __sub__(self, other):
        return self.value - other

class NewNumber(Number):
    def __repr__(self):
        return f'{self.value}'

if __name__ == "__main__":
    number = Number(10)
    print(number)

    newNumber = NewNumber(15)
    print(newNumber)
    newNumber -= 3
    print(newNumber)