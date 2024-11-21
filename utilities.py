import os, time

def prompt_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait(sec=3, press_key=True):
    if press_key:
        input('\nPress a ENTER to continue...')
    counter = sec
    print(f'Please wait...')
    while counter > 0:
        print(f'\t\t{counter}')
        time.sleep(1)
        counter -= 1

def get_user_input_choice(prompt):
    user_input = input(prompt)

    try:
        user_input = int(user_input)
    except (ValueError, OverflowError):
        return -1

    return user_input

def get_non_empty_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("Please enter a valid input.")