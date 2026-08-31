from pathlib import Path

import pandas as pd

from config import EMPLOYEES_FILE
from logger import log


class EmployeeAnalyzer:
	"""Loads and displays the employee CSV dataset."""

	def __init__(self, csv_file: Path = EMPLOYEES_FILE) -> None:
		self.csv_file = csv_file
		self.data: pd.DataFrame | None = None

	def load_data(self) -> pd.DataFrame:
		"""Load employee data from the configured CSV file."""
		try:
			self.data = pd.read_csv(self.csv_file)
			log(f"Loaded {len(self.data)} employee records.")
			return self.data
		except (FileNotFoundError, pd.errors.EmptyDataError) as exc:
			log(f"Could not load employee data: {exc}")
			raise ValueError("Unable to load the employee CSV file.") from exc

	def display_data(self) -> None:
		"""Print the employee dataset in a readable table."""
		if self.data is None:
			self.load_data()

		print("\n=== Employee Data ===")
		print(self.data.to_string(index=False))