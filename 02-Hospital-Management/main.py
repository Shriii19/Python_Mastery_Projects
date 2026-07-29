from appointment import Appointment
from doctor import Doctor
from hospital import Hospital
from patient import Patient


hospital = Hospital()


def get_int_input(prompt: str):
    value = input(prompt).strip()

    try:
        return int(value)
    except ValueError:
        print("Please enter a valid number.")
        return None


while True:
    print("\n" + "=" * 40)
    print("HOSPITAL MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Add Doctor")
    print("4. View Doctors")
    print("5. Book Appointment")
    print("6. View Appointments")
    print("0. Exit")

    choice = input("\nEnter your choice: ").strip()

    if choice == "1":
        patient_id = get_int_input("Patient ID: ")
        if patient_id is None:
            continue

        name = input("Patient Name: ").strip()
        age = get_int_input("Age: ")
        if age is None:
            continue

        disease = input("Disease: ").strip()
        hospital.add_patient(Patient(patient_id, name, age, disease))

    elif choice == "2":
        hospital.view_patients()

    elif choice == "3":
        doctor_id = get_int_input("Doctor ID: ")
        if doctor_id is None:
            continue

        name = input("Doctor Name: ").strip()
        specialization = input("Specialization: ").strip()
        hospital.add_doctor(Doctor(doctor_id, name, specialization))

    elif choice == "4":
        hospital.view_doctors()

    elif choice == "5":
        appointment_id = get_int_input("Appointment ID: ")
        if appointment_id is None:
            continue

        patient_id = get_int_input("Patient ID: ")
        if patient_id is None:
            continue

        doctor_id = get_int_input("Doctor ID: ")
        if doctor_id is None:
            continue

        schedule = input("Schedule (e.g. 2026-07-30 14:30): ").strip()
        hospital.book_appointment(
            Appointment(appointment_id, patient_id, doctor_id, schedule)
        )

    elif choice == "6":
        hospital.view_appointments()

    elif choice == "0":
        print("Thank you.")
        break

    else:
        print("Invalid choice.")
