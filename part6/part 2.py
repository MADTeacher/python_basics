def example_1(text):
    try:
        text[99]
    except IndexError:
        print('except') # выполняется except
    finally:
        print('finally') # выполняется finally
    print('after try')

def example_2(text):
    try:
        text[3]
    except IndexError:
        print('except') # выполняется except
    else:
        print('else')  # выполняется else
    finally:
        print('finally') # выполняется finally
    print('after try')

def example_3(text):
    try:
        text[3]
    except IndexError:
        print('except') # выполняется except
    finally:
        print('finally') # выполняется finally
    print('after try')

def example_4():
    try:
        my_error = 1 / 0
    except IndexError:
        print('except')  # выполняется except
    finally:
        print('finally')  # выполняется finally
    print('after run')  # после выполнения

def example_5():
    file = open('data', 'w')
    try:
        raise FileNotFoundError # Генерирует исключение
    finally:
        print('finally')  # выполняется finally
        file.close()  # Всегда закрывать файл, чтобы сбросить буферы
    print('after try')


if __name__ == "__main__":
    my_text = "Test"
    print("run example_1")
    example_1(my_text)
    print("run example_2")
    example_2(my_text)
    print("run example_3")
    example_3(my_text)
    # print("run example_4")
    # example_4()
    print("run example_5")
    example_5()
    print("Продолжаем работу!")