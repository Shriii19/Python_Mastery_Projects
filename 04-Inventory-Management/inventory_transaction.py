class InventoryTransaction:
    def __init__(
        self,
        transaction_id: str,
        product_id: str,
        transaction_type: str,
        quantity: int,
        unit_price: float,
        timestamp: str,
        supplier_id: str | None = None,
        description: str = "",
    ):
        self.transaction_id = transaction_id
        self.product_id = product_id
        self.transaction_type = transaction_type
        self.quantity = int(quantity)
        self.unit_price = float(unit_price)
        self.timestamp = timestamp
        self.supplier_id = supplier_id
        self.description = description

    def to_dict(self) -> dict:
        return {
            "transaction_id": self.transaction_id,
            "product_id": self.product_id,
            "transaction_type": self.transaction_type,
            "quantity": self.quantity,
            "unit_price": self.unit_price,
            "timestamp": self.timestamp,
            "supplier_id": self.supplier_id,
            "description": self.description,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            transaction_id=str(data["transaction_id"]),
            product_id=str(data["product_id"]),
            transaction_type=str(data["transaction_type"]),
            quantity=int(data.get("quantity", 0)),
            unit_price=float(data.get("unit_price", 0.0)),
            timestamp=str(data["timestamp"]),
            supplier_id=data.get("supplier_id"),
            description=str(data.get("description", "")),
        )

    def display(self) -> None:
        print("-" * 40)
        print(f"Transaction ID : {self.transaction_id}")
        print(f"Product ID     : {self.product_id}")
        print(f"Type           : {self.transaction_type}")
        print(f"Quantity       : {self.quantity}")
        print(f"Unit Price     : {self.unit_price:.2f}")
        print(f"Timestamp      : {self.timestamp}")
        print(f"Supplier ID    : {self.supplier_id}")
        print(f"Description    : {self.description}")
