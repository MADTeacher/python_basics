import os
import sqlite3

if __name__ == "__main__":
    db_name = 'my_todolist.db'
    with sqlite3.connect(db_name) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        # сообщаем БД, какие данные должны быть выбраны
        # и отсортированы в порядке дедлайнов
        query = """select id, priority, description, status, 
            deadline from my_task where project = ? 
            order by deadline
            """
        cursor.execute(query, ('MagicMonth',))
        # извлекаем данные
        for it_row in cursor.fetchall():
            print(f"{it_row['id']}, {it_row['priority']}, "
                  f"{it_row['description']}, {it_row['status']}",
                  f"{it_row['deadline']}")


