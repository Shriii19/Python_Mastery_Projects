class Patient:
    def __init__(self, patient_id: int, name: str, age: int, disease: str):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease

    def to_dict(self) -> dict:
        return {
            "patient_id": self.patient_id,
            "name": self.name,
            "age": self.age,
            "disease": self.disease,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            patient_id=int(data["patient_id"]),
            name=str(data["name"]),
            age=int(data["age"]),
            disease=str(data["disease"]),
        )
