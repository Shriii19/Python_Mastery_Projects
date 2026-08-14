from bank import Bank


def show_menu() -> None:
    print("\n=== Banking System Menu ===")
    print("1. Create Customer")
    print("2. Create Account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Transfer")
    print("6. View Transactions")
    print("7. Reports")
    print("8. Exit")


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


def handle_transfer(bank: Bank) -> None:
    from_account_number = input("Enter source account number: ").strip()
    to_account_number = input("Enter destination account number: ").strip()
    amount_input = input("Enter transfer amount: ").strip()

    try:
        amount = float(amount_input)
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return

    try:
        transaction = bank.transfer(
            from_account_number=from_account_number,
            to_account_number=to_account_number,
            amount=amount,
        )
        print(
            f"Transfer successful. Transaction ID: {transaction.transaction_id}, "
            f"Amount: {transaction.amount:.2f}"
        )
    except ValueError as exc:
        print(str(exc))


def handle_view_transactions(bank: Bank) -> None:
    account_number = input("Enter account number: ").strip()
    history = bank.get_transaction_history(account_number=account_number)

    if not history:
        print("No transactions found for this account.")
        return

    print("\nTransaction History")
    print("-" * 60)
    for transaction in history:
        print(
            f"{transaction.transaction_id} | {transaction.transaction_type} | "
            f"{transaction.account_number} | {transaction.amount:.2f} | {transaction.timestamp}"
        )


def handle_reports(bank: Bank) -> None:
    summary = bank.get_report_summary()

    print("\nBank Reports")
    print("-" * 60)
    print(f"Total Customers   : {summary['total_customers']}")
    print(f"Total Accounts    : {summary['total_accounts']}")
    print(f"Active Accounts   : {summary['active_accounts']}")
    print(f"Inactive Accounts : {summary['inactive_accounts']}")
    print(f"Total Balance     : {summary['total_balance']:.2f}")
    print(f"Total Transactions: {summary['total_transactions']}")
    print(f"Deposits          : {summary['deposit_count']}")
    print(f"Withdrawals       : {summary['withdraw_count']}")
    print(f"Transfers         : {summary['transfer_count']}")


def main() -> None:
    bank = Bank()
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "8":
            print("Goodbye!")
            break

        if choice == "3":
            handle_deposit(bank)
        elif choice == "4":
            handle_withdraw(bank)
        elif choice == "5":
            handle_transfer(bank)
        elif choice == "6":
            handle_view_transactions(bank)
        elif choice == "7":
            handle_reports(bank)
        elif choice in {"1", "2"}:
            print(f"Selected option: {choice}")
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
