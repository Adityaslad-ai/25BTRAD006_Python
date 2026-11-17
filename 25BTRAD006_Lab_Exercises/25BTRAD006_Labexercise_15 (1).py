
# Library Management System

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Issued"
        print(self.title, "-", self.author, "-", status)


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                book.display()

    def issue_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.available:
                    book.available = False
                    print("Book issued successfully.")
                else:
                    print("Book is already issued.")
                return
        print("Book not found.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.available:
                    book.available = True
                    print("Book returned successfully.")
                else:
                    print("Book was not issued.")
                return
        print("Book not found.")


library = Library()

library.add_book(Book("Python Basics", "John"))
library.add_book(Book("Java Programming", "James"))

while True:
    print("\n1. Display Books")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.display_books()
    elif choice == "2":
        title = input("Enter book title: ")
        library.issue_book(title)
    elif choice == "3":
        title = input("Enter book title: ")
        library.return_book(title)
    elif choice == "4":
        print("Exiting library system.")
        break
    else:
        print("Invalid choice.")
