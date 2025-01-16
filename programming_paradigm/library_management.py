class Book:
    def __init__(self, title, author):
        """Initialize a Book with a title, an author, and an availability status."""
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        """Initialize a Library with an empty list of books."""
        self._books = []

    def add_book(self, book):
        """Add a new book to the library collection."""
        if isinstance(book, Book):
            self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by its title, marking it as unavailable."""
        for book in self._books:
            if book.title == title and book.is_available():
                if book.check_out():
                    print(f"Successfully checked out '{title}'.")
                    return
        print(f"Sorry, '{title}' is either not available or does not exist in the library.")

    def return_book(self, title):
        """Return a book by its title, marking it as available."""
        for book in self._books:
            if book.title == title and not book.is_available():
                if book.return_book():
                    print(f"Successfully returned '{title}'.")
                    return
        print(f"Sorry, '{title}' is either not checked out or does not exist in the library.")

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")
