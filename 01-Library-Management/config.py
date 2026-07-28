from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
BOOK_FILE = str(BASE_DIR / "data" / "books.json")
STUDENT_FILE = str(BASE_DIR / "data" / "students.json")