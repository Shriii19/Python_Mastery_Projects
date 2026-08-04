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
    print("3. Search Patient")
    print("4. Update Patient")
    print("5. Delete Patient")
    print("6. Add Doctor")
    print("7. View Doctors")
    print("8. Search Doctor")
    print("9. Update Doctor")
    print("10. Remove Doctor")
    print("11. Book Appointment")
    print("12. View Appointments")
    print("13. Cancel Appointment")
    print("14. View Reports")
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
        patient_id = get_int_input("Patient ID to search: ")
        if patient_id is None:
            continue

        patient = hospital.search_patient(patient_id)
        if patient is None:
            print("Patient ID not found.")
        else:
            print(
                f"ID: {patient.patient_id}, Name: {patient.name}, "
                f"Age: {patient.age}, Disease: {patient.disease}"
            )

    elif choice == "4":
        patient_id = get_int_input("Patient ID to update: ")
        if patient_id is None:
            continue

        name = input("New Patient Name: ").strip()
        age = get_int_input("New Age: ")
        if age is None:
            continue
        disease = input("New Disease: ").strip()
        hospital.update_patient(patient_id, name, age, disease)

    elif choice == "5":
        patient_id = get_int_input("Patient ID to delete: ")
        if patient_id is None:
            continue
        hospital.delete_patient(patient_id)

    elif choice == "6":
        doctor_id = get_int_input("Doctor ID: ")
        if doctor_id is None:
            continue

        name = input("Doctor Name: ").strip()
        specialization = input("Specialization: ").strip()
        hospital.add_doctor(Doctor(doctor_id, name, specialization))

    elif choice == "7":
        hospital.view_doctors()

    elif choice == "8":
        doctor_id = get_int_input("Doctor ID to search: ")
        if doctor_id is None:
            continue

        doctor = hospital.search_doctor(doctor_id)
        if doctor is None:
            print("Doctor ID not found.")
        else:
            print(
                f"ID: {doctor.doctor_id}, Name: {doctor.name}, "
                f"Specialization: {doctor.specialization}"
            )

    elif choice == "9":
        doctor_id = get_int_input("Doctor ID to update: ")
        if doctor_id is None:
            continue

        name = input("New Doctor Name: ").strip()
        specialization = input("New Specialization: ").strip()
        hospital.update_doctor(doctor_id, name, specialization)

    elif choice == "10":
        doctor_id = get_int_input("Doctor ID to remove: ")
        if doctor_id is None:
            continue
        hospital.remove_doctor(doctor_id)

    elif choice == "11":
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

    elif choice == "12":
        hospital.view_appointments()

    elif choice == "13":
        appointment_id = get_int_input("Appointment ID to cancel: ")
        if appointment_id is None:
            continue
        hospital.cancel_appointment(appointment_id)

    elif choice == "14":
        hospital.view_reports()

    elif choice == "0":
        print("Thank you.")
        break

    else:
        print("Invalid choice.")
