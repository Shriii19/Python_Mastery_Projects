from analyzer import EmployeeAnalyzer


def show_menu() -> None:
	print("\n=== CSV Data Analyzer ===")
	print("1. Load and View Employee Data")
	print("2. Exit")


def main() -> None:
	analyzer = EmployeeAnalyzer()

	while True:
		show_menu()
		choice = input("Choose an option: ").strip()

		if choice == "1":
			try:
				analyzer.display_data()
			except ValueError as exc:
				print(f"Error: {exc}")
		elif choice == "2":
			print("Goodbye.")
			break
		else:
			print("Invalid option. Please try again.")


if __name__ == "__main__":
	main()