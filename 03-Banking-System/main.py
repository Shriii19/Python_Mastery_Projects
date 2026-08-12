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


def handle_deposit(bank: Bank) -> None:
    account_number = input("Enter account number: ").strip()
    amount_input = input("Enter deposit amount: ").strip()

    try:
        amount = float(amount_input)
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return

    try:
        transaction = bank.deposit(account_number=account_number, amount=amount)
        print(
            f"Deposit successful. Transaction ID: {transaction.transaction_id}, "
            f"Amount: {transaction.amount:.2f}"
        )
    except ValueError as exc:
        print(str(exc))


def handle_withdraw(bank: Bank) -> None:
    account_number = input("Enter account number: ").strip()
    amount_input = input("Enter withdrawal amount: ").strip()

    try:
        amount = float(amount_input)
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return

    try:
        transaction = bank.withdraw(account_number=account_number, amount=amount)
        print(
            f"Withdrawal successful. Transaction ID: {transaction.transaction_id}, "
            f"Amount: {transaction.amount:.2f}"
        )
    except ValueError as exc:
        print(str(exc))


def main() -> None:
    bank = Bank()
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "7":
            print("Goodbye!")
            break

        if choice == "3":
            handle_deposit(bank)
        elif choice == "4":
            handle_withdraw(bank)
        elif choice in {"1", "2", "5", "6"}:
            print(f"Selected option: {choice}")
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
