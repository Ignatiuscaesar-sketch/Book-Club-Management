import os

AUTH_FILE = 'current_user.txt'

def save_current_user(username):
    with open(AUTH_FILE, 'w') as f:
        f.write(username)

def get_current_user():
    if os.path.exists(AUTH_FILE):
        with open(AUTH_FILE, 'r') as f:
            return f.read().strip()
    return None

def clear_current_user():
    if os.path.exists(AUTH_FILE):
        os.remove(AUTH_FILE)
