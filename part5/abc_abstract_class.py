from abc import ABCMeta, abstractmethod


class AbstractBaseClass(metaclass=ABCMeta):
    def print_name(self):
        print("AbstractBaseClass with abc module help")

    @abstractmethod
    def action(self):
        ...


class FirstSubClass(AbstractBaseClass):
    ...


class SecondSubClass(AbstractBaseClass):
    def action(self):
        print("method was defined")


if __name__ == "__main__":
    #my_class = AbstractBaseClass()
    #my_class = FirstSubClass()
    my_class = SecondSubClass()
    my_class.print_name()