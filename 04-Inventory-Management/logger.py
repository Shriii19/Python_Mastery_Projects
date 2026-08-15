import logging
from pathlib import Path

from config import LOG_FILE

Path(LOG_FILE).parent.mkdir(parents=True, exist_ok=True)

logger = logging.getLogger("inventory_system")
logger.setLevel(logging.INFO)
logger.propagate = False

if not logger.handlers:
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(file_handler)


def log(message: str) -> None:
    logger.info(message)
