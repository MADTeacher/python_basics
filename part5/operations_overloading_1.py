class Number:
    def __init__(self, val):
        self.value = val

    def __sub__(self, other):
        return Number(self.value - other)

    def __add__(self, other):
        return Number(self.value + other)

    def __or__(self, other):
        return Number(self.value | other)

    def __str__(self):
        return f'{self.value}'

if __name__ == "__main__":
    my_number = Number(4)
    addValue = my_number + 10
    print(addValue)
    subValue = addValue - 13
    print(subValue)
    orValue = subValue | 4
    print(orValue)