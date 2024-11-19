class Member():
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.id_member = None
        self.borrowed_books = []
    
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def get_borrowed_books(self):
        return self.borrowed_books
    
    def add_borrowed_book(self, book):
        self.borrowed_books.append(book)
    
    def return_borrowed_book(self, book):
        self.borrowed_books.remove(book)