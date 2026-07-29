from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"

PATIENT_FILE = str(DATA_DIR / "patients.json")
DOCTOR_FILE = str(DATA_DIR / "doctors.json")
APPOINTMENT_FILE = str(DATA_DIR / "appointments.json")
LOG_FILE = str(LOG_DIR / "hospital.log")
