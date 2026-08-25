from main import show_menu


def test_show_menu_displays_options(capsys):
    show_menu()
    captured = capsys.readouterr()

    assert "=== Inventory Management Menu ===" in captured.out
    assert "1. Add Product" in captured.out
    assert "2. Add Supplier" in captured.out
    assert "3. Add Stock" in captured.out
    assert "4. Sell Product" in captured.out
    assert "5. View Transactions" in captured.out
    assert "6. Low Stock Report" in captured.out
    assert "7. Inventory Summary" in captured.out
    assert "8. Exit" in captured.out
