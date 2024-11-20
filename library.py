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

    def remove_book(self):
        # self.book_catalog.remove(book)
        print('(For more informations display book catalog)')
        print('\t0 - Go back')
        book_id = None
        while True:
            book_id = utilities.get_user_input_choice('\n\tInsert ID of the book to remove: ')
            if book_id == -1:
                print('Please insert a valid input.')
                continue
            if book_id == 0:
                return
            book_to_remove = self.get_book_by_id(book_id)
            if book_to_remove != None:
                try:
                    print('Removing...\n')
                    self.display_book(book_to_remove)
                    self.book_catalog.remove(book_to_remove)
                    self.save_books_to_json()
                    print('\nBook REMOVED')
                except:
                    print('Could not remove the book..')
                break
            else:
                print('Book not in catalog!')

    def get_book_by_id(self, id):
        book = [book for book in self.book_catalog if book.get_id() == id]
        return book[0] if len(book) != 0 else None

    def display_book(self, book):
        print(f'BookID: {book.get_id()}')
        print(f'\tTitle: {book.get_title()}')
        print(f'\tAuthor: {book.get_author()}')

    def display_catalog(self):
        print('----- BOOKS IN THE LIBRARY -----')
        for book in self.book_catalog:
            self.display_book(book)
        
        input('\nPress a ENTER to continue...')
    
    def get_members(self):
        return self.members

    def add_member(self, member):
        self.members.append(member)
    