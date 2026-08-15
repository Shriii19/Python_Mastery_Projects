class Product:
    def __init__(
        self,
        product_id: str,
        name: str,
        category: str,
        price: float,
        stock_quantity: int,
        supplier_id: str | None = None,
        reorder_level: int = 0,
    ):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = float(price)
        self.stock_quantity = int(stock_quantity)
        self.supplier_id = supplier_id
        self.reorder_level = int(reorder_level)

    def to_dict(self) -> dict:
        return {
            "product_id": self.product_id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "stock_quantity": self.stock_quantity,
            "supplier_id": self.supplier_id,
            "reorder_level": self.reorder_level,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            product_id=str(data["product_id"]),
            name=str(data["name"]),
            category=str(data["category"]),
            price=float(data.get("price", 0.0)),
            stock_quantity=int(data.get("stock_quantity", 0)),
            supplier_id=data.get("supplier_id"),
            reorder_level=int(data.get("reorder_level", 0)),
        )

    def display(self) -> None:
        print("-" * 40)
        print(f"Product ID     : {self.product_id}")
        print(f"Name           : {self.name}")
        print(f"Category       : {self.category}")
        print(f"Price          : {self.price:.2f}")
        print(f"Stock Quantity : {self.stock_quantity}")
        print(f"Supplier ID    : {self.supplier_id}")
        print(f"Reorder Level  : {self.reorder_level}")
