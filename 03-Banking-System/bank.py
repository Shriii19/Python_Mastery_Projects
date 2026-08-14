import json
from datetime import datetime
from pathlib import Path

from account import Account
from customer import Customer
from transaction import Transaction
from config import ACCOUNT_FILE, CUSTOMER_FILE, TRANSACTION_FILE


class Bank:
    def __init__(self, data_dir: str | None = None):
        self.base_dir = Path(data_dir) if data_dir else Path(__file__).resolve().parent
        self.data_dir = self.base_dir / "data" if data_dir is None else Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)

        self.customer_file = self.data_dir / "customers.json"
        self.account_file = self.data_dir / "accounts.json"
        self.transaction_file = self.data_dir / "transactions.json"

        self.customers = self._load_customers()
        self.accounts = self._load_accounts()
        self.transactions = self._load_transactions()

    def _load_customers(self) -> list[Customer]:
        if not self.customer_file.exists():
            return []
        with self.customer_file.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
        return [Customer.from_dict(item) for item in data]

    def _load_accounts(self) -> list[Account]:
        if not self.account_file.exists():
            return []
        with self.account_file.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
        return [Account.from_dict(item) for item in data]

    def _load_transactions(self) -> list[Transaction]:
        if not self.transaction_file.exists():
            return []
        with self.transaction_file.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
        return [Transaction.from_dict(item) for item in data]

    def _save_customers(self) -> None:
        with self.customer_file.open("w", encoding="utf-8") as fh:
            json.dump([customer.to_dict() for customer in self.customers], fh, indent=4)

    def _save_accounts(self) -> None:
        with self.account_file.open("w", encoding="utf-8") as fh:
            json.dump([account.to_dict() for account in self.accounts], fh, indent=4)

    def _save_transactions(self) -> None:
        with self.transaction_file.open("w", encoding="utf-8") as fh:
            json.dump([transaction.to_dict() for transaction in self.transactions], fh, indent=4)

    def add_customer(self, customer: Customer) -> None:
        self.customers.append(customer)
        self._save_customers()

    def add_account(self, account: Account) -> None:
        self.accounts.append(account)
        self._save_accounts()

    def add_transaction(self, transaction: Transaction) -> None:
        self.transactions.append(transaction)
        self._save_transactions()

    def deposit(self, account_number: str, amount: float, description: str = "Cash deposit") -> Transaction:
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        account = self.get_account(account_number)
        if account is None:
            raise ValueError("Account not found.")
        if not account.is_active:
            raise ValueError("Account is inactive.")

        account.balance += amount
        transaction = Transaction(
            transaction_id=f"TXN-{len(self.transactions) + 1:04d}",
            transaction_type="deposit",
            account_number=account_number,
            amount=amount,
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            description=description,
        )

        self.transactions.append(transaction)
        self._save_accounts()
        self._save_transactions()
        return transaction

    def withdraw(self, account_number: str, amount: float, description: str = "Cash withdrawal") -> Transaction:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")

        account = self.get_account(account_number)
        if account is None:
            raise ValueError("Account not found.")
        if not account.is_active:
            raise ValueError("Account is inactive.")
        if account.balance < amount:
            raise ValueError("Insufficient balance.")

        account.balance -= amount
        transaction = Transaction(
            transaction_id=f"TXN-{len(self.transactions) + 1:04d}",
            transaction_type="withdraw",
            account_number=account_number,
            amount=amount,
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            description=description,
        )

        self.transactions.append(transaction)
        self._save_accounts()
        self._save_transactions()
        return transaction

    def transfer(
        self,
        from_account_number: str,
        to_account_number: str,
        amount: float,
        description: str = "Transfer",
    ) -> Transaction:
        if amount <= 0:
            raise ValueError("Transfer amount must be greater than zero.")
        if from_account_number == to_account_number:
            raise ValueError("Source and destination accounts must be different.")

        from_account = self.get_account(from_account_number)
        to_account = self.get_account(to_account_number)
        if from_account is None:
            raise ValueError("Source account not found.")
        if to_account is None:
            raise ValueError("Destination account not found.")
        if not from_account.is_active or not to_account.is_active:
            raise ValueError("Both accounts must be active.")
        if from_account.balance < amount:
            raise ValueError("Insufficient balance in source account.")

        from_account.balance -= amount
        to_account.balance += amount

        transaction = Transaction(
            transaction_id=f"TXN-{len(self.transactions) + 1:04d}",
            transaction_type="transfer",
            account_number=from_account_number,
            amount=amount,
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            description=f"{description} to {to_account_number}",
        )

        self.transactions.append(transaction)
        self._save_accounts()
        self._save_transactions()
        return transaction

    def save_all(self) -> None:
        self._save_customers()
        self._save_accounts()
        self._save_transactions()

    def get_customer(self, customer_id: int) -> Customer | None:
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None

    def get_account(self, account_number: str) -> Account | None:
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def get_transaction(self, transaction_id: str) -> Transaction | None:
        for transaction in self.transactions:
            if transaction.transaction_id == transaction_id:
                return transaction
        return None

    def get_transaction_history(self, account_number: str) -> list[Transaction]:
        account = self.get_account(account_number)
        if account is None:
            return []

        return [
            transaction
            for transaction in self.transactions
            if transaction.account_number == account_number or account_number in transaction.description
        ]

    def get_report_summary(self) -> dict:
        deposit_count = sum(1 for transaction in self.transactions if transaction.transaction_type == "deposit")
        withdraw_count = sum(1 for transaction in self.transactions if transaction.transaction_type == "withdraw")
        transfer_count = sum(1 for transaction in self.transactions if transaction.transaction_type == "transfer")

        return {
            "total_customers": len(self.customers),
            "total_accounts": len(self.accounts),
            "active_accounts": sum(1 for account in self.accounts if account.is_active),
            "inactive_accounts": sum(1 for account in self.accounts if not account.is_active),
            "total_balance": sum(account.balance for account in self.accounts),
            "total_transactions": len(self.transactions),
            "deposit_count": deposit_count,
            "withdraw_count": withdraw_count,
            "transfer_count": transfer_count,
        }
