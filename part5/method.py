class TestClass:
    def __init__(self, magic=10):
        self.magic = magic

    def square_magic(self):
        return self.magic ** 2

if __name__ == "__main__":
    my_test1 = TestClass()
    print(my_test1.square_magic())
    my_test2 = TestClass(5)
    print(my_test2.square_magic())
    print(TestClass.square_magic(my_test2))
