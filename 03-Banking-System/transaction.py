class Transaction:
    def __init__(
        self,
        transaction_id: str,
        transaction_type: str,
        account_number: str,
        amount: float,
        timestamp: str,
        description: str = "",
    ):
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.account_number = account_number
        self.amount = float(amount)
        self.timestamp = timestamp
        self.description = description

    def to_dict(self) -> dict:
        return {
            "transaction_id": self.transaction_id,
            "transaction_type": self.transaction_type,
            "account_number": self.account_number,
            "amount": self.amount,
            "timestamp": self.timestamp,
            "description": self.description,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            transaction_id=str(data["transaction_id"]),
            transaction_type=str(data["transaction_type"]),
            account_number=str(data["account_number"]),
            amount=float(data["amount"]),
            timestamp=str(data["timestamp"]),
            description=str(data.get("description", "")),
        )

    def display(self) -> None:
        print("-" * 40)
        print(f"Transaction ID : {self.transaction_id}")
        print(f"Type           : {self.transaction_type}")
        print(f"Account No     : {self.account_number}")
        print(f"Amount         : {self.amount:.2f}")
        print(f"Timestamp      : {self.timestamp}")
        print(f"Description    : {self.description}")
