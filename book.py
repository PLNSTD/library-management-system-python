class Book():

    # Attribute to get unique id for each book
    _id_counter = 0

    def __init__(self, title, author, id_book=None, available=True, borrower=None):

        # Load last id_counter used
        if id_book is not None and id_book > Book._id_counter:
            Book._id_counter = id_book

        # Creates new ID if not given any
        Book._id_counter = Book._id_counter + 1 if id_book == None else Book._id_counter
        self.id = Book._id_counter if id_book == None else id_book

        self.title = title
        self.author = author
        self.available = available # Set book availability
        self.borrower = borrower # ID of the member who borrowed (if book unavailable)
    
    def get_id(self):
        return self.id
    
    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
    def is_available(self):
        return self.status

    def set_availability(self, status):
        self.available = status
    
    def get_borrower(self):
        return self.borrower

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'available': self.available,
            'borrower': self.borrower
        }
