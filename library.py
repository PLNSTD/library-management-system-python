import utilities
from book import Book

class Library():

    def __init__(self) -> None:
        self.book_catalog = []
        self.members = []
    
    def add_book(self):
        book_title = ''

        while True:
            user_input = input('Book Title: ')
            if len(user_input) > 0:
                book_title = user_input
                break
            print("Please enter a valid book title.")  # Inform user if input is empty
        
        # Clear Terminal
        utilities.prompt_clear()

        book_author = ''
        while True:
            user_input = input('Author: ')
            if len(user_input) > 0:
                book_author = user_input
                break
            print("Please enter a valid author.")  # Inform user if input is empty

        # Generate New Book
        new_book = Book(book_title, book_author)

        self.book_catalog.append(new_book)

    def remove_book(self, book):
        self.book_catalog.remove(book)

    def display_catalog(self):
        print('---- BOOKS IN THE LIBRARY ----')
        for book in self.book_catalog:
            print(f'\tTitle: {book.get_title()}')
            print(f'\tAuthor: {book.get_author()}')
    
    def get_members(self):
        return self.members

    def add_member(self, member):
        self.members.append(member)