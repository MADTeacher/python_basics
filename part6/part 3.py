class TestException(Exception): pass
class NewTestException(Exception): pass
if __name__ == "__main__":
    # try:
    #     raise IndexError("my error")
    # except IndexError:
    #     print("Обработка исключения")
    #     raise
    # print("Работаем дальше!")
    try:
        try:
            raise IndexError("my error")
        except IndexError as ex:
            print("Обработка исключения")
            raise TestException("Сцепление") from ex
    except TestException as ex:
        raise NewTestException("Еще одно сцепление") from ex

    print("Работаем дальше!")