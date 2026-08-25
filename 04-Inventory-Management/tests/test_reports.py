from inventory import Inventory
from product import Product
from supplier import Supplier


def test_get_report_summary_returns_expected_metrics(tmp_path):
    inventory = Inventory(data_dir=str(tmp_path))

    inventory.add_supplier(
        Supplier(
            supplier_id="S-001",
            name="Tech Supply Co.",
            phone="1234567890",
            email="tech@example.com",
            address="Main Street",
        )
    )
    inventory.add_supplier(
        Supplier(
            supplier_id="S-002",
            name="Office Goods",
            phone="0987654321",
            email="office@example.com",
            address="Second Street",
        )
    )

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

    summary = inventory.get_report_summary()

    assert summary["total_products"] == 2
    assert summary["total_suppliers"] == 2
    assert summary["total_stock"] == 13
    assert summary["inventory_value"] == 40.0 * 3 + 150.0 * 10
    assert summary["low_stock_items"] == 1
    assert summary["total_transactions"] == 0
