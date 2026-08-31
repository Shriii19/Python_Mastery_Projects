import logging

from config import LOG_FILE

logger = logging.getLogger("csv_data_analyzer")
logger.setLevel(logging.INFO)
logger.propagate = False

if not logger.handlers:
	file_handler = logging.FileHandler(LOG_FILE)
	file_handler.setLevel(logging.INFO)
	file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
	logger.addHandler(file_handler)


def log(message: str) -> None:
	logger.info(message)