class Supplier:
    def __init__(
        self,
        supplier_id: str,
        name: str,
        phone: str,
        email: str,
        address: str = "",
    ):
        self.supplier_id = supplier_id
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def to_dict(self) -> dict:
        return {
            "supplier_id": self.supplier_id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "address": self.address,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            supplier_id=str(data["supplier_id"]),
            name=str(data["name"]),
            phone=str(data["phone"]),
            email=str(data["email"]),
            address=str(data.get("address", "")),
        )

    def display(self) -> None:
        print("-" * 40)
        print(f"Supplier ID : {self.supplier_id}")
        print(f"Name        : {self.name}")
        print(f"Phone       : {self.phone}")
        print(f"Email       : {self.email}")
        print(f"Address     : {self.address}")
