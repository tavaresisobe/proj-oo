from models.user_type import UserType
from models.book import Book

LOAN_STUDENT = 3
LOAN_TEACHER = 10
LOAN_WORKER = 10

class User:
    def __init__(self, ra: str, name: str, user_type: UserType):
        self.ra = ra
        self.name = name
        self.user_type = user_type
        self.rented_books = []  # lista de livros emprestados (guarda objetos do tipo Book)

    def can_rent_more_books(self, user) -> bool:
        if user.user_type == UserType.STUDENT:
            return len(user.rented_books) < LOAN_STUDENT
        elif user.user_type == UserType.TEACHER:
            return len(user.rented_books) < LOAN_TEACHER
        elif user.user_type == UserType.HARDWORKER:
            return len(user.rented_books) < LOAN_WORKER

    def already_rented_book(self, user, book: Book) -> bool:
        return book in user.rented_books

    def add_rented_book(self, user, book: Book):
        try:
            user.rented_books.append(book)
        except Exception:
            return None
        return self

    def remove_rented_book(self, user, book: Book):
        try:
            user.rented_books.remove(book)
        except Exception:
            return None
        return self

    def get_user_by_ra(self, users_data: list, ra: str):
        for index, user in enumerate(users_data):
            if user.ra == ra:
                return user, index
        raise Exception(f"User with RA {ra} not found")

    def notify(self, message: str):
        print(f"Notificação para {self.name}: {message}")
