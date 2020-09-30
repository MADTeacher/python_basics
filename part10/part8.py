import os
import sqlite3

def all_projects_show(connection):
    cursor = connection.cursor()
    cursor.execute('select name, description, deadline  from my_project')
    print("Текущие проекты в списке дел: ")
    for name, description, deadline in cursor.fetchall():
        print("-------------------------------------------")
        print(f'  Имя проекта:"{name}"  \n'
              f'  Описание: "{description}" \n'
              f'  Предельный срок выполнения: {deadline}')
    print("-------------------------------------------")

if __name__ == "__main__":
    db_name = 'my_todolist.db'
    with sqlite3.connect(db_name) as connection:
        print("Начальное состояние БД")
        all_projects_show(connection)  # вывести текущие проекты

        try:
            cursor = connection.cursor()
            cursor.execute("""delete from my_project 
                           where name = 'SuperProgrammer'
                           """)
            print("Состояние БД, после удаления проекта")
            all_projects_show(connection)

            raise RuntimeError("ошибка при удалении")

        except Exception as my_simulated_error:
            print("Откат изменений")
            connection.rollback()
        else:
            connection.commit()

        print("Состояние БД, после вызова метода rollback")
        all_projects_show(connection)





