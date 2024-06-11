import click
from lib.models import session
from lib.models.user import User
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate(username, password):
    user = session.query(User).filter_by(username=username).first()
    if user and user.password == hash_password(password):
        return user
    return None

@click.command()
@click.option('--username', prompt=True)
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True)
def register(username, password):
    if session.query(User).filter_by(username=username).first():
        click.echo('Username already exists.')
        return
    user = User(username=username, password=hash_password(password))
    session.add(user)
    session.commit()
    click.echo('User registered successfully!')

@click.command()
@click.option('--username', prompt=True)
@click.option('--password', prompt=True, hide_input=True)
def login(username, password):
    user = authenticate(username, password)
    if user:
        click.echo('Login successful!')
        return user
    else:
        click.echo('Invalid username or password.')
        return None
