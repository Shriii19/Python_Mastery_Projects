class Student:

    def __init__(self, student_id, name, phone):
        self.student_id = student_id
        self.name = name
        self.phone = phone
        self.borrowed_books = []

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "phone": self.phone,
            "borrowed_books": self.borrowed_books
        }

    @staticmethod
    def from_dict(data):
        student = Student(
            data["student_id"],
            data["name"],
            data["phone"]
        )
        student.borrowed_books = data.get("borrowed_books", [])
        return student

    def display(self):
        print("-" * 40)
        print(f"Student ID : {self.student_id}")
        print(f"Name       : {self.name}")
        print(f"Phone      : {self.phone}")
        print(f"Borrowed   : {self.borrowed_books}")

