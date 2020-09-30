def intro_function(text, index):
    print(text[index])

if __name__ == "__main__":
    text_text = "Test"
    intro_function(text_text, 2)
    #intro_function(text_text, 10)
    try:
        intro_function(text_text, 10)
    except:
        print("Перехват исключения IndexError")
    print("Продолжаем работу!")