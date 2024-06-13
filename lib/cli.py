import click
from models import session
from models.member import Member
from models.book import Book
from models.meeting import Meeting
from models.user import User
from datetime import datetime
from auth import register_user, login_user

current_user = None

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
    global current_user
    current_user, message = login_user(username, password)
    click.echo(message)

def ensure_authenticated(func):
    def wrapper(*args, **kwargs):
        if not current_user:
            click.echo('You must be logged in to perform this action.')
            return
        return func(*args, **kwargs)
    return wrapper

@cli.command()
@ensure_authenticated
def add_member():
    name = input("Enter member name: ")
    email = input("Enter member email: ")
    member = Member(name=name, email=email)
    session.add(member)
    session.commit()
    click.echo(f"Member {name} added successfully!")

@cli.command()
@ensure_authenticated
def view_members():
    members = session.query(Member).all()
    for member in members:
        click.echo(member)

@cli.command()
@ensure_authenticated
def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    book = Book(title=title, author=author)
    session.add(book)
    session.commit()
    click.echo(f"Book {title} by {author} added successfully!")

@cli.command()
@ensure_authenticated
def view_books():
    books = session.query(Book).all()
    for book in books:
        click.echo(book)

@cli.command()
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

@cli.command()
@ensure_authenticated
def view_meetings():
    meetings = session.query(Meeting).all()
    for meeting in meetings:
        click.echo(meeting)

@cli.command()
def exit_program():
    click.echo("Goodbye!")
    exit()

if __name__ == '__main__':
    cli()
