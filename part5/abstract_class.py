class AbstractBaseClass:
    def print_name(self):
        print("AbstractBaseClass")

    def action(self):
        assert False, "method not define"

class AbstractBaseClassEx:
    def print_name(self):
        print("AbstractBaseClassEx")

    def action(self):
        raise NotImplementedError("method not define")

class SubClass(AbstractBaseClassEx):
    def action(self):
        print("method was defined")

if __name__ == "__main__":
    #my_class = AbstractBaseClass()
    #my_class = AbstractBaseClassEx()
    my_class = SubClass()
    my_class.print_name()
    my_class.action()