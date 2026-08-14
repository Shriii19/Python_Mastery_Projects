from account import Account
from bank import Bank
from customer import Customer
from main import handle_deposit, handle_transfer, handle_view_transactions, handle_withdraw, show_menu


def test_show_menu_displays_options(capsys):
    show_menu()
    captured = capsys.readouterr()

    assert "1. Create Customer" in captured.out
    assert "2. Create Account" in captured.out
    assert "3. Deposit" in captured.out
    assert "4. Withdraw" in captured.out
    assert "5. Transfer" in captured.out
    assert "6. View Transactions" in captured.out
    assert "7. Exit" in captured.out


def test_handle_deposit_updates_bank_data(tmp_path, monkeypatch, capsys):
    bank = Bank(data_dir=str(tmp_path))
    bank.add_customer(Customer(customer_id=1, name="Alice", phone="9999999999", email="alice@example.com"))
    bank.add_account(Account(account_number="ACC-001", customer_id=1, account_type="Savings", balance=100.0))

    inputs = iter(["ACC-001", "50"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    handle_deposit(bank)
    captured = capsys.readouterr()

    assert "Deposit successful" in captured.out
    assert bank.get_account("ACC-001").balance == 150.0


def test_handle_withdraw_updates_bank_data(tmp_path, monkeypatch, capsys):
    bank = Bank(data_dir=str(tmp_path))
    bank.add_customer(Customer(customer_id=2, name="Bob", phone="5555555555", email="bob@example.com"))
    bank.add_account(Account(account_number="ACC-002", customer_id=2, account_type="Checking", balance=200.0))

    inputs = iter(["ACC-002", "75"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    handle_withdraw(bank)
    captured = capsys.readouterr()

    assert "Withdrawal successful" in captured.out
    assert bank.get_account("ACC-002").balance == 125.0


def test_handle_transfer_updates_bank_data(tmp_path, monkeypatch, capsys):
    bank = Bank(data_dir=str(tmp_path))
    bank.add_customer(Customer(customer_id=3, name="Carol", phone="4444444444", email="carol@example.com"))
    bank.add_account(Account(account_number="ACC-003", customer_id=3, account_type="Savings", balance=250.0))
    bank.add_account(Account(account_number="ACC-004", customer_id=3, account_type="Savings", balance=100.0))

    inputs = iter(["ACC-003", "ACC-004", "60"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    handle_transfer(bank)
    captured = capsys.readouterr()

    assert "Transfer successful" in captured.out
    assert bank.get_account("ACC-003").balance == 190.0
    assert bank.get_account("ACC-004").balance == 160.0


def test_handle_view_transactions_displays_history(tmp_path, monkeypatch, capsys):
    bank = Bank(data_dir=str(tmp_path))
    bank.add_customer(Customer(customer_id=4, name="Dan", phone="6666666666", email="dan@example.com"))
    bank.add_account(Account(account_number="ACC-009", customer_id=4, account_type="Savings", balance=500.0))
    bank.deposit(account_number="ACC-009", amount=60.0)

    inputs = iter(["ACC-009"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    handle_view_transactions(bank)
    captured = capsys.readouterr()

    assert "Transaction History" in captured.out
    assert "deposit" in captured.out
    assert "ACC-009" in captured.out
