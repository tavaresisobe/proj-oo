from models.book import Book
from inventory import Inventory
from user import User
from loan import Loan
from datetime import datetime, timedelta
import logging
from typing import Tuple

LOGGER = logging.getLogger('sLogger')

class LibraryUserMediator:
    def __init__(self):
        self.inventory = Inventory(self)

    def process_to_rental_book(self, users_list: list[User], actual_inventary: list [Book],
                                rent: list[Loan], ra: str, book_id: int) -> None:

        user, user_index = self.__get_user_data(users_list=users_list, ra=ra)
        user: User

        try:
            if self.inventory.check_available(inventary=actual_inventary, id=book_id):
                book = self.inventory.get_book_by_id(inventary=actual_inventary, id=book_id)
                if user.can_rent_more_books(user=user):
                    new_loan = Loan(start=datetime.now(), end=datetime.now()+timedelta(days=10),
                                    user=user, book=book)
                    user = new_loan.make_loan(user, book)
                    actual_inventary = self.inventory.update_availability(inventary=actual_inventary, 
                                                       id=book_id, available=False)
                    users_list [user_index] = user
                    return actual_inventary, users_list, rent.append(new_loan)
                else:
                    LOGGER.info(f"{user.name} has reached the limit of rented books for
                          {user.user_type.name.lower()}")
            else:
                LOGGER.info(f"The book with ID {book_id} is not available for rent")
        except Exception as error:
            LOGGER.critical(f"An error occurred when renting the book with id {book_id} for ra {ra} - {error}")

    def process_to_return_book(self, users_list: list[User], actual_inventary: list [Book],
                                rent: list[Loan], ra: str, book_id: int) -> None:

        user, user_index = self.__get_user_data(users_list=users_list, ra=ra)
        user: User

        try:
            book = self.inventory.get_book_by_id(inventary=actual_inventary, id=book_id)
            if user.already_rented_book(user=user, book=book):
                loan, loan_index = Loan().search_for_loan(rent, book)
                user = loan.reversal_loan(user, book)
                actual_inventary = self.inventory.update_availability(inventary=actual_inventary, 
                                                       id=book_id, available=True)
                users_list [user_index] = user
                rent[loan_index].active = False
                return actual_inventary, users_list, rent
            else:
                LOGGER.info(f"{user.name} did not rent the book with ID {book_id}")
        except Exception as error:
            LOGGER.critical(f"An error occurred while returning the book with id {book_id} to ra {ra} - {error}")

    def __get_user_data(users_list: list[User], ra: str)-> Tuple[User, int]:
        try:
            LOGGER.info(f"Getting user with ra {ra}")
            return User().get_user_by_ra(users_data=users_list, ra=ra)
        except Exception as error:
            LOGGER.critical (f"User with ra {ra} not registered - {error}")
