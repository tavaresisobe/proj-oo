import unittest
from library_facade import LibraryFacade
from models.user_type import UserType
from user import User
from user_repo import UserRepo
from user_seed import seed_users


def run_app():
    library_facade = LibraryFacade()
    seed_books(library_facade)
    users = seed_users()

    while True:
        action = input("Enter action (rent, return, list, quit): ")
        if action == "rent":
            ra = input("Enter RA: ")
            book_id = int(input("Enter book ID: "))
            library_facade.rent_book(ra, book_id)
        elif action == "return":
            ra = input("Enter RA: ")
            book_id = int(input("Enter book ID: "))
            library_facade.return_rent_book(ra, book_id)
        elif action == "list":
            library_facade.list_books()
        elif action == "quit":
            break


def seed_books(library_facade: LibraryFacade):
    library_facade.add_book(1, "Book 1", "Author 1", "Fiction")
    library_facade.add_book(2, "Book 2", "Author 2", "Non-Fiction")


class TestLibraryFacade(unittest.TestCase):
    def setUp(self):
        self.library_facade = LibraryFacade()
        self.library_facade.add_book(1, "Test Book", "Test Author", "Fiction")

    def test_rent_book(self):
        user = User("123", "Test User", UserType.STUDENT)
        self.library_facade.rent_book("123", "Test User", UserType.STUDENT, 1)
        self.assertTrue(user.already_rented_book(self.library_facade.search_book(1)))

    def test_return_book(self):
        user = User("123", "Test User", UserType.STUDENT)
        self.library_facade.rent_book("123", "Test User", UserType.STUDENT, 1)
        self.library_facade.return_rent_book("123", "Test User", UserType.STUDENT, 1)
        self.assertFalse(user.already_rented_book(self.library_facade.search_book(1)))


if __name__ == "__main__":
    unittest.main()
    run_app()

