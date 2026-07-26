"""
Book Class

This file contains the Book class.
It represents a single book in the library.
"""


class Book:
    """
    Represents a single book.
    """

    def __init__(self, book_id: int, title: str, author: str, category: str):
        """
        Constructor

        Args:
            book_id : Unique ID of the book
            title : Name of the book
            author : Author name
            category : Book category
        """

        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.available = True

    def display_book(self):
        """
        Display complete book details.
        """

        print("-" * 35)
        print(f"Book ID   : {self.book_id}")
        print(f"Title     : {self.title}")
        print(f"Author    : {self.author}")
        print(f"Category  : {self.category}")
        print(f"Available : {self.available}")
        print("-" * 35)