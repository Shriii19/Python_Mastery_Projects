class Doctor:
    def __init__(self, doctor_id: int, name: str, specialization: str):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization

    def to_dict(self) -> dict:
        return {
            "doctor_id": self.doctor_id,
            "name": self.name,
            "specialization": self.specialization,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            doctor_id=int(data["doctor_id"]),
            name=str(data["name"]),
            specialization=str(data["specialization"]),
        )
