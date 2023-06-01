from dataclasses import dataclass
from datetime import date


@dataclass
class AcademicPerformance:
    student_name: str
    number_of_passes: int


@dataclass
class MissedInfo:
    day: date
    is_missed: bool


@dataclass
class FullAcademicPerformance:
    student_name: str
    missed_data: list[MissedInfo]
