import pytest

from inventory import Inventory
from product import Product


def test_add_stock_increases_quantity_and_records_transaction(tmp_path):
    inventory = Inventory(data_dir=str(tmp_path))
    inventory.add_product(
        Product(
            product_id="P-001",
            name="Keyboard",
            category="Accessories",
            price=40.0,
            stock_quantity=10,
            supplier_id="S-001",
            reorder_level=5,
        )
    )

    transaction = inventory.add_stock("P-001", 8, supplier_id="S-001", description="Purchase order")

    product = inventory.get_product("P-001")
    assert product is not None
    assert product.stock_quantity == 18
    assert transaction.transaction_type == "purchase"
    assert transaction.quantity == 8
    assert transaction.supplier_id == "S-001"
    assert len(inventory.transactions) == 1


def test_sell_product_decreases_quantity_and_records_transaction(tmp_path):
    inventory = Inventory(data_dir=str(tmp_path))
    inventory.add_product(
        Product(
            product_id="P-002",
            name="Monitor",
            category="Electronics",
            price=150.0,
            stock_quantity=12,
            supplier_id="S-002",
            reorder_level=4,
        )
    )

    transaction = inventory.sell_product("P-002", 3, description="Store sale")

    product = inventory.get_product("P-002")
    assert product is not None
    assert product.stock_quantity == 9
    assert transaction.transaction_type == "sale"
    assert transaction.quantity == 3
    assert transaction.description == "Store sale"


def test_sell_product_raises_error_if_insufficient_stock(tmp_path):
    inventory = Inventory(data_dir=str(tmp_path))
    inventory.add_product(
        Product(
            product_id="P-003",
            name="Mouse",
            category="Accessories",
            price=20.0,
            stock_quantity=2,
            supplier_id="S-003",
            reorder_level=2,
        )
    )

    with pytest.raises(ValueError, match="Insufficient stock available"):
        inventory.sell_product("P-003", 5)


def test_add_stock_rejects_non_positive_quantity(tmp_path):
    inventory = Inventory(data_dir=str(tmp_path))
    inventory.add_product(
        Product(
            product_id="P-004",
            name="Laptop Stand",
            category="Accessories",
            price=25.0,
            stock_quantity=4,
            supplier_id="S-004",
            reorder_level=2,
        )
    )

    with pytest.raises(ValueError, match="Quantity must be greater than zero"):
        inventory.add_stock("P-004", 0)
