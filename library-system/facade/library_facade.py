import logging
from mediator.library_mediator import LibraryMediator
from mediator.library_user_mediator import LibraryUserMediator
from src.book_category import BookCategory
from src.book_notifier import BookAvailabilityNotifier
from external_user_adapter import ExternalUserAdapter
from external_catalog_adapter import ExternalCatalogAdapter
from src.user import User

LOGGER = logging.getLogger('sLogger')

class LibraryFacade:
    def __init__(self, external_catalog_adapter=None, external_user_adapter=None):
        self.library_mediator = LibraryMediator()
        self.user_library_mediator = LibraryUserMediator()
        self.root_category = BookCategory("Root")
        self.notifier = BookAvailabilityNotifier()
        self.inventory = [] #lista de livros (guarda objetos do tipo Book)
        self.users = [] #lista de usuarios (guarda objetos do tipo User)
        self.loan = [] #lista de alugueis (guarda objetos do tipo Loan)

        if external_catalog_adapter:
            self.integrate_external_books(external_catalog_adapter)
        if external_user_adapter:
            self.integrate_external_users(external_user_adapter)

    def integrate_external_books(self, external_catalog_adapter: ExternalCatalogAdapter) -> None:
        external_catalog_adapter.integrate_books(self.inventory)

    def integrate_external_users(self, external_user_adapter: ExternalUserAdapter) -> None:
        external_user_adapter.integrate_users(self.users)

    def register_book(self, book_id: int, title: str, author: str, category: str) -> None:
        book_model = self.library_mediator.insert_book(actual_inventory=self.inventory, 
                                                       book_id=book_id, title=title, 
                                                       author=author, category=category)
        self.inventory.append(book_model)
        LOGGER.info(f"Livro cadastrado com sucesso")

        category_node = self.root_category.find_category(category)
        if not category_node:
            category_node = BookCategory(category)
            self.root_category.add_subcategory(category_node)
            LOGGER.info(f"Categoria cadastrada com sucesso")

        category_node.add_book(book_model)

    def delete_book(self, book_id: int) -> None:
        book_model = self.library_mediator.remove_book(actual_inventary=self.inventory,
                                                       book_id=book_id)
        self.inventory = book_model

        LOGGER.info(f"Livro removido com sucesso")

    def search_for_all_books(self) -> None:
        search_return = self.library_mediator.get_books(actual_inventary=self.inventory)
        if search_return:
            formatted_books = "\n".join([f"ID: {book.id}, Título: {book.title}, Categoria: {book.category}" for book in search_return])
            LOGGER.debug(f"Livros cadastrados:\n{formatted_books}")
        else:
            LOGGER.debug("Nenhum livro encontrado.")

        LOGGER.info(f"Busca concluida com sucesso")

    def search_book(self, book_id) -> None:
        search_return = self.library_mediator.get_book(actual_inventary=self.inventory,
                                                       book_id=book_id)
        
        if search_return:
            book_info = (f"ID: {search_return.id}, "
                     f"Título: {search_return.title}, "
                     f"Autor: {search_return.author}, "
                     f"Disponibilidade: {'Disponível' if search_return.is_available else 'Indisponível'}, "
                     f"Categoria: {search_return.category}")
            LOGGER.debug(f"Livro com id correspondente: {book_info}")
        else:
            LOGGER.debug(f"Nenhum livro encontrado com o id: {book_id}")

        LOGGER.info(f"Busca concluida com sucesso")
    
    def search_books_by_category(self, category_name: str) -> None:
        category = self.root_category.find_category(category_name)
        if category:
            books = category.get_books()
            for book in books:
                LOGGER.debug(f"Livro: {book.title}, Autor: {book.author}, ID: {book.id}")
            LOGGER.info(f"Listagem de livros da categoria {category_name} concluída com sucesso")
        else:
            LOGGER.critical(f"Categoria {category_name} não encontrada")

    def check_availability(self, book_id: int) -> None:
        availability = self.library_mediator.check_available(actual_inventary=self.inventory,
                                                             book_id=book_id)
        if availability:
            LOGGER.debug(f"O livro com ID {book_id} está disponível")
        else:
            LOGGER.debug(f"O livro com ID {book_id} não está disponível")

        LOGGER.info(f"Verificacao concluida com sucesso")

    def rent_book(self, ra: str, book_id: int) -> None:
        self.inventory, self.users, self.loan = self.user_library_mediator.process_to_rental_book(users_list=self.users,
                                                          actual_inventary = self.inventory,
                                                          rent=self.loan, ra=ra,
                                                          book_id=book_id)
        
        LOGGER.info(f"Empréstimo do livro {book_id} realizado com sucesso para o ra {ra}")

    def return_rent_book(self, ra: str, book_id: int) -> None:
        self.inventory, self.users, self.loan = self.user_library_mediator.process_to_return_book(users_list=self.users,
                                                          actual_inventary = self.inventory,
                                                          rent=self.loan, ra=ra,
                                                          book_id=book_id)

        LOGGER.info(f"Devolução do livro {book_id} realizada com sucesso para o ra {ra}")

    def subscribe_user_to_notifications(self, user: User) -> None:
        self.notifier.subscribe(user)
        LOGGER.info(f"Usuário {user.name} inscrito para notificações")

    def unsubscribe_user_from_notifications(self, user: User) -> None:
        self.notifier.unsubscribe(user)
        LOGGER.info(f"Usuário {user.name} desinscrito das notificações")
