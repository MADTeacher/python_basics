from threading import Thread, RLock
import logging
import time

class DoubleCounter:
    def __init__(self):
        self.first_counter = 1
        self.second_counter = 5
        self.lock = RLock()

    def increment_first_counter(self):
        with self.lock:
            self.first_counter += 1
            logging.debug(f"New first counter value is {self.first_counter}")

    def increment_second_counter(self):
        with self.lock:
            self.second_counter += 1
            logging.debug(f"New second counter value is {self.second_counter}")

    def increment(self):
        with self.lock:  # для блокировки используем диспетчер контекста
            self.increment_first_counter()
            self.increment_second_counter()


def thread_work(counter):
    counter.increment()
    time.sleep(0.2)
    counter.increment_second_counter()
    time.sleep(0.3)
    counter.increment_first_counter()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format='(%(threadName)-10s) %(message)s',
    )
    my_counter = DoubleCounter()
    logging.debug("Start")
    for it in range(3):
        new_thread = Thread(target=thread_work, args=(my_counter,))
        new_thread.start()
    logging.debug("Finish")