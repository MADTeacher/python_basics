import database.crud as crud
from report.base_report_builder import (
    BaseReportBuilder,
    ReportFieldEnum,
)


class FullReportBuilder(BaseReportBuilder):
    def __init__(self, group_id: int, discipline_id: int):
        super().__init__(
            group_id,
            discipline_id,
            "FullReport",
        )

    def build_report(self) -> None:
        super().build_report()
        worksheet = self.wb.active

        student_missed_info = crud.missed_classes_with_day(
            self.group_id,
            self.discipline_id,
        )
        row = 1
        for student in student_missed_info:
            col = ReportFieldEnum.NEXT
            if row == 1:
                for day in student.missed_data:
                    worksheet.cell(
                        row=row,
                        column=col,
                    ).value = day.day
                    col += 1
                row += 1
                col = ReportFieldEnum.NEXT

            for day in student.missed_data:
                color = BaseReportBuilder.GREEN_FILL
                if day.is_missed:
                    color = BaseReportBuilder.RED_FILL

                worksheet.cell(
                    row=row,
                    column=col,
                ).fill = color
                col += 1
            row += 1
