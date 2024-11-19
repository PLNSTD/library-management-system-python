class Book():

    # Attribute to get unique id for each book
    _id_counter = 0

    def __init__(self, title, author) -> None:
        # Set unique ID for the instance
        Book._id_counter += 1 

        self.id = Book._id_counter
        self.title = title
        self.author = author
        self.available = True # Available to get borrowed
    
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
    