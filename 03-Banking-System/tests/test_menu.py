from account import Account
from bank import Bank
from customer import Customer
from main import handle_deposit, show_menu


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
