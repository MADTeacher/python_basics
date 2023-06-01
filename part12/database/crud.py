import datetime

from sqlalchemy import exists, select, delete, Integer, and_
from sqlalchemy import func

from database import database as db
from model.academic_performance import (
    AcademicPerformance,
    MissedInfo,
    FullAcademicPerformance,
)
from model.admin import Admin
from model.group import Group
from model.student import Student
from model.discipline import Discipline
from model.missed_class import MissedClass
from model.assigned_discipline import association_table


def is_admin(user_telegram_id: int) -> bool:
    with db.Session() as session:
        admin = session.get(Admin, user_telegram_id)
        return admin is not None


def get_students(group_id: int) -> list[Student]:
    with db.Session() as session:
        smt = select(Student).where(Student.group_id == group_id)
        return session.scalars(smt).all()


def get_groups() -> list[Group]:
    with db.Session() as session:
        smt = select(Group)
        return session.scalars(smt).all()


def get_disciplines() -> list[Discipline]:
    with db.Session() as session:
        smt = select(Discipline)
        return session.scalars(smt).all()


def get_discipline(discipline_id: int) -> Discipline:
    with db.Session() as session:
        return session.get(Discipline, discipline_id)


def get_group(group_id: int) -> Group:
    with db.Session() as session:
        return session.get(Group, group_id)


def get_assigned_discipline(group_id: int) -> list[Discipline]:
    with db.Session() as session:
        group = session.get(Group, group_id)
        return group.disciplines


def get_assigned_group(discipline_id: int) -> list[Group]:
    with db.Session() as session:
        discipline = session.get(Discipline, discipline_id)
        return discipline.groups


def set_missed_students(
    students_id: list[int],
    group_id: int,
    discipline_id: int,
) -> None:
    session = db.Session()
    group = session.get(Group, group_id)
    current_date = datetime.date.today()
    for student in group.students:
        is_missed = student.id in students_id
        student.missed.append(
            MissedClass(
                discipline_id=discipline_id,
                date=current_date,
                is_missed=is_missed,
            )
        )
    session.commit()
    session.close()


def set_all_missed_students(
    group_id: int,
    discipline_id: int,
    is_missed=True,
) -> None:
    session = db.Session()
    group = session.get(Group, group_id)
    current_date = datetime.date.today()
    for student in group.students:
        student.missed.append(
            MissedClass(
                discipline_id=discipline_id,
                date=current_date,
                is_missed=is_missed,
            )
        )
    session.commit()
    session.close()


def rename_student(student_id: int, new_fullname: str) -> None:
    with db.Session() as session:
        student = session.get(Student, student_id)
        student.full_name = new_fullname
        session.commit()


def remove_student(student_id: int) -> None:
    with db.Session() as session:
        smt = delete(Student).where(Student.id == student_id)
        session.execute(smt)
        session.commit()


def remove_group(group_id: int) -> None:
    session = db.Session()
    smt = delete(Group).where(Group.id == group_id)
    session.execute(smt)
    session.commit()
    session.close()


def add_student(group_id: int, full_name: str) -> None:
    with db.Session() as session:
        group = session.get(Group, group_id)
        group.students.append(Student(full_name=full_name))
        session.commit()


def check_discipline(discipline_name: str) -> bool:
    with db.Session() as session:
        smt = select(Discipline).where(
            Discipline.name == discipline_name,
        )
        return session.scalar(smt) is not None


def add_discipline(discipline_name: str) -> None:
    with db.Session() as session:
        discipline = Discipline(name=discipline_name)
        session.add(discipline)
        session.commit()


def check_group(group_name: str) -> bool:
    with db.Session() as session:
        smt = select(Group).where(Group.name == group_name)
        return session.scalar(smt) is not None


def add_group(group_name: str) -> None:
    with db.Session() as session:
        group = Group(name=group_name)
        session.add(group)
        session.commit()


def get_groups_without_discipline(discipline_id: int) -> list[Group]:
    with db.Session() as session:
        smt = select(Group).where(
            ~Group.disciplines.any(id=discipline_id),
        )
        return session.scalars(smt).all()


def get_academic_performance(
    student_id: int, discipline_id: int
) -> tuple[str, int, int]:
    """
    Возвращает полное имя студента вместе с количеством пропущенных
    им занятий и общим количеством занятий для заданной дисциплины.
    """
    with db.Session() as session:
        student = session.get(Student, student_id)
        missed_classes_query = (
            session.query(
                func.sum(
                    MissedClass.is_missed.cast(Integer),
                ).label("missed_count"),
                func.count(MissedClass.id).label("total_count"),
            )
            .filter(
                and_(
                    MissedClass.student_id == student_id,
                    MissedClass.discipline_id == discipline_id,
                )
            )
            .group_by(MissedClass.student_id)
        )

        result = missed_classes_query.one_or_none()

        if result:
            missed_count, total_count = result
        else:
            missed_count, total_count = 0, 0

        return student.full_name, missed_count, total_count


def count_missed_classes(
    group_id: int, discipline_id: int
) -> tuple[int, list[AcademicPerformance]]:
    # используется для формирования краткого отчета
    with db.Session() as session:
        missed_classes_query = (
            session.query(
                Student.full_name.label("student_name"),
                func.sum(
                    MissedClass.is_missed.cast(Integer),
                ).label("missed_count"),
                func.count(MissedClass.id).label("total_count"),
            )
            .join(MissedClass, MissedClass.student_id == Student.id)
            .filter(Student.group_id == group_id)
            .filter(MissedClass.discipline_id == discipline_id)
            .group_by(Student.full_name)
            .order_by(Student.full_name)
        )

        results = missed_classes_query.all()

        missed_classes_by_group_and_discipline = [
            AcademicPerformance(
                student_name=student_name,
                number_of_passes=missed_count,
            )
            for student_name, missed_count, total_count in results
        ]

        return results[0][2], missed_classes_by_group_and_discipline


def missed_classes_with_day(
    group_id: int, discipline_id: int
) -> list[FullAcademicPerformance]:
    # используется для формирования полного отчета
    with db.Session() as session:
        missed_classes_query = (
            session.query(
                Student.full_name.label("student_name"),
                MissedClass.is_missed.label("missed_count"),
                MissedClass.date.label("date"),
            )
            .join(MissedClass, MissedClass.student_id == Student.id)
            .filter(
                and_(
                    Student.group_id == group_id,
                    MissedClass.discipline_id == discipline_id,
                )
            )
            .order_by(Student.full_name, MissedClass.date)
        )

        results = missed_classes_query.all()

        students: dict[str, list[MissedInfo]] = {}

        for student_name, is_missed, day in results:
            if student_name not in students:
                students[student_name] = []

            students[student_name].append(
                MissedInfo(
                    is_missed=is_missed,
                    day=day,
                )
            )

        result_list: list[FullAcademicPerformance] = [
            FullAcademicPerformance(
                student_name=name,
                missed_data=missed,
            )
            for name, missed in students.items()
        ]

        return result_list


def set_discipline2group(discipline_id: int, group_id: int) -> None:
    with db.Session() as session:
        discipline = session.get(Discipline, discipline_id)
        group = session.get(Group, group_id)
        group.disciplines.append(discipline)
        session.commit()
