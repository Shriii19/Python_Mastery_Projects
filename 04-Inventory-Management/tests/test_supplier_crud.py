import pytest

from inventory import Inventory
from supplier import Supplier


def test_add_supplier_rejects_duplicate_and_persists(tmp_path):
    inventory = Inventory(data_dir=str(tmp_path))

    supplier = Supplier(
        supplier_id="S-001",
        name="Tech Supply Co.",
        phone="1234567890",
        email="tech@example.com",
        address="Main Street",
    )

    inventory.add_supplier(supplier)
    stored = inventory.get_supplier("S-001")

    assert stored is not None
    assert stored.name == "Tech Supply Co."
    assert len(inventory.suppliers) == 1

    duplicate = Supplier(
        supplier_id="S-001",
        name="Another Supplier",
        phone="9876543210",
        email="another@example.com",
        address="Second Street",
    )

    with pytest.raises(ValueError, match="Supplier already exists"):
        inventory.add_supplier(duplicate)


def test_get_supplier_returns_none_for_unknown_supplier(tmp_path):
    inventory = Inventory(data_dir=str(tmp_path))

    assert inventory.get_supplier("S-UNKNOWN") is None


def test_update_supplier_modifies_fields(tmp_path):
    inventory = Inventory(data_dir=str(tmp_path))

    supplier = Supplier(
        supplier_id="S-001",
        name="Tech Supply Co.",
        phone="1234567890",
        email="tech@example.com",
        address="Main Street",
    )

    inventory.add_supplier(supplier)
    inventory.update_supplier(
        "S-001",
        name="Updated Supply Co.",
        phone="5550001111",
        email="updated@example.com",
        address="New Street",
    )

    updated = inventory.get_supplier("S-001")
    assert updated is not None
    assert updated.name == "Updated Supply Co."
    assert updated.phone == "5550001111"
    assert updated.email == "updated@example.com"
    assert updated.address == "New Street"


def test_update_supplier_raises_error_if_not_found(tmp_path):
    inventory = Inventory(data_dir=str(tmp_path))

    with pytest.raises(ValueError, match="Supplier not found"):
        inventory.update_supplier("S-UNKNOWN", name="New Name")


def test_delete_supplier_removes_from_inventory(tmp_path):
    inventory = Inventory(data_dir=str(tmp_path))

    supplier = Supplier(
        supplier_id="S-001",
        name="Tech Supply Co.",
        phone="1234567890",
        email="tech@example.com",
        address="Main Street",
    )

    inventory.add_supplier(supplier)
    inventory.delete_supplier("S-001")

    assert inventory.get_supplier("S-001") is None
    assert len(inventory.suppliers) == 0


def test_delete_supplier_raises_error_if_not_found(tmp_path):
    inventory = Inventory(data_dir=str(tmp_path))

    with pytest.raises(ValueError, match="Supplier not found"):
        inventory.delete_supplier("S-UNKNOWN")
