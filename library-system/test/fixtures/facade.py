from models.user_type import UserType

IS_AVAIBLE_TRUE = True
CATEGORY = "Ficção"

AUTHOR = "Joanne Rowling"
TITLE = "Harry Potter"

AUTHOR_2 = "The Hobbit"
TITLE_2 = "J.R.R. Tolkien"

AUTHOR_3 = "George Orwell"
TITLE_3 = "1984"

AUTHOR_4 = "Aldous Huxley"
TITLE_4 = "Brave New World"

BOOK = {
    "id": 1,
    "title": TITLE,
    "author": AUTHOR,
    "category": CATEGORY,
    "is_avaible": IS_AVAIBLE_TRUE
}

BOOK_2 = {
    "id": 2,
    "title": TITLE_2,
    "author": AUTHOR_2,
    "category": CATEGORY,
    "is_avaible": IS_AVAIBLE_TRUE
}

BOOK_3 = {
    "id": 3,
    "title": TITLE_3,
    "author": AUTHOR_3,
    "category": CATEGORY,
    "is_avaible": IS_AVAIBLE_TRUE
}

BOOK_4 = {
    "id": 4,
    "title": TITLE_4,
    "author": AUTHOR_4,
    "category": CATEGORY,
    "is_avaible": IS_AVAIBLE_TRUE
}

BOOK_DATA = {
    "1": BOOK,
    "2": BOOK_2,
    "3": BOOK_3,
    "4": BOOK_4
}

USERTYPE_STUDENT =  UserType.STUDENT
USERTYPE_TEACHER = UserType.TEACHER
USERTYPE_WORKER = UserType.HARDWORKER

NAME = "Cristiano Ronaldo"
RA = "158552"

NAME_2 = "Neymar Junior"
RA_2 = "152898"

NAME_3 = "Cassio Ramos"
RA_3 = "149828"

NAME_4 = "Ramon Diaz"
RA_4 = "132923"

NAME_5 = "José Mourinho"
RA_5 = "129121"

USER = {
    "ra": RA,
    "name": NAME,
    "user_type": USERTYPE_WORKER
}

USER_2 = {
    "ra": RA_2,
    "name": NAME_2,
    "user_type": USERTYPE_STUDENT
}

USER_3 = {
    "ra": RA_3,
    "name": NAME_3,
    "user_type": USERTYPE_STUDENT
}

USER_4 = {
    "ra": RA_4,
    "name": NAME_4,
    "user_type": USERTYPE_TEACHER
}

USER_5 = {
    "ra": RA_5,
    "name": NAME_5,
    "user_type": USERTYPE_TEACHER
}

USER_DATA = {
    "1": USER,
    "2": USER_2,
    "3": USER_3,
    "4": USER_4,
    "5": USER_5
}
