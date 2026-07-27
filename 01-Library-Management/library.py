"""
Library Class

This file manages books and students.
"""

import json

from book import Book
from student import Student
from config import BOOK_FILE, STUDENT_FILE


class Library:
    """
    Represents the library.
    """

    def __init__(self):
        # Store all books
        self.books = []

        # Store all students
        self.students = []

        # Load saved data when the program starts
        self.load_books()
        self.load_students()

    # ======================================================
    # BOOK METHODS
    # ======================================================

    def add_book(self, book: Book):
        self.books.append(book)
        self.save_books()
        print(f"\n'{book.title}' added successfully!")

    def view_books(self):

        if not self.books:
            print("\nNo books available.")
            return

        print("\n========== BOOK LIST ==========")

        for book in self.books:
            book.display()

    def search_books(self, keyword: str):

        cleaned_keyword = keyword.strip().lower()

        if not cleaned_keyword:
            print("\nPlease enter a valid keyword.")
            return

        matched_books = []

        for book in self.books:

            if (
                cleaned_keyword in str(book.book_id).lower()
                or cleaned_keyword in book.title.lower()
                or cleaned_keyword in book.author.lower()
                or cleaned_keyword in book.category.lower()
            ):
                matched_books.append(book)

        if not matched_books:
            print("\nNo books matched your search.")
            return

        print("\n========== SEARCH RESULT ==========")

        for book in matched_books:
            book.display()

    def delete_book(self, book_id: int):

        for book in self.books:

            if book.book_id == book_id:
                self.books.remove(book)
                self.save_books()
                print(f"\nBook ID {book_id} deleted successfully!")
                return

        print(f"\nBook ID {book_id} not found.")

    # ======================================================
    # STUDENT METHODS
    # ======================================================

    def add_student(self, student: Student):
        self.students.append(student)
        self.save_students()
        print(f"\n{student.name} registered successfully!")

    def view_students(self):

        if not self.students:
            print("\nNo students found.")
            return

        print("\n========== STUDENT LIST ==========")

        for student in self.students:
            student.display()

    # ======================================================
    # SAVE BOOKS
    # ======================================================

    def save_books(self):

        data = []

        for book in self.books:
            data.append(book.to_dict())

        with open(BOOK_FILE, "w") as file:
            json.dump(data, file, indent=4)

    # ======================================================
    # LOAD BOOKS
    # ======================================================

    def load_books(self):

        try:

            with open(BOOK_FILE, "r") as file:

                data = json.load(file)

                self.books = []

                for item in data:

                    book = Book(
                        item["book_id"],
                        item["title"],
                        item["author"],
                        item["category"]
                    )

                    book.available = item["available"]

                    self.books.append(book)

        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []

    # ======================================================
    # SAVE STUDENTS
    # ======================================================

    def save_students(self):

        data = []

        for student in self.students:
            data.append(student.to_dict())

        with open(STUDENT_FILE, "w") as file:
            json.dump(data, file, indent=4)

    # ======================================================
    # LOAD STUDENTS
    # ======================================================

    def load_students(self):

        try:

            with open(STUDENT_FILE, "r") as file:

                data = json.load(file)

                self.students = []

                for item in data:

                    student = Student(
                        item["student_id"],
                        item["name"],
                        item["phone"]
                    )

                    student.borrowed_books = item["borrowed_books"]

                    self.students.append(student)

        except (FileNotFoundError, json.JSONDecodeError):
            self.students = []