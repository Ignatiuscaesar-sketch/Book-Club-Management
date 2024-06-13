import hashlib
from models import session
from models.user import User

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate(username, password):
    user = session.query(User).filter_by(username=username).first()
    if user and user.password == hash_password(password):
        return user
    return None

def register_user(username, password):
    if session.query(User).filter_by(username=username).first():
        return 'Username already exists.'
    user = User(username=username, password=hash_password(password))
    session.add(user)
    session.commit()
    return 'User registered successfully!'

def login_user(username, password):
    user = authenticate(username, password)
    if user:
        return user, 'Login successful!'
    else:
        return None, 'Invalid username or password.'
