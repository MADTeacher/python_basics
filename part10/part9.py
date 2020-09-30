import sqlite3
import logging
from threading import Thread, Event
import time

logging.basicConfig(
      level=logging.DEBUG,
      format='%(asctime)s (%(threadName)-10s) %(message)s',
)

db_name = 'my_todolist.db'

def writer_to_db(sync_event, level):
    with sqlite3.connect(db_name,
                 isolation_level=level) as connection:
        cursor = connection.cursor()
        cursor.execute('update my_task set priority = priority+1')
        logging.debug("Ожидание синхронизации")
        sync_event.wait()
        logging.debug("Пауза в работе")
        time.sleep(1)
        connection.commit()
        logging.debug("Фиксация изменений")

def reader_to_db(sync_event, level):
    with sqlite3.connect(db_name,
                 isolation_level=level) as connection:
        cursor = connection.cursor()
        logging.debug("Ожидание синхронизации")
        sync_event.wait()
        logging.debug("Ожидание")
        cursor.execute('select * from my_task')
        logging.debug("Выборка из таблицы выполнена")
        cursor.fetchall()
        logging.debug("Получение результата выборки")

if __name__ == "__main__":
    isolation_level = 'EXCLUSIVE'
    sync_event = Event()
    my_threads = [
        Thread(name='А.С. Пушкин', target=writer_to_db,
                    args=(sync_event,isolation_level,)),
        Thread(name='Л.Н. Толстой', target=writer_to_db,
                     args=(sync_event,isolation_level,)),
        Thread(name='Иванов И.И.', target=reader_to_db,
                     args=(sync_event,isolation_level,)),
        Thread(name='Сидоров С.С.', target=reader_to_db,
                    args=(sync_event,isolation_level,)),
    ]

    [it.start() for it in my_threads]

    time.sleep(2)
    logging.debug("Подготовительные работы завершены")
    sync_event.set()

    [it.join() for it in my_threads]






