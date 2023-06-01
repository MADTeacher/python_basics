from report.base_report_builder import BaseReportBuilder


class ShortReportBuilder(BaseReportBuilder):
    def __init__(self, group_id: int, discipline_id: int):
        super().__init__(
            group_id,
            discipline_id,
            "ShortReport",
        )
