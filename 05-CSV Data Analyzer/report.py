"""Generate readable text reports from employee analysis results."""

from pathlib import Path

from analyzer import EmployeeAnalyzer
from config import REPORTS_DIR
from logger import log


class ReportGenerator:
	"""Write summary, department, and data-quality reports."""

	def __init__(self, analyzer: EmployeeAnalyzer, reports_dir: Path = REPORTS_DIR) -> None:
		self.analyzer = analyzer
		self.reports_dir = Path(reports_dir)
		self.reports_dir.mkdir(parents=True, exist_ok=True)

	@staticmethod
	def _money(value: float) -> str:
		return f"{value:,.2f}"

	def generate_summary_report(self) -> Path:
		stats = self.analyzer.statistics()
		content = ("================================\nEMPLOYEE SUMMARY\n================================\n\n"
				   f"Total Employees : {stats['total_employees']}\n"
				   f"Average Salary  : {self._money(stats['average_salary'])}\n"
				   f"Total Salary    : {self._money(stats['total_salary'])}\n"
				   f"Highest Salary  : {self._money(stats['maximum_salary'])}\n"
				   f"Lowest Salary   : {self._money(stats['minimum_salary'])}\n"
				   f"Average Age     : {stats['average_age']:.1f}\n"
				   f"Minimum Age     : {stats['minimum_age']:.1f}\n"
				   f"Maximum Age     : {stats['maximum_age']:.1f}\n")
		return self._write("summary_report.txt", content)

	def generate_department_report(self) -> Path:
		lines = ["================================", "DEPARTMENT ANALYSIS", "================================", ""]
		for row in self.analyzer.department_analysis().itertuples(index=False):
			lines.append(f"{row.department}: {row.employee_count} employees, "
						 f"average salary {self._money(row.average_salary)}, "
						 f"total salary {self._money(row.total_salary)}")
		return self._write("department_report.txt", "\n".join(lines) + "\n")

	def generate_data_quality_report(self) -> Path:
		quality = self.analyzer.data_quality()
		lines = ["================================", "DATA QUALITY REPORT", "================================", "",
				 "Missing Values:", quality["missing_values"].to_string(), "",
				 f"Duplicate Rows: {quality['duplicate_count']} duplicate row(s) found"]
		return self._write("data_quality_report.txt", "\n".join(lines) + "\n")

	def generate_all_reports(self) -> list[Path]:
		paths = [self.generate_summary_report(), self.generate_department_report(),
				 self.generate_data_quality_report()]
		log("All reports generated.")
		return paths

	def _write(self, filename: str, content: str) -> Path:
		path = self.reports_dir / filename
		path.write_text(content, encoding="utf-8")
		log(f"Report generated: {filename}")
		return path