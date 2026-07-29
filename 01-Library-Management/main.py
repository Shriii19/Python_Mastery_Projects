from library import Library
from book import Book
from student import Student


library = Library()


def get_int_input(prompt: str):
    value = input(prompt).strip()

    try:
        return int(value)
    except ValueError:
        print("Please enter a valid number.")
        return None


while True:

    print("\n" + "=" * 40)
    print("📚 LIBRARY MANAGEMENT SYSTEM")
    print("=" * 40)

    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Register Student")
    print("6. View Students")
    print("0. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        book_id = get_int_input("Book ID: ")
        if book_id is None:
            continue

        title = input("Title: ")
        author = input("Author: ")
        category = input("Category: ")

        book = Book(book_id, title, author, category)

        library.add_book(book)

    elif choice == "2":

        library.view_books()

    elif choice == "3":

        keyword = input("Enter Book ID, Title, Author, or Category: ")
        library.search_books(keyword)

    elif choice == "4":

        book_id = get_int_input("Enter Book ID to delete: ")
        if book_id is None:
            continue

        library.delete_book(book_id)

    elif choice == "5":

        student_id = get_int_input("Student ID: ")
        if student_id is None:
            continue

        name = input("Student Name: ")
        phone = input("Phone Number: ")

        student = Student(student_id, name, phone)

        library.add_student(student)

    elif choice == "6":

        library.view_students()

    elif choice == "0":

        print("\nThank You 😊")
        break

    else:

        print("Invalid Choice!")