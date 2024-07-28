# external_catalog_adapter.py
import requests
import logging
from typing import List, Dict
from models.book import Book

LOGGER = logging.getLogger('sLogger')

class ExternalCatalogAdapter:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def fetch_books(self) -> List[Dict]:
        """
        Fetch books from the external catalog system.
        """
        try:
            response = requests.get(f"{self.base_url}/books")
            response.raise_for_status()
            books = response.json()
            return books
        except requests.RequestException as e:
            print(f"An error occurred while fetching books: {e}")
            return []

    def integrate_books(self, inventory: List[Book]) -> None:
        """
        Integrate books from the external system into the library system.
        """
        books_data = self.fetch_books()
        for book_data in books_data:
            book = Book(
                id=book_data.get("id"),
                title=book_data.get("title"),
                author=book_data.get("author"),
                available=book_data.get("available"),
                category=book_data.get("category")
            )
            inventory.append(book)

if __name__ == "__main__":
    from facade.library_facade import LibraryFacade

    external_catalog_adapter = ExternalCatalogAdapter(base_url="http://external-catalog.com/api")
    library_facade = LibraryFacade()
    library_facade.integrate_external_books(external_catalog_adapter)
    LOGGER.info("Books integrated successfully")