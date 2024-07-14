
# Library Management System

This is a simple Library Management System implemented in Python using classes. It supports basic functionalities such as adding books, registering students, borrowing books, and returning books. The system includes both admin and student login features, providing different options based on the type of user.


## Features

### Admin Functions:
Add books to the library.\
View all books and registered students.

### Student Functions:
Borrow books.\
Return borrowed books.\
View their borrowed books.

## Classes
Book: Represents a book with attributes like book name, book ID, and availability status.
Student: Represents a student with attributes like student name, student ID, and a list of borrowed books.
Library: Manages the collection of books and students, and handles borrowing and returning books.
Admin: Represents an admin with an attribute for admin name.
## Usage

Run the script to start the Library Management System.
### Login Menu:
Admin Login: Allows the admin to add books and view the library.\
Student Login: Allows students to borrow and return books, and view their borrowed books.\
Exit: Exits the system.
### Admin Menu:
Add Book: Admin can add a new book to the library.\
View Library: Admin can view all the books and students in the library.\
Exit: Exits the admin menu.
### Student Menu:
Borrow Book: Students can borrow a book by specifying the book name.\
Return Book: Students can return a borrowed book by specifying the book name.\
View Borrowed Books: Students can view the list of books they have borrowed.\
Exit: Exits the student menu.