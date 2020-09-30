class MyRange:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.count_value = 0

    def __iter__(self):
        self.count_value = self.start - self.step
        return self

    def __next__(self):
        if self.count_value+self.step >= self.stop:
            raise StopIteration
        self.count_value += self.step
        return self.count_value

class MyGeneratorRange:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        count_value = self.start - self.step
        while count_value+self.step < self.stop:
            count_value += self.step
            yield count_value

if __name__ == "__main__":
    # print("MyRange")
    # my_range = MyRange(0, 4)
    # for it in my_range:
    #     print(it, end=' ')
    # print()
    # for it in MyRange(0, 12, 4):
    #     print(it, end=' ')
    # print()
    # my_iter = iter(my_range)
    # print(next(my_iter))
    # print(next(my_iter))
    # print(next(my_iter))
    # print(next(my_iter))
    # print(next(my_iter))

    test_range = MyRange(0, 3)
    for firtst_it in test_range:
        print(f'firtst_it = {firtst_it}')
        for second_it in test_range:
            print(f'second_it = {second_it}, '
                  f'firtst_it*second_it = {firtst_it*second_it}')



    # print("MyGeneratorRange")
    # my_range = MyGeneratorRange(0, 4)
    # for it in my_range:
    #     print(it, end=' ')
    # print()
    # for it in MyGeneratorRange(0, 12, 4):
    #     print(it, end=' ')
    # print()
    # my_iter = iter(my_range)
    # print(next(my_iter))
    # print(next(my_iter))
    # print(next(my_iter))
    # print(next(my_iter))
    # print(next(my_iter))

    print()
    test_range = MyGeneratorRange(0, 3)
    for firtst_it in test_range:
        print(f'firtst_it = {firtst_it}')
        for second_it in test_range:
            print(f'second_it = {second_it}, '
                  f'firtst_it*second_it = {firtst_it*second_it}')