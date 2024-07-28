from test.fixtures.facade import (
    BOOK, 
    BOOK_DATA,
    USER_DATA
)
from unittest import IsolatedAsyncioTestCase
from facade.library_facade import LibraryFacade
from src.user import User

#execute com: pytest --log-cli-level=DEBUG test/test_library_facade.py -vv
#para visualizar o log das operações

def any_function(*args, **kwargs):
    pass

class LibraryFacadeTest(IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.sut = LibraryFacade()
        self.users = []
    
    def set_up_books(self) -> None:
        for book_id, book in BOOK_DATA.items():
            self.sut.register_book(
                book_id=book["id"],
                title=book["title"],
                author=book["author"],
                category=book["category"]
            )
    
    def set_up_users(self) -> None:
        for user_id, user_data in USER_DATA.items():
            user = User(ra=user_data["ra"], name=user_data["name"], user_type=user_data["user_type"])
            self.users.append(user)
        self.sut.users = self.users

    async def test_to_register_books(self):
        self.set_up_books()
        #self.sut.register_book(book_id=1, title=BOOK.get("title"), author=BOOK.get("author"), category=BOOK.get("category"))

        assert self.sut.inventory[0].id == 1
        assert self.sut.inventory[0].author == BOOK.get("author")
    
    async def test_to_remove_books(self):
        self.sut.register_book(book_id=1, title=BOOK.get("title"), author=BOOK.get("author"), category=BOOK.get("category"))
        self.sut.delete_book(book_id=1)

        assert len(self.sut.inventory) == 0
    
    async def test_to_listing_all_books(self):
        self.set_up_books()
        self.sut.search_for_all_books()
    
    async def test_to_search_book(self):
        self.set_up_books()
        self.sut.search_book(book_id=1)

    async def test_to_check_avaibility(self):
        self.set_up_books()
        self.sut.check_availability(book_id=2)

    async def test_to_serach_book_by_category(self):
        self.sut.register_book(book_id=1, title=BOOK.get("title"), author=BOOK.get("author"), category=BOOK.get("category"))
        self.sut.search_books_by_category(category_name="Ficção")

    async def test_to_rent_book(self):
        self.set_up_books()
        self.set_up_users()
        self.sut.rent_book(ra="158552", book_id=1)
    
    async def test_to_return_loan_book(self):
        self.set_up_books()
        self.set_up_users()

        self.sut.rent_book(ra="158552", book_id=1)
        self.sut.rent_book(ra="129121", book_id=3)
        self.sut.rent_book(ra="158552", book_id=2)
        self.sut.rent_book(ra="158552", book_id=4)

        self.sut.return_rent_book(ra="158552", book_id=1) #devolvendo o livro com id 1

        self.sut.rent_book(ra="129121", book_id=1) #alugando o livro com o id 1, novamente
