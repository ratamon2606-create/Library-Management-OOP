# Library Management System - OOP Refactor

## 1. Project Overview

This project is a refactoring of a simple procedural Python script for a library management system into a robust, Object-Oriented (OOP) design. The goal is to improve modularity, maintainability, and encapsulation by modeling the system using three core classes: `Book`, `Member`, and `Library`.

The system supports core library functions:
* Managing a collection of books
* Registering new members
* Processing book borrowing and returning transactions
* Enforcing borrowing rules (e.g., limits, availability)
* Displaying reports on available books and member checkouts

## 2. Project Structure

The repository is organized into two main parts: the original procedural code and the new OOP solution.

library-management-oop/  
&ensp│   
&ensp├── README.md  
&ensp│  
&ensp├── procedural_version/  
&ensp│&emsp├── library_procedural.py  
&ensp│&emsp└── test_procedural.py  
&ensp│   
&ensp└── oop_solution/  
&ensp&emsp ├── library_oop.py  
&ensp&emsp └── test_oop.py  

## 3. Design Overview

The OOP solution is built around three classes that interact with each other. The `Library` class acts as the main controller, while `Book` and `Member` manage their own internal state.

### Book Class
Represents a single book title and its inventory.

* **Attributes:**
    * `id` (int): Unique identifier for the book.
    * `title` (str): The book's title.
    * `author` (str): The book's author.
    * `total_copies` (int): The total number of copies owned by the library.
    * `available_copies` (int): The number of copies *currently* available to borrow.
* **Key Methods:**
    * `borrow()`: Decrements `available_copies`. Returns `True` if successful, `False` if no copies are left.
    * `return_copy()`: Increments `available_copies` (up to `total_copies`).

### Member Class
Represents a registered library member and their borrowing status.

* **Attributes:**
    * `id` (int): Unique identifier for the member.
    * `name` (str): The member's name.
    * `email` (str): The member's email address.
    * `borrowed_books` (list): A list of `book_id`s for books the member currently has checked out.
    * `BORROW_LIMIT` (int): A class-level constant (set to 3).
* **Key Methods:**
    * `can_borrow()`: Returns `True` if the member is under their borrow limit.
    * `add_borrowed_book(book_id)`: Appends a `book_id` to the `borrowed_books` list.
    * `remove_borrowed_book(book_id)`: Removes a `book_id` from the `borrowed_books` list.

### Library Class
Acts as the central controller for the entire system, managing the collections and enforcing business logic.

* **Attributes:**
    * `books` (dict): A dictionary mapping `book_id` to `Book` objects for fast lookup.
    * `members` (dict): A dictionary mapping `member_id` to `Member` objects.
* **Key Methods:**
    * `add_book(...)`: Creates a new `Book` object and adds it to the `books` collection.
    * `add_member(...)`: Creates a new `Member` object and adds it to the `members` collection.
    * `find_book(book_id)`: Safely finds and returns a `Book` object from the collection.
    * `find_member(member_id)`: Safely finds and returns a `Member` object.
    * `borrow_book(member_id, book_id)`: The main transaction method. It finds the member and book, then checks all business rules (e.g., "Does the member exist?", "Does the book exist?", "Are copies available?", "Is the member under their limit?"). If all checks pass, it calls the `borrow()` method on the `Book` and `add_borrowed_book()` on the `Member`.
    * `return_book(member_id, book_id)`: The main return method. It checks that the member and book exist and that the member *actually* borrowed that book. If checks pass, it calls `return_copy()` on the `Book` and `remove_borrowed_book()` on the `Member`.
    * `display_available_books()`: Prints a report of all books with > 0 `available_copies`.
    * `display_member_books(member_id)`: Prints a report of all books borrowed by a specific member.

## 4. Testing

The solution includes a comprehensive test suite in `oop_solution/test_oop.py`. This script is designed to be run from the command line and validates the entire system's functionality, including both basic operations and critical edge cases.

### Test Coverage

The `test_library_system_oop()` function covers the following scenarios, mirroring the original procedural test:

* **Basic Operations:**
    * Adding multiple books and members.
    * Displaying available books (before and after borrowing).
    * Successful borrowing and returning of books.
    * Displaying a member's borrowed books.
* **Edge Cases:**
    * Attempting to borrow the last available copy.
    * Attempting to borrow a book that is out of stock (unavailable).
    * Attempting to borrow a book when the member has reached their 3-book limit.
    * Attempting to return a book the member never borrowed.
    * Attempting transactions with non-existent `book_id`s or `member_id`s.

### How to Run the Test

You can run the full test suite from your terminal.

1.  Navigate to the project's root directory (`library-management-oop/`).
2.  Execute the `test_oop.py` script:

    ```bash
    python oop_solution/test_oop.py
    ```

3.  Observe the console output, which will print the status of each test step, identical to the test output from the procedural version.