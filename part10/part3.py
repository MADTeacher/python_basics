import os
import sqlite3

if __name__ == "__main__":
    db_name = 'my_todolist.db'
    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()
        # сообщаем БД, какие данные должны быть выбраны
        cursor.execute('''
            select id, priority, description, status, deadline from my_task 
            where project = 'MagicMonth' ''')
        # извлекаем данные
        for it_row in cursor.fetchall():
            id, priority, description, status, deadline = it_row
            print(f'{id}, {priority}, {description}, {status}, {deadline}')

