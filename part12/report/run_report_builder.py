from enum import Enum

from report.base_report_builder import BaseReportBuilder
from report.full_report_builder import FullReportBuilder
from report.short_report_builder import ShortReportBuilder


class ReportBuilderTypeEnum(Enum):
    FULL = 2
    SHORT = 3


def run_report_builder(
    group_id: int,
    discipline_id: int,
    builder_type: ReportBuilderTypeEnum,
) -> str:
    report_builder: BaseReportBuilder | None = None
    match builder_type:
        case ReportBuilderTypeEnum.SHORT:
            report_builder = ShortReportBuilder(
                group_id,
                discipline_id,
            )
        case ReportBuilderTypeEnum.FULL:
            report_builder = FullReportBuilder(
                group_id,
                discipline_id,
            )

    report_builder.build_report()
    report_builder.save_report()
    return report_builder.get_path_to_report()
