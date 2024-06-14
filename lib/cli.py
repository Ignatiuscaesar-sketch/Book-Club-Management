import sys
import os

# Add the project root directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

import click
from lib.models import session
from lib.models.member import Member
from lib.models.book import Book
from lib.models.meeting import Meeting
from lib.models.user import User
from datetime import datetime
from lib.auth import register_user, login_user
from lib.helpers import save_current_user, get_current_user, clear_current_user

@click.group()
def cli():
    pass

@cli.command()
@click.option('--username', prompt=True)
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True)
def register(username, password):
    message = register_user(username, password)
    click.echo(message)

@cli.command()
@click.option('--username', prompt=True)
@click.option('--password', prompt=True, hide_input=True)
def login(username, password):
    user, message = login_user(username, password)
    click.echo(message)
    if user:
        save_current_user(user.username)
        click.echo(f'Current user set to: {user.username}')

def ensure_authenticated(func):
    @click.pass_context
    def wrapper(ctx, *args, **kwargs):
        current_user = get_current_user()
        if not current_user:
            click.echo('You must be logged in to perform this action.')
            ctx.exit()
        else:
            click.echo(f'Authenticated as: {current_user}')
            return func(*args, **kwargs)
    return wrapper

@cli.command(name='add-member')
@ensure_authenticated
def add_member():
    name = input("Enter member name: ")
    email = input("Enter member email: ")
    member = Member(name=name, email=email)
    session.add(member)
    session.commit()
    click.echo(f"Member {name} added successfully!")

@cli.command(name='view-members')
@ensure_authenticated
def view_members():
    members = session.query(Member).all()
    for member in members:
        click.echo(member)

@cli.command(name='add-book')
@ensure_authenticated
def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    book = Book(title=title, author=author)
    session.add(book)
    session.commit()
    click.echo(f"Book {title} by {author} added successfully!")

@cli.command(name='view-books')
@ensure_authenticated
def view_books():
    books = session.query(Book).all()
    for book in books:
        click.echo(book)

@cli.command(name='schedule-meeting')
@ensure_authenticated
def schedule_meeting():
    member_id = input("Enter member ID: ")
    book_id = input("Enter book ID: ")
    date_str = input("Enter meeting date (YYYY-MM-DD): ")
    date = datetime.strptime(date_str, "%Y-%m-%d").date()
    notes = input("Enter meeting notes: ")
    meeting = Meeting(member_id=member_id, book_id=book_id, date=date, notes=notes)
    session.add(meeting)
    session.commit()
    click.echo("Meeting scheduled successfully!")

@cli.command(name='view-meetings')
@ensure_authenticated
def view_meetings():
    meetings = session.query(Meeting).all()
    for meeting in meetings:
        click.echo(meeting)

@cli.command(name='update-password')
@click.option('--new_password', prompt=True, hide_input=True, confirmation_prompt=True)
@ensure_authenticated
def update_password(new_password):
    user = session.query(User).filter_by(username=get_current_user()).first()
    if user:
        user.password = hash_password(new_password)
        session.commit()
        click.echo("Password updated successfully!")
    else:
        click.echo("User not found.")

@cli.command(name='delete-member')
@click.option('--member_id', prompt=True)
@ensure_authenticated
def delete_member(member_id):
    member = session.query(Member).filter_by(id=member_id).first()
    if member:
        session.delete(member)
        session.commit()
        click.echo("Member deleted successfully!")
    else:
        click.echo("Member not found.")

@cli.command(name='delete-book')
@click.option('--book_id', prompt=True)
@ensure_authenticated
def delete_book(book_id):
    book = session.query(Book).filter_by(id=book_id).first()
    if book:
        session.delete(book)
        session.commit()
        click.echo("Book deleted successfully!")
    else:
        click.echo("Book not found.")

@cli.command()
def exit_program():
    clear_current_user()
    click.echo("Goodbye!")
    exit()

if __name__ == '__main__':
    cli()
