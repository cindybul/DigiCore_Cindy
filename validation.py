#colourful output
from colorama import Fore, Style, init
init(autoreset=True)

# This module allows you to use patterns to search, match, and manipulate strings based on complex criteria
import re


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

        # Get and validate URL
        url = input('Input URL/Resources: ').strip()
        if not (3 <= len(url) <= 20) or not re.match(r'^[a-zA-Z0-9_]+$', url) or url.startswith('_') or url.endswith('_'):
            print(Fore.RED + "Invalid URL It must be 3-20 characters, contain only letters, numbers, or underscores, and cannot start or end with an underscore.")
            continue

        # Return both if valid
        return username, password, url