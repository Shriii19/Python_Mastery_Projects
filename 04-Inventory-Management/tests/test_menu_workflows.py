from main import handle_add_product, handle_add_stock, handle_sell_product, handle_summary
from inventory import Inventory


def test_menu_workflows_update_real_inventory(tmp_path, monkeypatch, capsys):
    inventory = Inventory(data_dir=str(tmp_path))

    inputs = iter(["P-001", "Keyboard", "Accessories", "40", "10", "S-001", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    handle_add_product(inventory)

    inputs = iter(["P-001", "5", "S-001"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    handle_add_stock(inventory)

    inputs = iter(["P-001", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    handle_sell_product(inventory)

    handle_summary(inventory)
    output = capsys.readouterr().out

    assert inventory.get_product("P-001").stock_quantity == 12
    assert len(inventory.transactions) == 2
    assert "Inventory Summary" in output
    assert "Total Transactions" in output
