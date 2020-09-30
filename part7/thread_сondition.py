from threading import Thread, Condition
import logging
import time


def slave(condition):
    logging.debug('Запуск потока ведомого')
    with condition:
        condition.wait()  # ожидаем разблокировки ресурса
        logging.debug('Блокировка с ведомого снята')


def master(condition):
    logging.debug('Запуск потока ведущего')
    with condition:
        logging.debug('Разблокировка ресурса')
        condition.notifyAll()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format='(%(threadName)-3s) %(message)s',
    )

    condition = Condition()
    slave1 = Thread(name='slave1', target=slave, args=(condition,))
    slave2 = Thread(name='slave2', target=slave, args=(condition,))
    master = Thread(name='master', target=master, args=(condition,))

    slave1.start()
    time.sleep(0.1)
    slave2.start()
    time.sleep(0.1)
    master.start()
