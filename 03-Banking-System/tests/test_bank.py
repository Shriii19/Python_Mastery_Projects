import json
from pathlib import Path

from bank import Bank
from customer import Customer
from account import Account
from transaction import Transaction


def test_bank_can_manage_entities(tmp_path):
    bank = Bank(data_dir=str(tmp_path))

    customer = Customer(customer_id=1, name="Alice", phone="9999999999", email="alice@example.com")
    account = Account(account_number="ACC-001", customer_id=1, account_type="Savings", balance=100.0)
    transaction = Transaction(
        transaction_id="TXN-001",
        transaction_type="deposit",
        account_number="ACC-001",
        amount=50.0,
        timestamp="2026-08-09 10:00:00",
        description="Test deposit",
    )

    bank.add_customer(customer)
    bank.add_account(account)
    bank.add_transaction(transaction)

    assert bank.get_customer(1).name == "Alice"
    assert bank.get_account("ACC-001").balance == 100.0
    assert bank.get_transaction("TXN-001").description == "Test deposit"

    saved_customers = json.loads(Path(tmp_path / "customers.json").read_text())
    saved_accounts = json.loads(Path(tmp_path / "accounts.json").read_text())
    saved_transactions = json.loads(Path(tmp_path / "transactions.json").read_text())

    assert len(saved_customers) == 1
    assert len(saved_accounts) == 1
    assert len(saved_transactions) == 1
