def test_assert(value):
    assert value > 0, 'value должен быть > 0'
    return 30/value

if __name__ == "__main__":
    with open('dataFile', 'r') as myfile:
        ...
    print(test_assert(10))
    print(test_assert(0))