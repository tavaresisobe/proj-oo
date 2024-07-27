from typing import List
from user import User
from models.book import Book

class BookAvailabilityNotifier:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, user: User):
        if user not in self.subscribers:
            self.subscribers.append(user)

    def unsubscribe(self, user: User):
        if user in self.subscribers:
            self.subscribers.remove(user)

    def notify(self, message: str):
        self.subscribers: list[User]
        for user in self.subscribers:
            user.notify(message)

    def notify_new_book(self, book: Book):
        message = f"Novo livro adicionado: {book.title} por {book.author}"
        self.notify(message)

    def notify_book_status_change(self, book: Book, status: str):
        message = f"O status do livro {book.title} foi alterado para: {status}"
        self.notify(message)
