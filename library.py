import utilities, json
from book import Book

class Library():

    def __init__(self, json_file='books.json'):
        self.json_file = json_file
        self.book_catalog = self.load_books()
        self.members = []
    
    def load_books(self):
        try:
            with open(self.json_file, 'r') as file:
                data = json.load(file)
                books = [Book(book['title'], book['author'], book['available']) for book in data]
                return books
        except (FileNotFoundError):
            return []
    
    def save_books_to_json(self):
        # Convert all Book instances to dictionaries and save
        books_data = [book.to_dict() for book in self.book_catalog]

        with open(self.json_file, 'w') as file:
            json.dump(books_data, file, indent=4)

    def add_book(self):
        book_title = utilities.get_non_empty_input('Book Title: ')
        book_author = utilities.get_non_empty_input('Author: ')

        # Generate New Book and save to JSON file
        new_book = Book(book_title, book_author)
        self.book_catalog.append(new_book)
        self.save_books_to_json()

    def remove_book(self, book):
        self.book_catalog.remove(book)

    def display_catalog(self):
        print('---- BOOKS IN THE LIBRARY ----')
        for book in self.book_catalog:
            print(f'BookID: {book.get_id()}')
            print(f'\tTitle: {book.get_title()}')
            print(f'\tAuthor: {book.get_author()}')
        
        input('\nPress a ENTER to continue...')
    
    def get_members(self):
        return self.members

    def add_member(self, member):
        self.members.append(member)
    