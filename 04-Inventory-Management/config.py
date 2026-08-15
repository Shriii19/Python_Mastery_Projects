from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"

PRODUCTS_FILE = DATA_DIR / "products.json"
SUPPLIERS_FILE = DATA_DIR / "suppliers.json"
TRANSACTIONS_FILE = DATA_DIR / "transactions.json"
LOG_FILE = LOG_DIR / "inventory.log"

DATA_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)
