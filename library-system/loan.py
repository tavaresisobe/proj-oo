from models.book import Book
from user import User
from loan import Loan
import logging
from typing import Tuple

LOGGER = logging.getLogger('sLogger')

class Loan:
    def __init__(self, start: str, end: str, book: Book, user: User):
        self.start = start
        self.end = end
        self.book = book
        self.user = user
        self.active = True

    def make_loan(self, user: User, book: Book) -> User:
        LOGGER.info(f"Processing rental for {user.name} for book {book.title}")
        loan_return = self.user.add_rented_book(user=user, book=book)
        if loan_return:
            print(f"Book {book.title} rented successfully by {user.name}.")
        else:
            print(f"Failed to rent book '{book.title}' for {user.name}.")

        return loan_return

    def reversal_loan(self, user: User, book: Book) -> User:
        LOGGER.info(f"Processing reversal rental for {user.name} for book {book.title}")
        loan_return = self.user.remove_rented_book(user=user, book=book)
        if loan_return:
            LOGGER.info(f"Reversal rental for book {book.title} by {user.name} successful")
        else:
            LOGGER.info(f"Failed to reverse rental for book {book.title} by {user.name}")

        return loan_return
    
    def search_for_loan(self, loan_data: list[Loan], book: Book) -> Tuple[Loan, int]:
        for index, loan in enumerate(loan_data):
            if loan.book == book:
                return loan, index
