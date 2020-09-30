from threading import Thread, Semaphore, Lock, current_thread
import logging
import time

class TestPool:

    def __init__(self):
        super(TestPool, self).__init__()
        self.active = []
        self.lock = Lock()

    def makeActive(self, name):
        with self.lock:
            self.active.append(name)
            logging.debug(f'Потоков в пуле {self.active}')

    def makeInactive(self, name):
        with self.lock:
            self.active.remove(name)
            logging.debug(f'Потоков в пуле {self.active}')


def worker(semaphore, pool):
    logging.debug('Ожидание очереди при подключении к пулу')
    with semaphore:
        name = current_thread().getName()
        pool.makeActive(name)
        time.sleep(0.1)
        pool.makeInactive(name)


if __name__=="__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s (%(threadName)-1s) %(message)s',
        datefmt='%I:%M:%S %p'
    )

    pool = TestPool()
    semaphore = Semaphore(2)
    for it in range(6):
        new_thread = Thread(target=worker, name=str(it),
                            args=(semaphore, pool),
                            )
        new_thread.start()
