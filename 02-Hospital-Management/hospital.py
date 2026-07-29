import json
from pathlib import Path

from appointment import Appointment
from config import APPOINTMENT_FILE, DOCTOR_FILE, PATIENT_FILE
from doctor import Doctor
from logger import log
from patient import Patient


class Hospital:
    def __init__(self):
        self.patients = self._load_items(PATIENT_FILE, Patient)
        self.doctors = self._load_items(DOCTOR_FILE, Doctor)
        self.appointments = self._load_items(APPOINTMENT_FILE, Appointment)

    @staticmethod
    def _ensure_json_file(file_path: str) -> None:
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        if not path.exists():
            path.write_text("[]", encoding="utf-8")

    def _load_items(self, file_path: str, cls):
        self._ensure_json_file(file_path)

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        return [cls.from_dict(item) for item in data]

    @staticmethod
    def _save_items(file_path: str, items: list) -> None:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump([item.to_dict() for item in items], file, indent=4)

    def add_patient(self, patient: Patient) -> bool:
        if any(p.patient_id == patient.patient_id for p in self.patients):
            print("Patient ID already exists.")
            return False

        self.patients.append(patient)
        self._save_items(PATIENT_FILE, self.patients)
        log(f"Added patient: {patient.patient_id} - {patient.name}")
        print("Patient added successfully.")
        return True

    def add_doctor(self, doctor: Doctor) -> bool:
        if any(d.doctor_id == doctor.doctor_id for d in self.doctors):
            print("Doctor ID already exists.")
            return False

        self.doctors.append(doctor)
        self._save_items(DOCTOR_FILE, self.doctors)
        log(f"Added doctor: {doctor.doctor_id} - {doctor.name}")
        print("Doctor added successfully.")
        return True

    def book_appointment(self, appointment: Appointment) -> bool:
        if any(a.appointment_id == appointment.appointment_id for a in self.appointments):
            print("Appointment ID already exists.")
            return False

        if not any(p.patient_id == appointment.patient_id for p in self.patients):
            print("Patient ID not found.")
            return False

        if not any(d.doctor_id == appointment.doctor_id for d in self.doctors):
            print("Doctor ID not found.")
            return False

        self.appointments.append(appointment)
        self._save_items(APPOINTMENT_FILE, self.appointments)
        log(
            "Booked appointment: "
            f"{appointment.appointment_id} (Patient {appointment.patient_id} -> Doctor {appointment.doctor_id})"
        )
        print("Appointment booked successfully.")
        return True

    def view_patients(self) -> None:
        if not self.patients:
            print("No patients found.")
            return

        print("\nPatients:")
        for patient in self.patients:
            print(
                f"ID: {patient.patient_id}, Name: {patient.name}, "
                f"Age: {patient.age}, Disease: {patient.disease}"
            )

    def view_doctors(self) -> None:
        if not self.doctors:
            print("No doctors found.")
            return

        print("\nDoctors:")
        for doctor in self.doctors:
            print(
                f"ID: {doctor.doctor_id}, Name: {doctor.name}, "
                f"Specialization: {doctor.specialization}"
            )

    def view_appointments(self) -> None:
        if not self.appointments:
            print("No appointments found.")
            return

        print("\nAppointments:")
        for appointment in self.appointments:
            print(
                f"ID: {appointment.appointment_id}, Patient ID: {appointment.patient_id}, "
                f"Doctor ID: {appointment.doctor_id}, Schedule: {appointment.schedule}"
            )
