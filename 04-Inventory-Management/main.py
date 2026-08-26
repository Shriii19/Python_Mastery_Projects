from inventory import Inventory
from product import Product
from supplier import Supplier


def show_menu() -> None:
    print("\n=== Inventory Management Menu ===")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Add Supplier")
    print("6. View Suppliers")
    print("7. Update Supplier")
    print("8. Delete Supplier")
    print("9. Stock IN")
    print("10. Stock OUT")
    print("11. View Transactions")
    print("12. Low Stock Report")
    print("13. Inventory Summary")
    print("14. Exit")


def handle_add_product(inventory: Inventory) -> None:
    try:
        product = Product(
            product_id=input("Product ID: ").strip(),
            name=input("Name: ").strip(),
            category=input("Category: ").strip(),
            price=float(input("Price: ").strip()),
            stock_quantity=int(input("Stock quantity: ").strip()),
            supplier_id=input("Supplier ID (optional): ").strip() or None,
            reorder_level=int(input("Reorder level: ").strip()),
        )
        inventory.add_product(product)
        print("Product added successfully.")
    except (ValueError, TypeError) as exc:
        print(f"Error: {exc}")


def handle_add_supplier(inventory: Inventory) -> None:
    supplier = Supplier(
        supplier_id=input("Supplier ID: ").strip(),
        name=input("Name: ").strip(),
        phone=input("Phone: ").strip(),
        email=input("Email: ").strip(),
        address=input("Address: ").strip(),
    )
    try:
        inventory.add_supplier(supplier)
        print("Supplier added successfully.")
    except ValueError as exc:
        print(f"Error: {exc}")


def handle_view_products(inventory: Inventory) -> None:
    if not inventory.products:
        print("No products found.")
        return
    for product in inventory.products:
        product.display()


def handle_update_product(inventory: Inventory) -> None:
    product_id = input("Product ID: ").strip()
    try:
        inventory.update_product(
            product_id,
            name=input("New name: ").strip(),
            category=input("New category: ").strip(),
            price=float(input("New price: ").strip()),
            reorder_level=int(input("New reorder level: ").strip()),
        )
        print("Product updated successfully.")
    except ValueError as exc:
        print(f"Error: {exc}")


def handle_delete_product(inventory: Inventory) -> None:
    try:
        inventory.delete_product(input("Product ID: ").strip())
        print("Product deleted successfully.")
    except ValueError as exc:
        print(f"Error: {exc}")


def handle_view_suppliers(inventory: Inventory) -> None:
    if not inventory.suppliers:
        print("No suppliers found.")
        return
    for supplier in inventory.suppliers:
        supplier.display()


def handle_update_supplier(inventory: Inventory) -> None:
    supplier_id = input("Supplier ID: ").strip()
    try:
        inventory.update_supplier(
            supplier_id,
            name=input("New name: ").strip(),
            phone=input("New phone: ").strip(),
            email=input("New email: ").strip(),
            address=input("New address: ").strip(),
        )
        print("Supplier updated successfully.")
    except ValueError as exc:
        print(f"Error: {exc}")


def handle_delete_supplier(inventory: Inventory) -> None:
    try:
        inventory.delete_supplier(input("Supplier ID: ").strip())
        print("Supplier deleted successfully.")
    except ValueError as exc:
        print(f"Error: {exc}")


def handle_add_stock(inventory: Inventory) -> None:
    try:
        product_id = input("Product ID: ").strip()
        quantity = int(input("Quantity received: ").strip())
        supplier_id = input("Supplier ID (optional): ").strip() or None
        inventory.add_stock(product_id, quantity, supplier_id=supplier_id)
        print("Stock added successfully.")
    except ValueError as exc:
        print(f"Error: {exc}")


def handle_sell_product(inventory: Inventory) -> None:
    try:
        product_id = input("Product ID: ").strip()
        quantity = int(input("Quantity sold: ").strip())
        inventory.sell_product(product_id, quantity)
        print("Product sold successfully.")
    except ValueError as exc:
        print(f"Error: {exc}")


def handle_view_transactions(inventory: Inventory) -> None:
    product_id = input("Product ID: ").strip()
    history = inventory.get_transaction_history(product_id)
    if not history:
        print("No transactions found.")
        return
    for transaction in history:
        transaction.display()


def handle_low_stock(inventory: Inventory) -> None:
    products = inventory.get_low_stock_products()
    if not products:
        print("No low-stock products.")
        return
    for product in products:
        product.display()


def handle_summary(inventory: Inventory) -> None:
    summary = inventory.get_report_summary()
    print("\nInventory Summary")
    print(f"Total Products     : {summary['total_products']}")
    print(f"Total Suppliers    : {summary['total_suppliers']}")
    print(f"Total Stock        : {summary['total_stock']}")
    print(f"Inventory Value    : {summary['inventory_value']:.2f}")
    print(f"Low-Stock Products : {summary['low_stock_items']}")
    print(f"Total Transactions : {summary['total_transactions']}")


def main() -> None:
    inventory = Inventory()
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "14":
            print("Goodbye!")
            break

        if choice == "1":
            handle_add_product(inventory)
        elif choice == "2":
            handle_view_products(inventory)
        elif choice == "3":
            handle_update_product(inventory)
        elif choice == "4":
            handle_delete_product(inventory)
        elif choice == "5":
            handle_add_supplier(inventory)
        elif choice == "6":
            handle_view_suppliers(inventory)
        elif choice == "7":
            handle_update_supplier(inventory)
        elif choice == "8":
            handle_delete_supplier(inventory)
        elif choice == "9":
            handle_add_stock(inventory)
        elif choice == "10":
            handle_sell_product(inventory)
        elif choice == "11":
            handle_view_transactions(inventory)
        elif choice == "12":
            handle_low_stock(inventory)
        elif choice == "13":
            handle_summary(inventory)
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
