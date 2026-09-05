from pathlib import Path
from typing import Any
from io import StringIO

import pandas as pd

from config import EMPLOYEES_FILE
from logger import log

REQUIRED_COLUMNS = ["id", "name", "department", "age", "salary"]


class EmployeeAnalyzer:
	"""Load, inspect, analyze, and clean employee data."""

	def __init__(self, csv_file: Path = EMPLOYEES_FILE) -> None:
		self.csv_file = Path(csv_file)
		self.data: pd.DataFrame | None = None

	def load_data(self) -> pd.DataFrame:
		"""Load and validate the employee CSV file."""
		try:
			data = pd.read_csv(self.csv_file)
		except FileNotFoundError as exc:
			log(f"CSV file not found: {self.csv_file}")
			raise ValueError("CSV file was not found.") from exc
		except pd.errors.EmptyDataError as exc:
			log("CSV file is empty.")
			raise ValueError("CSV file is empty.") from exc
		except (pd.errors.ParserError, UnicodeDecodeError) as exc:
			log(f"Invalid CSV: {exc}")
			raise ValueError("CSV file is invalid or cannot be read.") from exc

		missing_columns = [column for column in REQUIRED_COLUMNS if column not in data]
		if missing_columns:
			message = f"CSV is missing required columns: {', '.join(missing_columns)}."
			log(message)
			raise ValueError(message)
		if data.empty:
			raise ValueError("CSV contains no employee records.")

		self.data = data[REQUIRED_COLUMNS].copy()
		log(f"Loaded {len(self.data)} employee records.")
		return self.data

	def _require_data(self) -> pd.DataFrame:
		if self.data is None:
			self.load_data()
		return self.data

	def view_data(self) -> pd.DataFrame:
		return self._require_data().copy()

	def first_records(self, count: int = 5) -> pd.DataFrame:
		return self._require_data().head(count)

	def last_records(self, count: int = 5) -> pd.DataFrame:
		return self._require_data().tail(count)

	def dataset_shape(self) -> tuple[int, int]:
		return self._require_data().shape

	def column_names(self) -> list[str]:
		return list(self._require_data().columns)

	def data_types(self) -> pd.Series:
		return self._require_data().dtypes

	def dataset_info(self) -> str:
		output = StringIO()
		self._require_data().info(buf=output)
		return output.getvalue()

	def filter_data(self, department: str | None = None, salary_gt: float | None = None,
					salary_lt: float | None = None, age_gt: float | None = None,
					age_lt: float | None = None) -> pd.DataFrame:
		"""Return rows matching all supplied filters."""
		data = self._require_data()
		result = data
		if department:
			department = department.strip().casefold()
			result = result[result["department"].astype(str).str.casefold() == department]
		for column, value, operator in (("salary", salary_gt, ">"), ("salary", salary_lt, "<"),
										("age", age_gt, ">"), ("age", age_lt, "<")):
			if value is not None:
				if not isinstance(value, (int, float)):
					raise ValueError("Filter values must be numeric.")
				result = result[result[column].notna() & (result[column] > value if operator == ">" else result[column] < value)]
		log("Employee data filtered.")
		return result.copy()

	def sort_data(self, column: str, ascending: bool = True) -> pd.DataFrame:
		column = column.strip().casefold()
		if column not in {"name", "age", "salary", "department"}:
			raise ValueError("Sort column must be name, age, salary, or department.")
		result = self._require_data().sort_values(column, ascending=ascending, na_position="last")
		log(f"Employee data sorted by {column}.")
		return result.copy()

	def statistics(self) -> dict[str, Any]:
		data = self._require_data()
		result = {"total_employees": len(data), "average_salary": data["salary"].mean(),
				  "total_salary": data["salary"].sum(), "minimum_salary": data["salary"].min(),
				  "maximum_salary": data["salary"].max(), "average_age": data["age"].mean(),
				  "minimum_age": data["age"].min(), "maximum_age": data["age"].max()}
		log("Employee statistics calculated.")
		return result

	def department_analysis(self) -> pd.DataFrame:
		result = (self._require_data().groupby("department", dropna=False)
				  .agg(employee_count=("id", "count"), average_salary=("salary", "mean"),
					   total_salary=("salary", "sum")).reset_index())
		log("Department analysis calculated.")
		return result

	def missing_values(self) -> pd.Series:
		return self._require_data().isna().sum()

	def duplicate_rows(self) -> pd.DataFrame:
		return self._require_data()[self._require_data().duplicated(keep=False)].copy()

	def data_quality(self) -> dict[str, Any]:
		missing = self.missing_values()
		duplicates = self._require_data().duplicated().sum()
		return {"missing_values": missing, "duplicate_count": int(duplicates),
				"duplicate_rows": self.duplicate_rows()}

	def clean_data(self) -> pd.DataFrame:
		"""Return a cleaned copy without changing the original loaded data."""
		cleaned = self._require_data().copy()
		cleaned["id"] = pd.to_numeric(cleaned["id"], errors="coerce").astype("Int64")
		for column in ("age", "salary"):
			cleaned[column] = pd.to_numeric(cleaned[column], errors="coerce")
			cleaned[column] = cleaned[column].fillna(cleaned[column].median())
		cleaned["name"] = cleaned["name"].fillna("Unknown")
		cleaned["department"] = cleaned["department"].fillna("Unknown")
		cleaned = cleaned.drop_duplicates().reset_index(drop=True)
		log(f"Cleaned data created with {len(cleaned)} records.")
		return cleaned

	def display_data(self) -> None:
		print("\n=== Employee Data ===")
		print(self.view_data().to_string(index=False))