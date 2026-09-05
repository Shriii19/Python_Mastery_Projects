import math

from analyzer import EmployeeAnalyzer
from logger import log
from report import ReportGenerator


def show_menu() -> None:
	print("\n========================================")
	print("       CSV DATA ANALYZER")
	print("========================================")
	print("1. View Data")
	print("2. Dataset Information")
	print("3. Filter Data")
	print("4. Sort Data")
	print("5. Statistics")
	print("6. Department Analysis")
	print("7. Data Quality")
	print("8. Clean Data")
	print("9. Generate Reports")
	print("0. Exit")


def print_frame(frame) -> None:
	print(frame.to_string(index=False))


def numeric_input(prompt: str) -> float | None:
	value = input(prompt).strip()
	if not value:
		return None
	try:
		result = float(value)
	except ValueError:
		print("Please enter a valid number or leave the field blank.")
		return None
	if not math.isfinite(result):
		print("Please enter a finite number or leave the field blank.")
		return None
	return result


def main() -> None:
	log("Application started.")
	analyzer = EmployeeAnalyzer()
	reports = ReportGenerator(analyzer)

	while True:
		show_menu()
		choice = input("Choose an option: ").strip()

		try:
			if choice == "1":
				print_frame(analyzer.view_data())
			elif choice == "2":
				print(f"Shape: {analyzer.dataset_shape()}")
				print(f"Columns: {', '.join(analyzer.column_names())}")
				print(analyzer.data_types())
				print(analyzer.dataset_info())
			elif choice == "3":
				department = input("Department (Enter to skip): ").strip() or None
				print_frame(analyzer.filter_data(department, numeric_input("Salary greater than (Enter to skip): "),
					numeric_input("Salary less than (Enter to skip): "), numeric_input("Age greater than (Enter to skip): "),
					numeric_input("Age less than (Enter to skip): ")))
			elif choice == "4":
				column = input("Sort by (name, age, salary, department): ").strip()
				ascending = input("Ascending? (y/n): ").strip().lower() != "n"
				print_frame(analyzer.sort_data(column, ascending))
			elif choice == "5":
				for key, value in analyzer.statistics().items():
					print(f"{key.replace('_', ' ').title()}: {value:,.2f}" if isinstance(value, float) else f"{key.replace('_', ' ').title()}: {value}")
			elif choice == "6":
				print_frame(analyzer.department_analysis())
			elif choice == "7":
				quality = analyzer.data_quality()
				print("Missing Values:")
				print(quality["missing_values"].to_string())
				print(f"Duplicate rows: {quality['duplicate_count']}")
			elif choice == "8":
				print_frame(analyzer.clean_data())
			elif choice == "9":
				for path in reports.generate_all_reports():
					print(f"Generated: {path.name}")
			elif choice == "0":
				print("Goodbye.")
				break
			else:
				print("Invalid option. Please try again.")
		except ValueError as exc:
			print(f"Error: {exc}")
		except (EOFError, KeyboardInterrupt):
			print("\nGoodbye.")
			break


if __name__ == "__main__":
	main()