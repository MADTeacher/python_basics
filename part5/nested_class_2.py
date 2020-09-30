TestVal = 5

def test_function():
    TestVal = 1
    print(TestVal)

    class NestedClass:
        print(TestVal)

        def first_method(self):
            print(TestVal)

        def second_method(self):
            TestVal = 3
            print(TestVal)

    my_class = NestedClass()
    my_class.first_method()
    my_class.second_method()


if __name__ == "__main__":
    print(TestVal)
    test_function()
