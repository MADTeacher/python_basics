class TestException(Exception): pass

def test_raise(text):
    if text == "exept":
        raise TestException("My Exception")
    print("No Exception")

def test(text):
    try:
        test_raise(text)
    except TestException as my_ex:
        print(my_ex)

if __name__ == "__main__":
    my_str = "notExept"
    test(my_str)
    my_str = "exept"
    test(my_str)