class Book:
    def __init__(self, id: int, title: str, author: str, category: str):
        self.id = id
        self.title = title
        self.author = author
        self.category = category
        self.is_available = True
