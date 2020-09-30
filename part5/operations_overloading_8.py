class Number:
    def __init__(self, val):
        self.value = val

    def __lt__(self, other):
        return self.value < other

    def __gt__(self, other):
        return self.value > other

    def __le__(self, other):
        return self.value <= other

    def __ge__(self, other):
        return self.value >= other

    def __eq__(self, other):
        return self.value == other

    def __ne__(self, other):
        return self.value != other

if __name__ == "__main__":
    first = Number(10)
    second = Number(11)
    print(first < second)
    print(first > second)
    print(first <= second)
    print(first >= second)
    print(first == second)
    print(first != second)