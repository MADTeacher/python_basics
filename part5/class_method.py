class TestClass:
    """Класс пыщ-пыщ"""
    all_created_clases = []
    def __init__(self, magic=10):
        """Создание экземпляра класса"""
        self.magic = magic
        TestClass.all_created_clases.append(self)
        #self.__class__.all_created_clases.append(self)

    def square_magic(self):
        """Возведение в квадрат"""
        return self.magic ** 2

    @classmethod
    def sum_all_square_magic(cls):
        """Статистический метод подсчета квадратов всех TestClass"""
        rezult = 0
        for it in cls.all_created_clases:
            rezult += it.square_magic()
        return rezult

if __name__ == "__main__":
    my_test1 = TestClass()
    my_test2 = TestClass(5)
    my_test4 = TestClass(15)
    print(TestClass.sum_all_square_magic())
    my_test5 = TestClass(1)
    print(TestClass.sum_all_square_magic())