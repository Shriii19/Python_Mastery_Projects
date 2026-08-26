import json
from datetime import datetime
from pathlib import Path

from inventory_transaction import InventoryTransaction
from logger import log
from product import Product
from supplier import Supplier


class Inventory:
    def __init__(self, data_dir: str | None = None):
        self.base_dir = Path(data_dir) if data_dir else Path(__file__).resolve().parent
        self.data_dir = self.base_dir / "data" if data_dir is None else Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)

        self.products_file = self.data_dir / "products.json"
        self.suppliers_file = self.data_dir / "suppliers.json"
        self.transactions_file = self.data_dir / "transactions.json"

        self.products = self._load_products()
        self.suppliers = self._load_suppliers()
        self.transactions = self._load_transactions()

    def _load_products(self) -> list[Product]:
        if not self.products_file.exists():
            return []
        with self.products_file.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
        return [Product.from_dict(item) for item in data]

    def _load_suppliers(self) -> list[Supplier]:
        if not self.suppliers_file.exists():
            return []
        with self.suppliers_file.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
        return [Supplier.from_dict(item) for item in data]

    def _load_transactions(self) -> list[InventoryTransaction]:
        if not self.transactions_file.exists():
            return []
        with self.transactions_file.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
        return [InventoryTransaction.from_dict(item) for item in data]

    def _save_products(self) -> None:
        with self.products_file.open("w", encoding="utf-8") as fh:
            json.dump([product.to_dict() for product in self.products], fh, indent=4)

    def _save_suppliers(self) -> None:
        with self.suppliers_file.open("w", encoding="utf-8") as fh:
            json.dump([supplier.to_dict() for supplier in self.suppliers], fh, indent=4)

    def _save_transactions(self) -> None:
        with self.transactions_file.open("w", encoding="utf-8") as fh:
            json.dump([transaction.to_dict() for transaction in self.transactions], fh, indent=4)

    def save_all(self) -> None:
        self._save_products()
        self._save_suppliers()
        self._save_transactions()

    def add_product(self, product: Product) -> None:
        for existing_product in self.products:
            if existing_product.product_id == product.product_id:
                raise ValueError("Product already exists.")

        self.products.append(product)
        self._save_products()
        log(f"Product added: {product.product_id} - {product.name}")

    def add_supplier(self, supplier: Supplier) -> None:
        for existing_supplier in self.suppliers:
            if existing_supplier.supplier_id == supplier.supplier_id:
                raise ValueError("Supplier already exists.")

        self.suppliers.append(supplier)
        self._save_suppliers()
        log(f"Supplier added: {supplier.supplier_id} - {supplier.name}")

    def add_transaction(self, transaction: InventoryTransaction) -> None:
        self.transactions.append(transaction)
        self._save_transactions()
        log(f"Transaction recorded: {transaction.transaction_id} - {transaction.transaction_type}")

    def get_product(self, product_id: str) -> Product | None:
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

    def update_product(self, product_id: str, **kwargs) -> None:
        product = self.get_product(product_id)
        if product is None:
            raise ValueError("Product not found.")

        supported_fields = {"name", "category", "price", "stock_quantity", "supplier_id", "reorder_level"}
        unknown_fields = set(kwargs) - supported_fields
        if unknown_fields:
            raise ValueError(f"Unsupported product fields: {', '.join(sorted(unknown_fields))}.")

        if "name" in kwargs:
            product.name = str(kwargs["name"])
        if "category" in kwargs:
            product.category = str(kwargs["category"])
        if "price" in kwargs:
            price = float(kwargs["price"])
            if price < 0:
                raise ValueError("Price cannot be negative.")
            product.price = price
        if "stock_quantity" in kwargs:
            stock_quantity = int(kwargs["stock_quantity"])
            if stock_quantity < 0:
                raise ValueError("Stock quantity cannot be negative.")
            product.stock_quantity = stock_quantity
        if "supplier_id" in kwargs:
            product.supplier_id = kwargs["supplier_id"]
        if "reorder_level" in kwargs:
            reorder_level = int(kwargs["reorder_level"])
            if reorder_level < 0:
                raise ValueError("Reorder level cannot be negative.")
            product.reorder_level = reorder_level

        self._save_products()
        log(f"Product updated: {product_id}")

    def delete_product(self, product_id: str) -> None:
        product = self.get_product(product_id)
        if product is None:
            raise ValueError("Product not found.")

        self.products = [p for p in self.products if p.product_id != product_id]
        self._save_products()
        log(f"Product deleted: {product_id}")

    def get_supplier(self, supplier_id: str) -> Supplier | None:
        for supplier in self.suppliers:
            if supplier.supplier_id == supplier_id:
                return supplier
        return None

    def update_supplier(self, supplier_id: str, **kwargs) -> None:
        supplier = self.get_supplier(supplier_id)
        if supplier is None:
            raise ValueError("Supplier not found.")

        if "name" in kwargs:
            supplier.name = str(kwargs["name"])
        if "phone" in kwargs:
            supplier.phone = str(kwargs["phone"])
        if "email" in kwargs:
            supplier.email = str(kwargs["email"])
        if "address" in kwargs:
            supplier.address = str(kwargs["address"])

        self._save_suppliers()
        log(f"Supplier updated: {supplier_id}")

    def delete_supplier(self, supplier_id: str) -> None:
        supplier = self.get_supplier(supplier_id)
        if supplier is None:
            raise ValueError("Supplier not found.")

        self.suppliers = [s for s in self.suppliers if s.supplier_id != supplier_id]
        self._save_suppliers()
        log(f"Supplier deleted: {supplier_id}")

    def add_stock(self, product_id: str, quantity: int, supplier_id: str | None = None, description: str = "Stock received") -> InventoryTransaction:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        product = self.get_product(product_id)
        if product is None:
            raise ValueError("Product not found.")

        product.stock_quantity += quantity
        transaction = InventoryTransaction(
            transaction_id=f"INV-{len(self.transactions) + 1:04d}",
            product_id=product_id,
            transaction_type="purchase",
            quantity=quantity,
            unit_price=product.price,
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            supplier_id=supplier_id,
            description=description,
        )

        self.transactions.append(transaction)
        self._save_products()
        self._save_transactions()
        log(f"Stock added: {product_id} quantity {quantity}")
        return transaction

    def sell_product(self, product_id: str, quantity: int, description: str = "Sale") -> InventoryTransaction:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        product = self.get_product(product_id)
        if product is None:
            raise ValueError("Product not found.")
        if product.stock_quantity < quantity:
            raise ValueError("Insufficient stock available.")

        product.stock_quantity -= quantity
        transaction = InventoryTransaction(
            transaction_id=f"INV-{len(self.transactions) + 1:04d}",
            product_id=product_id,
            transaction_type="sale",
            quantity=quantity,
            unit_price=product.price,
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            description=description,
        )

        self.transactions.append(transaction)
        self._save_products()
        self._save_transactions()
        log(f"Product sold: {product_id} quantity {quantity}")
        return transaction

    def get_inventory_value(self) -> float:
        return sum(product.price * product.stock_quantity for product in self.products)

    def get_low_stock_products(self) -> list[Product]:
        return [product for product in self.products if product.stock_quantity <= product.reorder_level]

    def get_transaction_history(self, product_id: str) -> list[InventoryTransaction]:
        return [transaction for transaction in self.transactions if transaction.product_id == product_id]

    def get_report_summary(self) -> dict:
        return {
            "total_products": len(self.products),
            "total_suppliers": len(self.suppliers),
            "total_stock": sum(product.stock_quantity for product in self.products),
            "inventory_value": self.get_inventory_value(),
            "low_stock_items": len(self.get_low_stock_products()),
            "total_transactions": len(self.transactions),
        }
