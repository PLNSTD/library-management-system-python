import utilities, json
from book import Book
from member import Member

class Library():

    def __init__(self, book_json_file='books.json', members_json_file='members.json'):
        self.book_json_file = book_json_file
        self.members_json_file = members_json_file
        self.book_catalog = self.load_books()
        self.members = self.load_members()
    
    def load_books(self):
        try:
            with open(self.book_json_file, 'r') as file:
                data = json.load(file)
                books = [Book(title=book['title'], author=book['author'], id_book=book['id'], available=book['available'], borrower=book['borrower']) for book in data]
                return books
        except (FileNotFoundError):
            return []
    
    def save_books_to_json(self):
        # Convert all Book instances to dictionaries and save
        books_data = [book.to_dict() for book in self.book_catalog]

        with open(self.book_json_file, 'w') as file:
            json.dump(books_data, file, indent=4)

    def load_members(self):
        try:
            with open(self.members_json_file, 'r') as file:
                data = json.load(file)
                members = [Member(first_name=member['first_name'], last_name=member['last_name'], id_member=member['id'], borrowed_books=member['borrowed_books']) for member in data]
                return members
        except (FileNotFoundError):
            return []

    def save_members_to_json(self):
        # Convert all Member instances to dictionaries and save
        members_data = [member.to_dict() for member in self.members]

        with open(self.members_json_file, 'w') as file:
            json.dump(members_data, file, indent=4)

    def add_book(self):
        print('----- NEW BOOK -----')
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
                print('Book ID not in catalog!')

    def get_book_by_id(self, id):
        book = [book for book in self.book_catalog if book.get_id() == id]
        return book[0] if len(book) != 0 else None

    def get_member_by_id(self, id):
        member = [member for member in self.members if member.get_id() == id]
        return member[0] if len(member) != 0 else None
    
    def display_book(self, book):
        print(f'BookID: {book.get_id()}')
        print(f'\tTitle: {book.get_title()}')
        print(f'\tAuthor: {book.get_author()}')
        if book.get_borrower() is not None:
            print(f'\tBorrowed by: {book.get_borrower()}')

    def display_catalog(self):
        print('----- BOOKS IN THE LIBRARY -----')
        for book in self.book_catalog:
            self.display_book(book)
    
    def display_member(self, member):
        print(f'MemberID: {member.get_id()}')
        print(f'\tFirst Name: {member.get_first_name()}')
        print(f'\tLast Name: {member.get_last_name()}')
        borrowed_books = member.get_borrowed_books()
        print(f'\tTotal Borrowed books: {len(borrowed_books)}')
        if len(borrowed_books) > 0:
            for book in borrowed_books:
                self.display_book(book)

    def display_member_list(self):
        for member in self.members:
            self.display_member(member)
    
    def get_members(self):
        return self.members

    def add_member(self):
        print('----- NEW MEMBER -----')
        member_first_name = utilities.get_non_empty_input('First Name: ')
        member_last_name = utilities.get_non_empty_input('Last Name: ')

        # Generate New member and save to JSON file
        new_member = Member(member_first_name, member_last_name)
        self.members.append(new_member)
        self.save_members_to_json()
    
    def remove_member(self):
        # self.book_catalog.remove(book)
        print('(For more informations display members)')
        print('\t0 - Go back')
        member_id = None
        while True:
            member_id = utilities.get_user_input_choice('\n\tInsert ID of the member to remove: ')
            if member_id == -1:
                print('Please insert a valid input.')
                continue
            if member_id == 0:
                return
            member_to_remove = self.get_member_by_id(member_id)
            if member_to_remove != None:
                try:
                    print('Removing...\n')
                    self.display_member(member_to_remove)
                    self.members.remove(member_to_remove)
                    self.save_members_to_json()
                    print('\nMember REMOVED')
                except:
                    print('Could not remove the member..')
                break
            else:
                print('Member ID not present!')
    