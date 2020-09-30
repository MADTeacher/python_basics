class MyRange:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return MyRangeIterator(self)


class MyRangeIterator:
    def __init__(self, myrange_object):
        self.my_range = myrange_object
        self.count_value = myrange_object.start - myrange_object.step

    def __next__(self):
        if self.count_value+self.my_range.step >= self.my_range.stop:
            raise StopIteration
        self.count_value += self.my_range.step
        return self.count_value


if __name__ == "__main__":
    print("MyRange")
    my_range = MyRange(0, 4)
    for it in my_range:
        print(it, end=' ')
    print()
    for it in MyRange(0, 12, 4):
        print(it, end=' ')
    print()
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