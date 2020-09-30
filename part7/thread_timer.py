from threading import Timer
import logging
import time

def thread_work():
    logging.debug("Поехали!")

if __name__=="__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format='(%(threadName)-10s) %(message)s',
    )

    my_timer1 = Timer(0.3, thread_work)
    my_timer1.setName("MyTreadTimer-1")
    my_timer2 = Timer(0.3, thread_work)
    my_timer2.setName("MyTreadTimer-2")

    logging.debug("Запуск таймеров!")
    my_timer1.start()
    my_timer2.start()

    logging.debug(f"Задержка перед отменой выполнения {my_timer2.getName()}")
    time.sleep(0.2)
    logging.debug(f"Отмена потока - {my_timer2.getName()}")
    my_timer2.cancel()
    logging.debug("Завершение")