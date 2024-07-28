from models.book import Book
import logging

LOGGER = logging.getLogger('sLogger')

class Loan:
    def __init__(self, start: str, end: str, book: Book, user):
        self.start = start
        self.end = end
        self.book = book
        self.user = user
        self.active = True

    def make_loan(self, user, book: Book):
        LOGGER.info(f"Processing rental for {user.name} for book {book.title}")
        loan_return = user.add_rented_book(user=user, book=book)
        if loan_return:
            print(f"Book {book.title} rented successfully by {user.name}.")
        else:
            print(f"Failed to rent book '{book.title}' for {user.name}.")

        return loan_return

    def reversal_loan(self, user, book: Book):
        LOGGER.info(f"Processing reversal rental for {user.name} for book {book.title}")
        loan_return = user.remove_rented_book(user=user, book=book)
        if loan_return:
            LOGGER.info(f"Reversal rental for book {book.title} by {user.name} successful")
        else:
            LOGGER.info(f"Failed to reverse rental for book {book.title} by {user.name}")

        return loan_return
