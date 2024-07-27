from user_repo import UserRepo
from user import User
from models.user_type import UserType


def seed_users():
    user_repo = UserRepo()
    user_repo.add_user(User("123", "Student 1", UserType.STUDENT))
    user_repo.add_user(User("456", "Teacher 1", UserType.TEACHER))
    return user_repo.users


def seed_users():
    user_repo = UserRepo()
    user_repo.add_user(User("123", "Student 1", UserType.STUDENT))
    user_repo.add_user(User("456", "Teacher 1", UserType.TEACHER))
    return user_repo.users

