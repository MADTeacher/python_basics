class TestAttribute:
    def __init__(self, name):
        self.name = name

    def __getattr__(self, item):
        print("in __getattr__")
        if item == "age":
            self.__dict__[item] = 3
            return self.__dict__[item]
        else:
            raise AttributeError(item)

    def __setattr__(self, key, value):
        print(f"in __setattr__, key = {key}, value = {value}")
        if key == "age":
            self.__dict__[key] = value + 1
        elif key == "name":
            self.__dict__[key] = value
        else:
            raise AttributeError(value + "not allowed")

if __name__ == "__main__":
    my_test = TestAttribute("Alex")
    print(my_test.name)
    print(my_test.age)
    print(my_test.age)
    #print(my_test.country)

    my_test.name = "Jon"
    my_test.age = 10
    print(my_test.name)
    print(my_test.age)
    my_test.country = "Germany"
