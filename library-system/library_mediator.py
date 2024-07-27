from inventory import Inventory
from models.book import Book
import logging

LOGGER = logging.getLogger('sLogger')

class LibraryMediator:
    def __init__(self):
        self.inventory = Inventory()

    def insert_book(self, actual_inventory: list, book_id: int, title: str, author: str, category: str) -> Book:
        self.__id_aleady_exist(inventary=actual_inventory, id=book_id)
        try:
            LOGGER.info ("registering book")
            new_book = Book(id=book_id, title=title, author=author, category=category)
            return self.inventory.add_book(book=new_book)
        except Exception as error:
            LOGGER.critical(f"An error occurred when registering a new book with id: {book_id} - {error}")

    def get_book(self, actual_inventary: list, book_id: int) -> Book:
        try:
            LOGGER.info (f"geting book with id {book_id}")
            search_result = self.inventory.get_book_by_id(inventary=actual_inventary, id=book_id)
            return search_result
        except Exception as error:
            LOGGER.critical(f"the book with id {book_id} was not found - {error}")

    def get_books(self, actual_inventary: list) -> list[Book]:
        try:
            LOGGER.info(f"getting books")
            return self.inventory.get_books(inventary=actual_inventary)
        except Exception as error:
            LOGGER.critical(f"failure on getting books - {error}")

    def remove_book(self, actual_inventary: list, book_id: int) -> list[Book]:
        self.__id_exist(inventary=actual_inventary, id=book_id)
        try:
            LOGGER.info(f"removing book with id {book_id}")
            return self.inventory.remove_book(inventary=actual_inventary, id=book_id)
        except Exception as error:
            LOGGER.critical(f"failed to remove book with id {book_id} - {error}")
            raise error

    def check_available(self, actual_inventary: list, book_id: int) -> bool:
        self.__id_exist(inventary=actual_inventary, id=book_id)
        try:
            LOGGER.info(f"checking avaibility to book with id {book_id}")
            is_avaible = self.inventory.check_available(book_id)
            return is_avaible
        except Exception as error:
            LOGGER.critical(f"failed to check avaibility to id {book_id} - {error}")
            raise error
    
    def __id_exist(self, inventary: list, id: int)-> Book:
        LOGGER.info(f"checking existence of id {id}")
        try:
            id_exist = self.get_book(actual_inventary=inventary, book_id=id)
            if not id_exist:
                raise Exception
            return id_exist
        except Exception as error:
            LOGGER.critical(f"the id {id} does not exist - {error}")
            raise error

    def __id_aleady_exist(self, inventary: list, id: int)-> Book:
        LOGGER.info(f"checking the recurrence of id {id}")
        try:
            id_exist = self.get_book(actual_inventary=inventary, book_id=id)
            if id_exist:
                raise Exception
            return id_exist
        except Exception as error:
            LOGGER.critical (f"A book with the id {id} already exists")
            raise error
