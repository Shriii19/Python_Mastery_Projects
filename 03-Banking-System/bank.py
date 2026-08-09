import json
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
