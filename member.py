class Member():

    # Attribute to get unique id for each book
    _id_counter = 0

    def __init__(self, first_name, last_name, id_member=None, borrowed_books=None):
        
        # Load last id_counter used
        if id_member is not None and id_member > Member._id_counter:
            Member._id_counter = id_member

        # Creates new ID if not given any
        Member._id_counter = Member._id_counter + 1 if id_member == None else Member._id_counter
        self.id = Member._id_counter + 1 if id_member == None else id_member
        
        self.first_name = first_name
        self.last_name = last_name

        # Load borrowed_books
        self.borrowed_books = [] if borrowed_books == None else borrowed_books
    
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name

    def get_id(self):
        return self.id
    
    def get_borrowed_books(self):
        return self.borrowed_books
    
    def add_borrowed_book(self, book):
        self.borrowed_books.append(book)
    
    def return_borrowed_book(self, book):
        self.borrowed_books.remove(book)
    
    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'borrowed_books': self.borrowed_books
        }