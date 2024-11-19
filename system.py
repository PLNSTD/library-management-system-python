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
        print('\t3 - Borrow a Book')
        print('\t4 - Return a Book')
        print('\t5 - Display Book Catalog')
        print('\t6 - Display Library Members')
        print('\t0 - Exit System')

        # Get User Input
        user_input = utilities.get_user_input_choice()

        if user_input == 1:
            # Clear Terminal
            utilities.prompt_clear()

            # Use the my_lib class to Generate a new book
            my_lib.add_book()

            # Wait to get to main menu
            utilities.wait()
        elif user_input == 5:
            # Clear Terminal
            utilities.prompt_clear()

            # Use the my_lib class to Generate a new book
            my_lib.display_catalog()

            # Wait to get to main menu
            utilities.wait()
        elif user_input == 0: # EXIT SYSTEM
            utilities.prompt_clear()
            break
        
main()