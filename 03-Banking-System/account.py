class Account:
    def __init__(
        self,
        account_number: str,
        customer_id: int,
        account_type: str,
        balance: float = 0.0,
        is_active: bool = True,
    ):
        self.account_number = account_number
        self.customer_id = customer_id
        self.account_type = account_type
        self.balance = float(balance)
        self.is_active = is_active

    def to_dict(self) -> dict:
        return {
            "account_number": self.account_number,
            "customer_id": self.customer_id,
            "account_type": self.account_type,
            "balance": self.balance,
            "is_active": self.is_active,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            account_number=str(data["account_number"]),
            customer_id=int(data["customer_id"]),
            account_type=str(data["account_type"]),
            balance=float(data.get("balance", 0.0)),
            is_active=bool(data.get("is_active", True)),
        )

    def display(self) -> None:
        print("-" * 40)
        print(f"Account No  : {self.account_number}")
        print(f"Customer ID : {self.customer_id}")
        print(f"Type        : {self.account_type}")
        print(f"Balance     : {self.balance:.2f}")
        print(f"Active      : {self.is_active}")
