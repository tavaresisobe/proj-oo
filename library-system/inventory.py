from models.book import Book

class Inventory:
    def __init__(self):
        self.books = [] # representa uma 'abstracao' de operacoes no banco de dados

    def add_book(self, book: Book) -> Book:
        self.books.append(book)
        return self.books[0]

    def remove_book(self, inventary: list[Book], id: int) -> list[Book]:
        self.books = inventary

        if id in [book.id for book in self.books]:
            self.books = [book for book in self.books if book.id != id]
        return self.books

    def get_books(self, inventary: list[Book]) -> list[Book]:
        self.books = inventary

        return self.books

    def get_book_by_id(self, inventary: list[Book], id: int) -> Book:
        self.books = inventary

        for book in self.books:
            if book.id == id:
                return book
        return None

    def check_available(self, inventary: list[Book], id: int) -> bool:
        self.books = inventary

        for book in self.books:
            if book.id == id:
                return book.is_available
        raise Exception

    def update_availability(self, inventary: list[Book], id: int, available: bool) -> list[Book]:
        self.books = inventary

        for book in self.books:
            if book.id == id:
                book.is_available = available
                return self.books
        raise Exception
