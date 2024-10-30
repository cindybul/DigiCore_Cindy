from colorama import Fore, init
import re

init(autoreset=True)

def get_valid_credentials():
    while True:
        # Get and validate username
        username = input('Input username: ').strip()
        if not (3 <= len(username) <= 20) or not re.match(r'^[a-zA-Z0-9_]+$', username) or username.startswith('_') or username.endswith('_'):
            print(Fore.RED + "Invalid username. It must be 3-20 characters, contain only letters, numbers, or underscores, and cannot start or end with an underscore.")
            continue  # Prompt again if invalid
        
        # Get and validate password
        password = input('Input password: ').strip()
        if len(password) < 8 or not re.match(r'^[a-zA-Z0-9_!@#$%^&*()]+$', password):
            print(Fore.RED + "Invalid password. It must be at least 8 characters long and can include symbols.")
            continue  # Prompt again if invalid

        # Return both if valid
        return username, password