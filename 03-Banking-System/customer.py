class Customer:
    def __init__(
        self,
        customer_id: int,
        name: str,
        phone: str,
        email: str,
        account_numbers: list[str] | None = None,
    ):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.email = email
        self.account_numbers = account_numbers if account_numbers is not None else []

    def to_dict(self) -> dict:
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "account_numbers": self.account_numbers,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            customer_id=int(data["customer_id"]),
            name=str(data["name"]),
            phone=str(data["phone"]),
            email=str(data["email"]),
            account_numbers=list(data.get("account_numbers", [])),
        )

    def display(self) -> None:
        print("-" * 40)
        print(f"Customer ID : {self.customer_id}")
        print(f"Name        : {self.name}")
        print(f"Phone       : {self.phone}")
        print(f"Email       : {self.email}")
        print(f"Accounts    : {self.account_numbers}")
