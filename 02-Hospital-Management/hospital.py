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

    @staticmethod
    def _find_index_by_attr(items: list, attr: str, value: int) -> int:
        for index, item in enumerate(items):
            if getattr(item, attr) == value:
                return index
        return -1

    def add_patient(self, patient: Patient) -> bool:
        if any(p.patient_id == patient.patient_id for p in self.patients):
            print("Patient ID already exists.")
            return False

        self.patients.append(patient)
        self._save_items(PATIENT_FILE, self.patients)
        log(f"Added patient: {patient.patient_id} - {patient.name}")
        print("Patient added successfully.")
        return True

    def search_patient(self, patient_id: int) -> Patient | None:
        for patient in self.patients:
            if patient.patient_id == patient_id:
                return patient
        return None

    def update_patient(self, patient_id: int, name: str, age: int, disease: str) -> bool:
        patient = self.search_patient(patient_id)
        if patient is None:
            print("Patient ID not found.")
            return False

        patient.name = name
        patient.age = age
        patient.disease = disease
        self._save_items(PATIENT_FILE, self.patients)
        log(f"Updated patient: {patient.patient_id} - {patient.name}")
        print("Patient updated successfully.")
        return True

    def delete_patient(self, patient_id: int) -> bool:
        index = self._find_index_by_attr(self.patients, "patient_id", patient_id)
        if index == -1:
            print("Patient ID not found.")
            return False

        removed_patient = self.patients.pop(index)
        removed_count = len(
            [a for a in self.appointments if a.patient_id == removed_patient.patient_id]
        )
        self.appointments = [
            appointment
            for appointment in self.appointments
            if appointment.patient_id != removed_patient.patient_id
        ]
        self._save_items(PATIENT_FILE, self.patients)
        self._save_items(APPOINTMENT_FILE, self.appointments)
        log(
            f"Deleted patient: {removed_patient.patient_id} - {removed_patient.name}; "
            f"removed appointments: {removed_count}"
        )
        print("Patient deleted successfully.")
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

    def search_doctor(self, doctor_id: int) -> Doctor | None:
        for doctor in self.doctors:
            if doctor.doctor_id == doctor_id:
                return doctor
        return None

    def update_doctor(self, doctor_id: int, name: str, specialization: str) -> bool:
        doctor = self.search_doctor(doctor_id)
        if doctor is None:
            print("Doctor ID not found.")
            return False

        doctor.name = name
        doctor.specialization = specialization
        self._save_items(DOCTOR_FILE, self.doctors)
        log(f"Updated doctor: {doctor.doctor_id} - {doctor.name}")
        print("Doctor updated successfully.")
        return True

    def remove_doctor(self, doctor_id: int) -> bool:
        index = self._find_index_by_attr(self.doctors, "doctor_id", doctor_id)
        if index == -1:
            print("Doctor ID not found.")
            return False

        removed_doctor = self.doctors.pop(index)
        removed_count = len(
            [a for a in self.appointments if a.doctor_id == removed_doctor.doctor_id]
        )
        self.appointments = [
            appointment
            for appointment in self.appointments
            if appointment.doctor_id != removed_doctor.doctor_id
        ]
        self._save_items(DOCTOR_FILE, self.doctors)
        self._save_items(APPOINTMENT_FILE, self.appointments)
        log(
            f"Removed doctor: {removed_doctor.doctor_id} - {removed_doctor.name}; "
            f"removed appointments: {removed_count}"
        )
        print("Doctor removed successfully.")
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

    def cancel_appointment(self, appointment_id: int) -> bool:
        index = self._find_index_by_attr(
            self.appointments, "appointment_id", appointment_id
        )
        if index == -1:
            print("Appointment ID not found.")
            return False

        removed_appointment = self.appointments.pop(index)
        self._save_items(APPOINTMENT_FILE, self.appointments)
        log(
            "Canceled appointment: "
            f"{removed_appointment.appointment_id} (Patient {removed_appointment.patient_id} "
            f"-> Doctor {removed_appointment.doctor_id})"
        )
        print("Appointment canceled successfully.")
        return True

    def get_reports(self) -> dict:
        doctor_ids_with_appointments = {a.doctor_id for a in self.appointments}
        available_doctors = [
            doctor for doctor in self.doctors if doctor.doctor_id not in doctor_ids_with_appointments
        ]

        return {
            "total_patients": len(self.patients),
            "total_doctors": len(self.doctors),
            "total_appointments": len(self.appointments),
            "available_doctors": available_doctors,
            "appointment_summary": [
                {
                    "appointment_id": appointment.appointment_id,
                    "patient_id": appointment.patient_id,
                    "doctor_id": appointment.doctor_id,
                    "schedule": appointment.schedule,
                }
                for appointment in self.appointments
            ],
        }

    def view_reports(self) -> None:
        reports = self.get_reports()

        print("\nReports:")
        print(f"Total Patients: {reports['total_patients']}")
        print(f"Total Doctors: {reports['total_doctors']}")
        print(f"Total Appointments: {reports['total_appointments']}")

        print("\nAvailable Doctors:")
        if not reports["available_doctors"]:
            print("No available doctors.")
        else:
            for doctor in reports["available_doctors"]:
                print(
                    f"ID: {doctor.doctor_id}, Name: {doctor.name}, "
                    f"Specialization: {doctor.specialization}"
                )

        print("\nAppointment Summary:")
        if not reports["appointment_summary"]:
            print("No appointments found.")
        else:
            for appointment in reports["appointment_summary"]:
                print(
                    f"ID: {appointment['appointment_id']}, "
                    f"Patient ID: {appointment['patient_id']}, "
                    f"Doctor ID: {appointment['doctor_id']}, "
                    f"Schedule: {appointment['schedule']}"
                )

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
