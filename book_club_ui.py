import tkinter as tk
from tkinter import messagebox
from lib.models import session
from lib.models.member import Member
from lib.models.book import Book
from lib.models.meeting import Meeting
from lib.models.user import User
from lib.auth import register_user, login_user, hash_password
from datetime import datetime

# Global variable to store current user
current_user = None

class BookClubApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Book Club Management")
        self.geometry("400x600")

        self.current_user = None

        # Create the main frame
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(pady=10)

        # Create the login frame
        self.login_frame = tk.Frame(self.main_frame)
        self.login_frame.pack()

        # Username entry
        self.username_label = tk.Label(self.login_frame, text="Username:")
        self.username_label.grid(row=0, column=0, padx=5, pady=5)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        # Password entry
        self.password_label = tk.Label(self.login_frame, text="Password:")
        self.password_label.grid(row=1, column=0, padx=5, pady=5)
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        # Login and register buttons
        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        self.login_button.grid(row=2, column=0, padx=5, pady=5)
        self.register_button = tk.Button(self.login_frame, text="Register", command=self.register)
        self.register_button.grid(row=2, column=1, padx=5, pady=5)

        # Create the actions frame
        self.actions_frame = tk.Frame(self.main_frame)
        self.actions_frame.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        global current_user
        current_user, message = login_user(username, password)
        if current_user:
            messagebox.showinfo("Login", "Login successful!")
            self.show_actions()
        else:
            messagebox.showerror("Login", message)

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        message = register_user(username, password)
        if "successfully" in message:
            messagebox.showinfo("Register", message)
        else:
            messagebox.showerror("Register", message)

    def show_actions(self):
        self.login_frame.pack_forget()

        tk.Button(self.actions_frame, text="Add Book", command=self.add_book).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(self.actions_frame, text="View Books", command=self.view_books).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(self.actions_frame, text="Add Member", command=self.add_member).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(self.actions_frame, text="View Members", command=self.view_members).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(self.actions_frame, text="Schedule Meeting", command=self.schedule_meeting).grid(row=2, column=0, padx=5, pady=5)
        tk.Button(self.actions_frame, text="View Meetings", command=self.view_meetings).grid(row=2, column=1, padx=5, pady=5)
        tk.Button(self.actions_frame, text="Update Password", command=self.update_password).grid(row=3, column=0, padx=5, pady=5)
        tk.Button(self.actions_frame, text="Delete Member", command=self.delete_member).grid(row=3, column=1, padx=5, pady=5)
        tk.Button(self.actions_frame, text="Delete Book", command=self.delete_book).grid(row=4, column=0, padx=5, pady=5)
        tk.Button(self.actions_frame, text="Logout", command=self.logout).grid(row=5, column=0, columnspan=2, pady=10)

    def add_book(self):
        AddBookWindow(self)

    def view_books(self):
        ViewBooksWindow(self)

    def add_member(self):
        AddMemberWindow(self)

    def view_members(self):
        ViewMembersWindow(self)

    def schedule_meeting(self):
        ScheduleMeetingWindow(self)

    def view_meetings(self):
        ViewMeetingsWindow(self)

    def update_password(self):
        UpdatePasswordWindow(self)

    def delete_member(self):
        DeleteMemberWindow(self)

    def delete_book(self):
        DeleteBookWindow(self)

    def logout(self):
        global current_user
        current_user = None
        self.actions_frame.pack_forget()
        self.login_frame.pack()

class AddBookWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Add Book")
        self.geometry("300x200")

        tk.Label(self, text="Title:").pack(pady=5)
        self.title_entry = tk.Entry(self)
        self.title_entry.pack(pady=5)

        tk.Label(self, text="Author:").pack(pady=5)
        self.author_entry = tk.Entry(self)
        self.author_entry.pack(pady=5)

        tk.Button(self, text="Add", command=self.add_book).pack(pady=10)

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        book = Book(title=title, author=author)
        session.add(book)
        session.commit()
        messagebox.showinfo("Add Book", f"Book '{title}' by {author} added successfully!")
        self.destroy()

class ViewBooksWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("View Books")
        self.geometry("400x400")

        books = session.query(Book).all()
        for book in books:
            tk.Label(self, text=str(book)).pack(pady=5)

class AddMemberWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Add Member")
        self.geometry("300x200")

        tk.Label(self, text="Name:").pack(pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=5)

        tk.Label(self, text="Email:").pack(pady=5)
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)

        tk.Button(self, text="Add", command=self.add_member).pack(pady=10)

    def add_member(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        member = Member(name=name, email=email)
        session.add(member)
        session.commit()
        messagebox.showinfo("Add Member", f"Member {name} added successfully!")
        self.destroy()

class ViewMembersWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("View Members")
        self.geometry("400x400")

        members = session.query(Member).all()
        for member in members:
            tk.Label(self, text=str(member)).pack(pady=5)

class ScheduleMeetingWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Schedule Meeting")
        self.geometry("300x300")

        tk.Label(self, text="Member ID:").pack(pady=5)
        self.member_id_entry = tk.Entry(self)
        self.member_id_entry.pack(pady=5)

        tk.Label(self, text="Book ID:").pack(pady=5)
        self.book_id_entry = tk.Entry(self)
        self.book_id_entry.pack(pady=5)

        tk.Label(self, text="Date (YYYY-MM-DD):").pack(pady=5)
        self.date_entry = tk.Entry(self)
        self.date_entry.pack(pady=5)

        tk.Label(self, text="Notes:").pack(pady=5)
        self.notes_entry = tk.Entry(self)
        self.notes_entry.pack(pady=5)

        tk.Button(self, text="Schedule", command=self.schedule_meeting).pack(pady=10)

    def schedule_meeting(self):
        member_id = self.member_id_entry.get()
        book_id = self.book_id_entry.get()
        date_str = self.date_entry.get()
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        notes = self.notes_entry.get()
        meeting = Meeting(member_id=member_id, book_id=book_id, date=date, notes=notes)
        session.add(meeting)
        session.commit()
        messagebox.showinfo("Schedule Meeting", "Meeting scheduled successfully!")
        self.destroy()

class ViewMeetingsWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("View Meetings")
        self.geometry("400x400")

        meetings = session.query(Meeting).all()
        for meeting in meetings:
            tk.Label(self, text=str(meeting)).pack(pady=5)

class UpdatePasswordWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Update Password")
        self.geometry("300x150")

        tk.Label(self, text="New Password:").pack(pady=5)
        self.new_password_entry = tk.Entry(self, show="*")
        self.new_password_entry.pack(pady=5)

        tk.Button(self, text="Update", command=self.update_password).pack(pady=10)

    def update_password(self):
        new_password = self.new_password_entry.get()
        global current_user
        user = session.query(User).filter_by(username=current_user.username).first()
        if user:
            user.password = hash_password(new_password)
            session.commit()
            messagebox.showinfo("Update Password", "Password updated successfully!")
            self.destroy()
        else:
            messagebox.showerror("Error", "User not found.")

class DeleteMemberWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Delete Member")
        self.geometry("300x150")

        tk.Label(self, text="Member ID:").pack(pady=5)
        self.member_id_entry = tk.Entry(self)
        self.member_id_entry.pack(pady=5)

        tk.Button(self, text="Delete", command=self.delete_member).pack(pady=10)

    def delete_member(self):
        member_id = self.member_id_entry.get()
        member = session.query(Member).filter_by(id=member_id).first()
        if member:
            session.delete(member)
            session.commit()
            messagebox.showinfo("Delete Member", "Member deleted successfully!")
            self.destroy()
        else:
            messagebox.showerror("Error", "Member not found.")

class DeleteBookWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Delete Book")
        self.geometry("300x150")

        tk.Label(self, text="Book ID:").pack(pady=5)
        self.book_id_entry = tk.Entry(self)
        self.book_id_entry.pack(pady=5)

        tk.Button(self, text="Delete", command=self.delete_book).pack(pady=10)

    def delete_book(self):
        book_id = self.book_id_entry.get()
        book = session.query(Book).filter_by(id=book_id).first()
        if book:
            session.delete(book)
            session.commit()
            messagebox.showinfo("Delete Book", "Book deleted successfully!")
            self.destroy()
        else:
            messagebox.showerror("Error", "Book not found.")

if __name__ == "__main__":
    app = BookClubApp()
    app.mainloop()
