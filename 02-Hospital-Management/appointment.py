class Appointment:
    def __init__(self, appointment_id: int, patient_id: int, doctor_id: int, schedule: str):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.schedule = schedule

    def to_dict(self) -> dict:
        return {
            "appointment_id": self.appointment_id,
            "patient_id": self.patient_id,
            "doctor_id": self.doctor_id,
            "schedule": self.schedule,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            appointment_id=int(data["appointment_id"]),
            patient_id=int(data["patient_id"]),
            doctor_id=int(data["doctor_id"]),
            schedule=str(data["schedule"]),
        )
