from models.user_type import UserType
from models.book import Book
from user import User

LOAN_STUDENT = 3
LOAN_TEACHER = 10
LOAN_WORKER = 10

class User:
    def __init__(self, ra: str, name: str, user_type: UserType):
        self.ra = ra
        self.name = name
        self.user_type = user_type
        self.rented_books = [] #lista de livros emprestados (guarda objetos do tipo Book)

    def can_rent_more_books(self, user: User) -> bool:
        if user.user_type == UserType.STUDENT:
            return len(self.rented_books) < LOAN_STUDENT
        elif self.user_type == UserType.TEACHER:
            return len(self.rented_books) < LOAN_TEACHER
        elif self.user_type == UserType.HARDWORKER:
            return len (self.rented_books) < LOAN_WORKER

    def already_rented_book(self, user: User, book: Book) -> bool:
        return book in user.rented_books

    def add_rented_book(self, user: User, book: Book) -> User:
        try:
            user.rented_books.append(book)
        except:
            return None
        return user

    def remove_rented_book(self, user: User, book: Book) -> User:
        try:
            user.rented_books.remove(book)
        except:
            return None
        return user
    
    def get_user_by_ra(self, users_data: list[User], ra: str):
        for index, user in enumerate(users_data):
            if user.ra == ra:
                return user, index
        raise Exception(f"User with RA {ra} not found")

    def notify(self, message: str):
        print(f"Notificação para {self.name}: {message}")

