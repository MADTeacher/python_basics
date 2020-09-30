from threading import Thread, Event
import logging
import time

def event_work(event):
    logging.debug("run event_work")
    event_wait = event.wait()
    logging.debug("Флаг установлен")

def event_with_timeout(event, time):
    while not event.is_set(): # флаг установлен?
        logging.debug("Ожидание установки флага или истечение "
                      "времени в event_with_timeout")
        event_wait = event.wait(time)
        logging.debug("Флаг установлен")
        if event_wait:
            logging.debug("Обработка события")
        else:
            logging.debug("Флаг не был установлен")


if __name__=="__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format='(%(threadName)-10s) %(message)s',
    )

    event = Event()
    my_thread1 = Thread(name='event_thread',
                        target=event_work, args=(event,))
    my_thread1.start()
    my_thread2 = Thread(name='event_timeout',
                        target=event_with_timeout, args=(event, 3))
    my_thread2.start()
    logging.debug('Задержка перед установкой флага')
    time.sleep(0.3)
    event.set()
    logging.debug("Флаг установлен")
