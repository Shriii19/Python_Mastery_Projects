import logging
from pathlib import Path

from config import LOG_FILE

Path(LOG_FILE).parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def log(message: str) -> None:
    logging.info(message)
