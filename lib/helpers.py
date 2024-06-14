import os

def save_current_user(username):
    with open('current_user.txt', 'w') as file:
        file.write(username)

def get_current_user():
    if os.path.exists('current_user.txt'):
        with open('current_user.txt', 'r') as file:
            return file.read().strip()
    return None

def clear_current_user():
    if os.path.exists('current_user.txt'):
        os.remove('current_user.txt')
