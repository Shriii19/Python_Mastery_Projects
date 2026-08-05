import hospital as hospital_module
from appointment import Appointment
from doctor import Doctor
from hospital import Hospital
from patient import Patient


def make_hospital(tmp_path, monkeypatch) -> Hospital:
    patients_file = tmp_path / "patients.json"
    doctors_file = tmp_path / "doctors.json"
    appointments_file = tmp_path / "appointments.json"

    monkeypatch.setattr(hospital_module, "PATIENT_FILE", str(patients_file))
    monkeypatch.setattr(hospital_module, "DOCTOR_FILE", str(doctors_file))
    monkeypatch.setattr(hospital_module, "APPOINTMENT_FILE", str(appointments_file))

    return Hospital()


def test_hospital_initializes(tmp_path, monkeypatch):
    hospital = make_hospital(tmp_path, monkeypatch)

    assert isinstance(hospital.patients, list)
    assert isinstance(hospital.doctors, list)
    assert isinstance(hospital.appointments, list)


def test_patient_crud_and_search(tmp_path, monkeypatch):
    hospital = make_hospital(tmp_path, monkeypatch)

    assert hospital.add_patient(Patient(1, "Alice", 30, "Flu")) is True
    assert hospital.add_patient(Patient(1, "Alice", 30, "Flu")) is False

    patient = hospital.search_patient(1)
    assert patient is not None
    assert patient.name == "Alice"

    assert hospital.update_patient(1, "Alice Updated", 31, "Cold") is True
    assert hospital.search_patient(1).name == "Alice Updated"
    assert hospital.update_patient(999, "X", 20, "Y") is False

    assert hospital.delete_patient(1) is True
    assert hospital.search_patient(1) is None
    assert hospital.delete_patient(999) is False


def test_doctor_crud_and_search(tmp_path, monkeypatch):
    hospital = make_hospital(tmp_path, monkeypatch)

    assert hospital.add_doctor(Doctor(10, "Dr. Bob", "Cardiology")) is True
    assert hospital.add_doctor(Doctor(10, "Dr. Bob", "Cardiology")) is False

    doctor = hospital.search_doctor(10)
    assert doctor is not None
    assert doctor.name == "Dr. Bob"

    assert hospital.update_doctor(10, "Dr. Bob Updated", "Neurology") is True
    assert hospital.search_doctor(10).specialization == "Neurology"
    assert hospital.update_doctor(404, "Ghost", "None") is False

    assert hospital.remove_doctor(10) is True
    assert hospital.search_doctor(10) is None
    assert hospital.remove_doctor(404) is False


def test_appointment_booking_validation_and_cancel(tmp_path, monkeypatch):
    hospital = make_hospital(tmp_path, monkeypatch)

    hospital.add_patient(Patient(1, "Alice", 30, "Flu"))
    hospital.add_doctor(Doctor(10, "Dr. Bob", "Cardiology"))

    assert hospital.book_appointment(Appointment(100, 1, 10, "2026-08-05 09:00")) is True
    assert hospital.book_appointment(Appointment(100, 1, 10, "2026-08-05 09:00")) is False
    assert hospital.book_appointment(Appointment(101, 999, 10, "2026-08-05 10:00")) is False
    assert hospital.book_appointment(Appointment(102, 1, 999, "2026-08-05 11:00")) is False

    assert hospital.cancel_appointment(100) is True
    assert hospital.cancel_appointment(100) is False


def test_reports_and_cascade_behavior(tmp_path, monkeypatch):
    hospital = make_hospital(tmp_path, monkeypatch)

    hospital.add_patient(Patient(1, "Alice", 30, "Flu"))
    hospital.add_patient(Patient(2, "John", 42, "Fever"))
    hospital.add_doctor(Doctor(10, "Dr. Bob", "Cardiology"))
    hospital.add_doctor(Doctor(11, "Dr. Eve", "Dermatology"))
    hospital.book_appointment(Appointment(100, 1, 10, "2026-08-05 09:00"))

    reports = hospital.get_reports()
    assert reports["total_patients"] == 2
    assert reports["total_doctors"] == 2
    assert reports["total_appointments"] == 1
    assert len(reports["available_doctors"]) == 1
    assert reports["available_doctors"][0].doctor_id == 11
    assert reports["appointment_summary"][0]["appointment_id"] == 100

    assert hospital.delete_patient(1) is True
    assert len(hospital.appointments) == 0


def test_persistence_across_reloads(tmp_path, monkeypatch):
    hospital = make_hospital(tmp_path, monkeypatch)
    hospital.add_patient(Patient(1, "Alice", 30, "Flu"))
    hospital.add_doctor(Doctor(10, "Dr. Bob", "Cardiology"))
    hospital.book_appointment(Appointment(100, 1, 10, "2026-08-05 09:00"))

    reloaded = Hospital()
    assert len(reloaded.patients) == 1
    assert len(reloaded.doctors) == 1
    assert len(reloaded.appointments) == 1
