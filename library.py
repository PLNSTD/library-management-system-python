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
        print('(For more informations display book catalog)')
        print('\t0 - Go back')
        book_id = None

        # Get book choice
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
            print(f'\tBorrower ID: {book.get_borrower()}')

    def display_catalog(self):
        print('----- BOOKS IN THE LIBRARY -----')
        print(f'Total books: {len(self.book_catalog)}')
        for book in self.book_catalog:
            self.display_book(book)
    
    def display_member(self, member, show_books=True):
        print(f'MemberID: {member.get_id()}')
        print(f'\tFirst Name: {member.get_first_name()}')
        print(f'\tLast Name: {member.get_last_name()}')
        borrowed_books = member.get_borrowed_books()
        print(f'\tTotal Borrowed books: {len(borrowed_books)}')
        if len(borrowed_books) > 0 and show_books:
            for book_id in borrowed_books:
                self.display_book(self.get_book_by_id(book_id))

    def display_member_list(self):
        print('----- MEMBERS OF THE LIBRARY -----')
        print(f'Total members: {len(self.members)}')
        for member in self.members:
            self.display_member(member, show_books=False)
    
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
    
    def borrow_book(self):
        book_to_borrow = None
        borrower = None

        print('----- BORROWING MENU -----')
        print('\t0 - Go back')

        # Get Info book and availability
        while True: # Check input and get book (if exists)
            book_id = utilities.get_user_input_choice('\nInsert Book ID: ')
            
            if book_id == -1:
                print('Please insert a valid input.')
                continue

            if book_id == 0:
                return
            
            book_to_borrow = self.get_book_by_id(book_id)
            
            if book_to_borrow == None:
                print('\n\tBook not in catalog!')
                continue

            if not book_to_borrow.is_available():
                print('\n\tBook unavailable at the moment.. already borrowed')
                continue
            break

        self.display_book(book_to_borrow)

        while True: # Check input and get member (if exists)
            member_id = utilities.get_user_input_choice('\nInsert Member ID: ')

            if member_id == -1:
                print('Please insert a valid input.')
                continue

            if member_id == 0:
                return
            
            borrower = self.get_member_by_id(member_id)

            if borrower == None:
                print('\n\tMember ID not in the system')
                continue
            break

        # Update book got borrowed
        book_to_borrow.set_availability(False)
        book_to_borrow.set_borrower(borrower.get_id())

        # Update member borrowed books
        borrower.add_borrowed_book(book_to_borrow.get_id())
        # utilities.wait(1,press_key=False) # Wait time to update lists

        self.save_books_to_json()
        self.save_members_to_json()

        self.display_member(borrower, show_books=False)

    def return_book(self):
        book_to_return = None
        borrower = None

        print('----- BORROWING MENU-----')
        print('\t0 - Go back')

        while True: # Check input and get member (if exists)
            member_id = utilities.get_user_input_choice('\nInsert Member ID: ')

            if member_id == -1:
                print('Please insert a valid input.')
                continue

            if member_id == 0:
                return
            
            borrower = self.get_member_by_id(member_id)

            if borrower == None:
                print('\n\tMember ID not in the system')
                continue

            if len(borrower.get_borrowed_books()) == 0:
                print('\n\tThis member has no book to return!')
                continue
            break

        self.display_member(borrower, show_books=False)

        # Get Info book and availability
        while True: # Check input and get book (if exists)
            book_id = utilities.get_user_input_choice('\nInsert Book ID: ')
            
            if book_id == -1:
                print('Please insert a valid input.')
                continue

            if book_id == 0:
                return
            
            book_to_return = self.get_book_by_id(book_id)
            
            if book_to_return == None:
                print('\n\tBook not in catalog!')
                continue

            if book_to_return.get_id() not in borrower.get_borrowed_books():
                print("\n\tThis book is not in the member's borrowed list!")
                continue
            break

        self.display_book(book_to_return)

        # Update book got borrowed
        book_to_return.set_availability(True)
        book_to_return.set_borrower(None)

        # Update member borrowed books
        borrower.return_borrowed_book(book_to_return.get_id())

        self.save_books_to_json()
        self.save_members_to_json()
