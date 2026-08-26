from main import show_menu


def test_show_menu_displays_options(capsys):
    show_menu()
    captured = capsys.readouterr()

    assert "=== Inventory Management Menu ===" in captured.out
    assert "1. Add Product" in captured.out
    assert "2. View Products" in captured.out
    assert "3. Update Product" in captured.out
    assert "4. Delete Product" in captured.out
    assert "5. Add Supplier" in captured.out
    assert "6. View Suppliers" in captured.out
    assert "7. Update Supplier" in captured.out
    assert "8. Delete Supplier" in captured.out
    assert "9. Stock IN" in captured.out
    assert "10. Stock OUT" in captured.out
    assert "11. View Transactions" in captured.out
    assert "12. Low Stock Report" in captured.out
    assert "13. Inventory Summary" in captured.out
    assert "14. Exit" in captured.out
