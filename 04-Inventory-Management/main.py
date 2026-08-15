from inventory import Inventory


def show_menu() -> None:
    print("\n=== Inventory Management Menu ===")
    print("1. Add Product")
    print("2. Add Supplier")
    print("3. Add Stock")
    print("4. Sell Product")
    print("5. View Transactions")
    print("6. Low Stock Report")
    print("7. Inventory Summary")
    print("8. Exit")


def main() -> None:
    inventory = Inventory()
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "8":
            print("Goodbye!")
            break

        if choice == "3":
            print("Add stock flow selected.")
        elif choice == "4":
            print("Sell product flow selected.")
        elif choice == "5":
            print("View transactions flow selected.")
        elif choice == "6":
            print("Low stock report selected.")
        elif choice == "7":
            print("Inventory summary selected.")
        elif choice in {"1", "2"}:
            print(f"Selected option: {choice}")
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
