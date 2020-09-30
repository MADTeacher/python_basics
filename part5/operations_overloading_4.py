class TestContains:
    def __init__(self, value):
        self.data = value

    def __contains__(self, x):
        return x in self.data

if __name__ == '__main__' :
    X = TestContains([1, 2, 3, 4, 5])
    print(3 in X)
    print(10 in X)
    print('d' in X)