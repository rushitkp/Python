#Write a program in python to implement Library Management System using file handling technique.System should perform below operations.
#a. Issue a book for student.
#b. List information today’s issued books.
#(Note: Use of object oriented paradigm is compulsory.)


import datetime

class LibraryManagementSystem:
    def __init__(self, books_file='books.txt', issued_books_file='issued_books.txt'):
        self.books_file = books_file
        self.issued_books_file = issued_books_file

    def issue_book(self, book_id, student_name):
        with open(self.issued_books_file, 'a') as file:
            file.write(f"{book_id},{student_name},{datetime.datetime.now()}\n")

    def list_issued_books_for_today(self):
        today = datetime.date.today()
        with open(self.issued_books_file, 'r') as file:
            for line in file:
                book_id, student_name, issue_date = line.strip().split(',')
                issue_date = datetime.datetime.strptime(issue_date, '%Y-%m-%d %H:%M:%S.%f').date()
                if issue_date == today:
                    print(f"Book ID: {book_id}, Student Name: {student_name}, Issue Date: {issue_date}")

# Create an instance of LibraryManagementSystem
library_system = LibraryManagementSystem()

# Issue a book
book_id = input("Enter Book ID: ")
student_name = input("Enter Student Name: ")
library_system.issue_book(book_id, student_name)
print("Book issued successfully.")

# List information about today's issued books
print("Today's Issued Books:")
library_system.list_issued_books_for_today()
