print("********************Welcome to Library Management System********************")

class Book:
    def __init__(self, book_name, book_id):
        self.book_name = book_name
        self.book_id = book_id
        self.is_available = True

    def __str__(self) -> str:
        return f'Name of book: {self.book_name}, Book ID: {self.book_id}, Available?: {self.is_available}'

class Student:
    def __init__(self, student_name, student_id):
        self.student_name = student_name
        self.student_id = student_id
        self.borrowed_books = []

    def borrow(self, book):
        if book.is_available:
            book.is_available = False
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book)
            return True
        return False

    def __str__(self):
        books = ', '.join([book.book_name for book in self.borrowed_books])
        return f'{self.student_name} borrowed books: {books}.'

class Library:
    def __init__(self):
        self.books = []
        self.students = []

    def add_book(self, book):
        self.books.append(book)

    def add_student(self, student):
        self.students.append(student)

    def search_book(self, book_name):
        for book in self.books:
            if book.book_name == book_name:
                return book
        return None

    def borrow(self, student_name, book_name):
        student = next((s for s in self.students if s.student_name == student_name), None)
        book = self.search_book(book_name)
        if student and book:
            return student.borrow(book)
        return False

    def return_book(self, student_name, book_name):
        student = next((s for s in self.students if s.student_name == student_name), None)
        book = self.search_book(book_name)
        if student and book:
            return student.return_book(book)
        return False

    def __str__(self):
        books = '\n'.join([str(book) for book in self.books])
        students = '\n'.join([str(student) for student in self.students])
        return f'Library Books:\n{books}\n\nLibrary Members:\n{students}'

class Admin:
    def __init__(self, admin_name):
        self.admin_name = admin_name

def admin_menu(library):
    while True:
        print("\nAdmin Menu:")
        print("1. Add Book")
        print("2. View Library")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            book_name = input("Enter book name: ")
            book_id = input("Enter book ID: ")
            book = Book(book_name, book_id)
            library.add_book(book)
            print(f'Book "{book_name}" added successfully.')
        elif choice == '2':
            print(library)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def student_menu(library, student):
    while True:
        print("\nStudent Menu:")
        print("1. Borrow Book")
        print("2. Return Book")
        print("3. View Borrowed Books")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            book_name = input("Enter book name: ")
            if library.borrow(student.student_name, book_name):
                print(f'Book "{book_name}" borrowed successfully.')
            else:
                print(f'Failed to borrow book "{book_name}".')
        elif choice == '2':
            book_name = input("Enter book name: ")
            if library.return_book(student.student_name, book_name):
                print(f'Book "{book_name}" returned successfully.')
            else:
                print(f'Failed to return book "{book_name}".')
        elif choice == '3':
            print(student)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

# Main program
library = Library()

admin = Admin("Admin1")
students = [Student("Bigyan Aryal", "1"), Student("Bruce Banner", "2")]

for student in students:
    library.add_student(student)

while True:
    print("\nLogin Menu:")
    print("1. Admin Login")
    print("2. Student Login")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        admin_menu(library)
    elif choice == '2':
        student_name = input("Enter student name: ")
        student = next((s for s in library.students if s.student_name == student_name), None)
        if student:
            student_menu(library, student)
        else:
            print("Student not found.")
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")



    

