class FirstBaseClass:
    def test_method(self):
        print("FirstBaseClass")

class SecondBaseClass:
    ...

class ThirdBaseClass:
    def test_method(self):
        print("ThirdBaseClass")

class FirstTestClass(FirstBaseClass, ThirdBaseClass):
    ...

class SecondTestClass(SecondBaseClass):
    def test_method(self):
        print("SecondTestClass")

class TopTestClass(FirstTestClass, SecondTestClass):
    ...

if __name__ == "__main__":
    my_class = TopTestClass()
    my_class.test_method() # ??