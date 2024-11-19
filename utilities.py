import os, time

def prompt_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait():
    time.sleep(3)

def get_user_input_choice():
    user_input = input('\nYour choice: ')

    try:
        user_input = int(user_input)
    except (ValueError, OverflowError):
        return -1

    return user_input
