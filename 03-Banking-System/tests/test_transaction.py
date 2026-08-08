from transaction import Transaction


def test_transaction_serialization():
    tx = Transaction(
        transaction_id="TXN-1001",
        transaction_type="deposit",
        account_number="ACC-001",
        amount=150.0,
        timestamp="2026-08-08 10:00:00",
        description="Initial deposit",
    )

    data = tx.to_dict()

    assert data["transaction_id"] == "TXN-1001"
    assert data["transaction_type"] == "deposit"
    assert data["amount"] == 150.0

    restored = Transaction.from_dict(data)

    assert restored.transaction_id == tx.transaction_id
    assert restored.account_number == tx.account_number
    assert restored.amount == tx.amount
