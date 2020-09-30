from threading import Thread


def thread_work(name):
    print(name)


if __name__=="__main__":
    for it in range(5):
        new_thread = Thread(target=thread_work, args=(f"Thread #{it}",))
        new_thread.start()
