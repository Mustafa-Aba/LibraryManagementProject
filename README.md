Project Name: Library Management System

Description:

This project implements a user-friendly and efficient Library Management System using object-oriented programming principles in Python. It enables you to manage a library's book collection effectively, including adding, borrowing, returning, and searching for books.

Key Features:

  Object-oriented design ensures modularity and maintainability.
  Persistent data storage using a books.txt file, guaranteeing data integrity.
  Intuitive menu-driven interface for easy interaction.
  Comprehensive book management functionalities:
    -Add new books to the library, specifying title, author, release year, and number of pages.
    -List all books in the library.
    -Remove books from the library.
Getting Started:

1.Prerequisites: Python 3.x (any version).
2.Run the project:
  Clone or download the project repository to your local machine.
  Open a terminal window in the project directory.
  Run the main.py script: python main.py.
3.Follow the on-screen menu: The system will present you with options to add, list or remove for books.
Code Structure:

Library class:
  -Constructor and destructor for opening/closing the books.txt file.
  -list_books: Reads and displays all books from the file.
  -add_book: Prompts for book details and adds them to the file.
  -remove_book: Prompts for a book title and removes it from the file.
Example Usage:

Welcome to the Library Management System!

*** MENU ***
1) List Books
2) Add Book
3) Remove Book
4) Exit

Enter your choice: 1

**List of Books:**

- The Lord of the Rings, J.R.R. Tolkien, 1954, 1170 pages
- The Alchemist, Paulo Coelho, 1988, 168 pages

... (similar interactions for other functionalities)

Enter your choice: 4

Goodbye!
Additional Notes:

The books.txt file is created automatically when you first run the program.
You can customize the menu options and functionalities as needed.
Consider adding error handling and validation for robust operation.
Contribution:

Feel free to contribute to this project by submitting pull requests with improvements, new features, or bug fixes.

