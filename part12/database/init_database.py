import os

from sqlalchemy_utils import database_exists, create_database

from database import database as db
from database.database import Session, engine
from utils.parser import Parser
from model.group import Group
from model.admin import Admin
from model.student import Student
from model.discipline import Discipline
from model.missed_class import MissedClass
from dotenv import load_dotenv


load_dotenv()


def init_database() -> None:
    if not database_exists(engine.url):
        create_database(engine.url)
        db.create_tables()
        input_data = Parser(os.getenv("PATH_TO_CONFIG_DATA")).get_data()

        session: Session = db.Session()
        session.add(Admin(telegram_id=os.getenv("DEFAULT_ADMIN")))
        for discipline, groups in input_data.items():
            session.add(
                Discipline(name=discipline, groups=[
                    Group(
                        name=it_gr,
                        students=[
                            Student(full_name=it_st)
                            for it_st in groups[it_gr]
                        ]
                    )
                    for it_gr in groups
                ])
            )
        session.commit()
        session.close()
