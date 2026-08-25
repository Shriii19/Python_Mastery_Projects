from config import LOG_FILE
from logger import log


def test_log_writes_message_to_file():
    log("inventory test message")

    assert LOG_FILE.exists()
    contents = LOG_FILE.read_text(encoding="utf-8")
    assert "inventory test message" in contents
