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
