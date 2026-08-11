from bank import Bank


def show_menu() -> None:
    print("\n=== Banking System Menu ===")
    print("1. Create Customer")
    print("2. Create Account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Transfer")
    print("6. View Transactions")
    print("7. Exit")


def main() -> None:
    bank = Bank()
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "7":
            print("Goodbye!")
            break

        if choice in {"1", "2", "3", "4", "5", "6"}:
            print(f"Selected option: {choice}")
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
