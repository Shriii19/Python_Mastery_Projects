import json
from pathlib import Path

from bank import Bank
from customer import Customer
from account import Account
from transaction import Transaction
from config import LOG_FILE


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


def test_bank_can_save_and_reload_all_data(tmp_path):
    bank = Bank(data_dir=str(tmp_path))
    bank.add_customer(Customer(customer_id=2, name="Bob", phone="5555555555", email="bob@example.com"))
    bank.add_account(Account(account_number="ACC-002", customer_id=2, account_type="Current", balance=250.0))
    bank.add_transaction(
        Transaction(
            transaction_id="TXN-002",
            transaction_type="withdraw",
            account_number="ACC-002",
            amount=25.0,
            timestamp="2026-08-10 09:30:00",
            description="ATM withdrawal",
        )
    )

    bank.save_all()

    reloaded_bank = Bank(data_dir=str(tmp_path))

    assert reloaded_bank.get_customer(2).name == "Bob"
    assert reloaded_bank.get_account("ACC-002").balance == 250.0
    assert reloaded_bank.get_transaction("TXN-002").transaction_type == "withdraw"


def test_deposit_updates_balance_and_creates_transaction(tmp_path):
    bank = Bank(data_dir=str(tmp_path))
    bank.add_customer(Customer(customer_id=3, name="Carol", phone="1111111111", email="carol@example.com"))
    bank.add_account(Account(account_number="ACC-003", customer_id=3, account_type="Savings", balance=100.0))

    transaction = bank.deposit(account_number="ACC-003", amount=75.0)

    updated_account = bank.get_account("ACC-003")
    assert updated_account is not None
    assert updated_account.balance == 175.0
    assert transaction.transaction_type == "deposit"
    assert transaction.account_number == "ACC-003"

    saved_accounts = json.loads(Path(tmp_path / "accounts.json").read_text())
    saved_transactions = json.loads(Path(tmp_path / "transactions.json").read_text())
    assert saved_accounts[0]["balance"] == 175.0
    assert saved_transactions[0]["transaction_type"] == "deposit"


def test_withdraw_updates_balance_and_creates_transaction(tmp_path):
    bank = Bank(data_dir=str(tmp_path))
    bank.add_customer(Customer(customer_id=4, name="David", phone="2222222222", email="david@example.com"))
    bank.add_account(Account(account_number="ACC-004", customer_id=4, account_type="Checking", balance=200.0))

    transaction = bank.withdraw(account_number="ACC-004", amount=50.0)

    updated_account = bank.get_account("ACC-004")
    assert updated_account is not None
    assert updated_account.balance == 150.0
    assert transaction.transaction_type == "withdraw"
    assert transaction.account_number == "ACC-004"

    saved_accounts = json.loads(Path(tmp_path / "accounts.json").read_text())
    saved_transactions = json.loads(Path(tmp_path / "transactions.json").read_text())
    assert saved_accounts[0]["balance"] == 150.0
    assert saved_transactions[0]["transaction_type"] == "withdraw"


def test_transfer_moves_money_between_accounts_and_creates_transaction(tmp_path):
    bank = Bank(data_dir=str(tmp_path))
    bank.add_customer(Customer(customer_id=5, name="Eve", phone="3333333333", email="eve@example.com"))
    bank.add_account(Account(account_number="ACC-005", customer_id=5, account_type="Savings", balance=300.0))
    bank.add_account(Account(account_number="ACC-006", customer_id=5, account_type="Savings", balance=120.0))

    transaction = bank.transfer(from_account_number="ACC-005", to_account_number="ACC-006", amount=80.0)

    source_account = bank.get_account("ACC-005")
    destination_account = bank.get_account("ACC-006")
    assert source_account is not None
    assert destination_account is not None
    assert source_account.balance == 220.0
    assert destination_account.balance == 200.0
    assert transaction.transaction_type == "transfer"
    assert transaction.account_number == "ACC-005"
    assert "ACC-006" in transaction.description

    saved_accounts = json.loads(Path(tmp_path / "accounts.json").read_text())
    saved_transactions = json.loads(Path(tmp_path / "transactions.json").read_text())
    assert saved_accounts[0]["balance"] == 220.0
    assert saved_accounts[1]["balance"] == 200.0
    assert saved_transactions[0]["transaction_type"] == "transfer"


def test_get_transaction_history_returns_account_transactions(tmp_path):
    bank = Bank(data_dir=str(tmp_path))
    bank.add_customer(Customer(customer_id=6, name="Frank", phone="7777777777", email="frank@example.com"))
    bank.add_account(Account(account_number="ACC-007", customer_id=6, account_type="Savings", balance=400.0))
    bank.add_account(Account(account_number="ACC-008", customer_id=6, account_type="Savings", balance=100.0))

    bank.deposit(account_number="ACC-007", amount=50.0)
    bank.withdraw(account_number="ACC-007", amount=25.0)
    bank.transfer(from_account_number="ACC-007", to_account_number="ACC-008", amount=40.0)

    history = bank.get_transaction_history(account_number="ACC-007")

    assert len(history) == 3
    assert history[0].transaction_type == "deposit"
    assert history[1].transaction_type == "withdraw"
    assert history[2].transaction_type == "transfer"


def test_get_transaction_history_returns_empty_for_unknown_account(tmp_path):
    bank = Bank(data_dir=str(tmp_path))

    history = bank.get_transaction_history(account_number="ACC-UNKNOWN")

    assert history == []


def test_deposit_logs_action(tmp_path):
    bank = Bank(data_dir=str(tmp_path))
    bank.add_customer(Customer(customer_id=7, name="Grace", phone="8888888888", email="grace@example.com"))
    bank.add_account(Account(account_number="ACC-012", customer_id=7, account_type="Savings", balance=50.0))

    bank.deposit(account_number="ACC-012", amount=10.0)

    log_path = Path(LOG_FILE)
    assert log_path.exists()
    contents = log_path.read_text(encoding="utf-8")
    assert "deposit" in contents.lower()
    assert "ACC-012" in contents
