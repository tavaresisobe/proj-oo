# external_user_adapter.py
import requests
import logging
from typing import List, Dict
from src.user import User, UserType

LOGGER = logging.getLogger('sLogger')

class ExternalUserAdapter:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def fetch_users(self) -> List[Dict]:
        try:
            response = requests.get(f"{self.base_url}/users")
            response.raise_for_status()
            users = response.json()
            return users
        except requests.RequestException as e:
            print(f"An error occurred while fetching users: {e}")
            return []

    def integrate_users(self, users: List[User]) -> None:
        users_data = self.fetch_users()
        for user_data in users_data:
            user = User(
                ra=user_data.get("ra"),
                name=user_data.get("name"),
                user_type=UserType[user_data.get("user_type").upper()]
            )
            users.append(user)

if __name__ == "__main__":
    from facade.library_facade import LibraryFacade

    external_user_adapter = ExternalUserAdapter(base_url="http://external-user.com/api")
    library_facade = LibraryFacade()
    library_facade.integrate_external_users(external_user_adapter)
    LOGGER.info("Users integrated successfully")
