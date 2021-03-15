create table my_project(
    name primary key,
    description text,
    deadline date
);

create table my_task(
    id integer primary key autoincrement not null,
    priority integer default 0,
    description text,
    status text,
    deadline date
    real_done_date date,
    project text not null references my_project(name)
);
