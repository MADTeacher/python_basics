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
    with sqlite3.connect(db_name) as first_connection:
        first_cursor = first_connection.cursor()
        print("Начальное состояние БД")
        all_projects_show(first_connection)  # вывести текущие проекты
        first_cursor.execute('''
                insert into my_project(name, description, deadline)
                values ('SuperProgrammer', 
                        'после изучения Python за 21 день устроиться 
                        на должность Senior Python Developer', 
                        '2020-09-16')
            ''')
        print("Состояние БД, после внесения изменений")
        all_projects_show(first_connection)

    print("Состояние БД, до вызова метода commit")
    with sqlite3.connect(db_name) as second_connection:
        all_projects_show(second_connection)  # вывести текущие проекты

    first_connection.commit()
    print("Состояние БД, после вызова метода commit")
    with sqlite3.connect(db_name) as third_connection:
        all_projects_show(third_connection)  # вывести текущие проекты




