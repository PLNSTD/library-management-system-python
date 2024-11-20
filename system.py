import utilities
from library import Library

def main():
    my_lib = Library()
    while True:
        # Clear Terminal
        utilities.prompt_clear()

        # User Options
        print('Nebula Academy Library')
        print('\t1 - Add a Book')
        print('\t2 - Remove a Book')
        print('\t3 - Add a Member')
        print('\t4 - Remove a Member')
        print('\t5 - Borrow a Book')
        print('\t6 - Return a Book')
        print('\t7 - Display Book Catalog')
        print('\t8 - Display Library Members')
        print('\t0 - Exit System')

        # Get User Input
        user_input = utilities.get_user_input_choice('\n\tYour choice: ')
        
        # Clear Terminal
        utilities.prompt_clear()

        if user_input == 1: # Add a book
            # Use the library class to generate a new book
            my_lib.add_book()
        elif user_input == 2: # Remove a book
            # Use the library class to remove existing book
            my_lib.remove_book()
        elif user_input == 3: # TODO: Add a member
            # Use the library class to add a new member
            my_lib.add_member()
        elif user_input == 4: # TODO: Remove a member
            pass
        elif user_input == 5: # TODO: Borrow a book
            pass
        elif user_input == 6: # TODO: Return a book
            pass
        elif user_input == 7: # Display books
            # Use the library class to display books
            my_lib.display_catalog()
        elif user_input == 8: # TODO: Display members
            my_lib.display_member_list()
        elif user_input == 0: # EXIT SYSTEM
            break

        # Wait to get to main menu
        utilities.wait()
        
main()