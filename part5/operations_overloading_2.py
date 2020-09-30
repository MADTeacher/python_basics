class CustomList:
    def __init__(self, elements_amount=1):
        self.__custom_list = [0] * elements_amount
        self.size = elements_amount

    def __str__(self):
        return f'{self.__custom_list}'

    def __getitem__(self, item):
        if not self.__index_check(item):
            new_list = CustomList(self.size)
            new_list.__custom_list = self.__custom_list[item]
            return new_list
        return self.__custom_list[item]

    def __setitem__(self, key, value):
        if self.__index_check(key):
            self.__custom_list[key] = value
        else:
            my_range = range(key.start if key.start else 0,
                             key.stop,
                             key.step if key.step else 1)
            for it in my_range:
                self.__custom_list[it] = value

    def __index_check(self, index):
        if isinstance(index, int):
            print(f'current index = {index}')
            return True
        elif isinstance(index, slice):
            print(f'slice: start = {index.start}, '
                  f'stop = {index.stop}, '
                  f'step = {index.step}')
            return False
        else:
            raise IndexError("Bad index")


if __name__ == "__main__":
    my_list = CustomList(8)
    print(my_list)
    my_list[4] = 35
    print(my_list)
    my_list[0:4] = 50
    print(my_list)
    new_list = my_list[0:6:2]
    print(new_list)
    #my_list['2']
    for it in new_list:
        print(it)
