# BookWize

## Overview

BookWize is a comprehensive Book Club Management System designed to streamline the management of book clubs. The system features both a Command Line Interface (CLI) and a Graphical User Interface (GUI) built using Tkinter. It allows book club organizers to efficiently handle members, books, and meetings while ensuring secure access for different users.

## Features

### Command Line Interface (CLI)

1. **User Registration**
   - Securely register new users.
   - Command: `PYTHONPATH=. python lib/cli.py register --username <username> --password <password>`

2. **User Login**
   - Securely log in existing users.
   - Command: `PYTHONPATH=. python lib/cli.py login --username <username> --password <password>`

3. **Add Member**
   - Add a new member to the system.
   - Command: `PYTHONPATH=. python lib/cli.py add-member`

4. **View Members**
   - List all members in the system.
   - Command: `PYTHONPATH=. python lib/cli.py view-members`

5. **Add Book**
   - Add a new book to the system.
   - Command: `PYTHONPATH=. python lib/cli.py add-book`

6. **View Books**
   - List all books in the system.
   - Command: `PYTHONPATH=. python lib/cli.py view-books`

7. **Schedule Meeting**
   - Schedule a new meeting.
   - Command: `PYTHONPATH=. python lib/cli.py schedule-meeting`

8. **View Meetings**
   - List all meetings.
   - Command: `PYTHONPATH=. python lib/cli.py view-meetings`

9. **Update Password**
   - Update user passwords securely.
   - Command: `PYTHONPATH=. python lib/cli.py update-password --new-password <new_password>`

10. **Delete Member**
    - Delete a member by their ID.
    - Command: `PYTHONPATH=. python lib/cli.py delete-member`

11. **Delete Book**
    - Delete a book by its ID.
    - Command: `PYTHONPATH=. python lib/cli.py delete-book`

### Graphical User Interface (GUI)

1. **User Registration and Login**
   - Visual interface for secure user registration and login.
   - Buttons: "Register" and "Login"

2. **Add Member**
   - Form to add a new member.
   - Button: "Add Member"

3. **View Members**
   - List all members.
   - Button: "View Members"

4. **Add Book**
   - Form to add a new book.
   - Button: "Add Book"

5. **View Books**
   - List all books.
   - Button: "View Books"

6. **Schedule Meeting**
   - Form to schedule a new meeting.
   - Button: "Schedule Meeting"

7. **View Meetings**
   - List all meetings.
   - Button: "View Meetings"

8. **Update Password**
   - Form to update user passwords.
   - Button: "Update Password"

9. **Delete Member**
   - Form to delete a member by ID.
   - Button: "Delete Member"

10. **Delete Book**
    - Form to delete a book by ID.
    - Button: "Delete Book"

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/bookwize.git
    cd bookwize
    ```

2. Set up the virtual environment and install dependencies:
    ```sh
    pipenv install
    pipenv shell
    ```

3. Create the database:
    ```sh
    PYTHONPATH=. python lib/create_tables.py
    ```


## Usage

### Command Line Interface (CLI)

- **Register a new user**:
    ```sh
    PYTHONPATH=. python lib/cli.py register --username JohnDoe --password Password123
    ```

- **Login an existing user**:
    ```sh
    PYTHONPATH=. python lib/cli.py login --username JohnDoe --password Password123
    ```

- **Add a member**:
    ```sh
    PYTHONPATH=. python lib/cli.py add-member
    ```

- **View members**:
    ```sh
    PYTHONPATH=. python lib/cli.py view-members
    ```

- **Add a book**:
    ```sh
    PYTHONPATH=. python lib/cli.py add-book
    ```

- **View books**:
    ```sh
    PYTHONPATH=. python lib/cli.py view-books
    ```

- **Schedule a meeting**:
    ```sh
    PYTHONPATH=. python lib/cli.py schedule-meeting
    ```

- **View meetings**:
    ```sh
    PYTHONPATH=. python lib/cli.py view-meetings
    ```

- **Update password**:
    ```sh
    PYTHONPATH=. python lib/cli.py update-password --new-password NewPassword123
    ```

- **Delete a member**:
    ```sh
    PYTHONPATH=. python lib/cli.py delete-member
    ```

- **Delete a book**:
    ```sh
    PYTHONPATH=. python lib/cli.py delete-book
    ```

### Graphical User Interface (GUI)

1. Start the GUI:
    ```sh
    PYTHONPATH=. python book_club_ui.py
    ```

2. Use the buttons to navigate through the features:
    - Register/Login
    - Add/View Members
    - Add/View Books
    - Schedule/View Meetings
    - Update Password
    - Delete Member
    - Delete Book

## Conclusion

BookWize is a robust and user-friendly Book Club Management System designed to meet the needs of book club organizers. It provides secure access, efficient management of members, books, and meetings, and is built with both CLI and GUI for flexibility. Thank you for using BookWize!


