from inventory import Inventory
from product import Product


def test_get_low_stock_products_returns_items_below_or_equal_to_reorder_level(tmp_path):
    inventory = Inventory(data_dir=str(tmp_path))

    inventory.add_product(
        Product(
            product_id="P-001",
            name="Keyboard",
            category="Accessories",
            price=40.0,
            stock_quantity=3,
            supplier_id="S-001",
            reorder_level=5,
        )
    )
    inventory.add_product(
        Product(
            product_id="P-002",
            name="Monitor",
            category="Electronics",
            price=150.0,
            stock_quantity=10,
            supplier_id="S-002",
            reorder_level=4,
        )
    )
    inventory.add_product(
        Product(
            product_id="P-003",
            name="Mouse",
            category="Accessories",
            price=20.0,
            stock_quantity=8,
            supplier_id="S-003",
            reorder_level=8,
        )
    )

    low_stock = inventory.get_low_stock_products()

    ids = [product.product_id for product in low_stock]
    assert "P-001" in ids
    assert "P-003" in ids
    assert "P-002" not in ids
    assert len(low_stock) == 2
