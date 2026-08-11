from main import show_menu


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
