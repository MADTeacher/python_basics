class MyError(Exception):pass

class TestWith:
    def print_value(self, value):
        print(f"Входное значение: {value}")

    def __enter__(self):
        print("Начало блока with")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("Успешное завершение!")
        else:
            print("Было сгенерировано исключение: "+str(exc_type))
            return False

if __name__ == "__main__":
    with TestWith() as test_object:
        test_object.print_value("Test 1")
        print("Конец блока with")
    with TestWith() as test_object:
        test_object.print_value("Test 2")
        raise MyError("Ошибка!")
        print("Конец блока with")
