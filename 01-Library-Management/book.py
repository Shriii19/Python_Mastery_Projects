class Book:

    def __init__(self, book_id, title, author, category):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.available = True

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "category": self.category,
            "available": self.available
        }

    @staticmethod
    def from_dict(data):
        book = Book(
            data["book_id"],
            data["title"],
            data["author"],
            data["category"]
        )
        book.available = data.get("available", True)
        return book

    def display(self):
        print("-" * 40)
        print(f"Book ID   : {self.book_id}")
        print(f"Title     : {self.title}")
        print(f"Author    : {self.author}")
        print(f"Category  : {self.category}")
        print(f"Available : {self.available}")

