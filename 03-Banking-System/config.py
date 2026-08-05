from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"

CUSTOMER_FILE = str(DATA_DIR / "customers.json")
ACCOUNT_FILE = str(DATA_DIR / "accounts.json")
TRANSACTION_FILE = str(DATA_DIR / "transactions.json")
LOG_FILE = str(LOG_DIR / "banking.log")
