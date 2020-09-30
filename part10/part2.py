import os
import sqlite3

if __name__ == "__main__":
    db_name = 'my_todolist.db'
    db_schema_name = 'my_todolist_definition.sql'
    db_is_created = os.path.exists(db_name)
    connection = sqlite3.connect(db_name)
    if db_is_created:
        print('Подключение к уже существующей БД!')
    else:
        print('Создание новой БД!')
    with open(db_schema_name, 'rt') as schema_file:
        my_schema = schema_file.read()
        # выполнение кода создания таблиц,
        # загруженного из my_todolist_definition.sql
    connection.executescript(my_schema)

    print('Добавление записей в БД!')
    connection.executescript('''
        INSERT INTO my_project(name, description, deadline)
        VALUES ('MagicMonth', 'Изучить Python за 21 день', '2020-09-01')
        ''')
    connection.executescript('''
        INSERT INTO my_task(description, deadline, status, project)
        VALUES ('Синтаксис и структуры данных', '2020-08-16',
                'done', 'MagicMonth')
        ''')
    connection.executescript(''' 
        insert into my_task(description, deadline, status,  project)
        values ('Функции, классы, модули', '2020-08-25', 'wait', 'MagicMonth')
        ''')
    connection.executescript('''
        insert into my_task(description, deadline, status,  project)
        values ('Поплакать, что не так всё просто', '2020-08-20',
                'wait', 'MagicMonth')
        ''')

