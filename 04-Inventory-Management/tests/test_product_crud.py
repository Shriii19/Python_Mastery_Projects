import pytest

from inventory import Inventory
from product import Product


def test_add_product_rejects_duplicate_and_persists(tmp_path):
    inventory = Inventory(data_dir=str(tmp_path))

    product = Product(
        product_id="P-001",
        name="Wireless Mouse",
        category="Accessories",
        price=25.5,
        stock_quantity=20,
        supplier_id="S-001",
        reorder_level=5,
    )

    inventory.add_product(product)

    stored = inventory.get_product("P-001")
    assert stored is not None
    assert stored.name == "Wireless Mouse"
    assert inventory.products[0].product_id == "P-001"

    duplicate = Product(
        product_id="P-001",
        name="Duplicate Mouse",
        category="Accessories",
        price=30.0,
        stock_quantity=10,
        supplier_id="S-001",
        reorder_level=3,
    )

    with pytest.raises(ValueError, match="Product already exists"):
        inventory.add_product(duplicate)


def test_get_product_returns_none_for_unknown_product(tmp_path):
    inventory = Inventory(data_dir=str(tmp_path))

    assert inventory.get_product("P-UNKNOWN") is None


def test_update_product_modifies_fields(tmp_path):
    inventory = Inventory(data_dir=str(tmp_path))

    product = Product(
        product_id="P-001",
        name="Wireless Mouse",
        category="Accessories",
        price=25.5,
        stock_quantity=20,
        supplier_id="S-001",
        reorder_level=5,
    )

    inventory.add_product(product)

    inventory.update_product(
        "P-001",
        name="Wireless Gaming Mouse",
        price=35.99,
        stock_quantity=25,
        reorder_level=3,
    )

    updated = inventory.get_product("P-001")
    assert updated is not None
    assert updated.name == "Wireless Gaming Mouse"
    assert updated.price == 35.99
    assert updated.stock_quantity == 25
    assert updated.reorder_level == 3
    assert updated.category == "Accessories"
    assert updated.supplier_id == "S-001"


def test_update_product_raises_error_if_not_found(tmp_path):
    inventory = Inventory(data_dir=str(tmp_path))

    with pytest.raises(ValueError, match="Product not found"):
        inventory.update_product("P-UNKNOWN", name="New Name")
