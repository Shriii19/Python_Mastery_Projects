import pytest

from inventory import Inventory
from product import Product


def test_add_product_raises_on_duplicate(tmp_path):
    inventory = Inventory(data_dir=str(tmp_path))
    product = Product(
        product_id="P-001",
        name="Keyboard",
        category="Accessories",
        price=40.0,
        stock_quantity=10,
        supplier_id="S-001",
        reorder_level=5,
    )

    inventory.add_product(product)

    with pytest.raises(ValueError, match="Product already exists"):
        inventory.add_product(product)


def test_sell_product_raises_on_missing_product(tmp_path):
    inventory = Inventory(data_dir=str(tmp_path))

    with pytest.raises(ValueError, match="Product not found"):
        inventory.sell_product("P-UNKNOWN", 1)


def test_add_stock_raises_on_invalid_quantity(tmp_path):
    inventory = Inventory(data_dir=str(tmp_path))
    inventory.add_product(
        Product(
            product_id="P-002",
            name="Mouse",
            category="Accessories",
            price=20.0,
            stock_quantity=5,
            supplier_id="S-001",
            reorder_level=2,
        )
    )

    with pytest.raises(ValueError, match="Quantity must be greater than zero"):
        inventory.add_stock("P-002", 0)
