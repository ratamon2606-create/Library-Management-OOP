class Book:
    def __init__(self, book_id, title, author, total_copies):
        self.id = book_id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies
    
    def borrow(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        return False
        
    def return_copy(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
    
    def __str__(self):
        return f"{self.title} by {self.author} ({self.available_copies} available)"


class Member:
    
    BORROW_LIMIT = 3
    
    def __init__(self, member_id, name, email):
        self.id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []
        
    def can_borrow(self):
        return len(self.borrowed_books) < self.BORROW_LIMIT

    def add_borrowed_book(self, book_id):
        if book_id not in self.borrowed_books:
            self.borrowed_books.append(book_id)
            
    def remove_borrowed_book(self, book_id):
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)

    def __str__(self):
        return f"Member: {self.name} ({self.email}) - {len(self.borrowed_books)} books borrowed"


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
    
    def add_book(self, book_id, title, author, total_copies):
        if book_id in self.books:
            print(f"Error: Book ID {book_id} already exists.")
            return
        book = Book(book_id, title, author, total_copies)
        self.books[book_id] = book
        print(f"Book '{title}' added successfully!")
        
    def add_member(self, member_id, name, email):
        if member_id in self.members:
            print(f"Error: Member ID {member_id} already exists.")
            return
        member = Member(member_id, name, email)
        self.members[member_id] = member
        print(f"Member '{name}' registered successfully!")

    def find_book(self, book_id):
        return self.books.get(book_id)
        
    def find_member(self, member_id):
        return self.members.get(member_id)

    def borrow_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        
        if not member:
            print("Error: Member not found!")
            return False
        
        if not book:
            print("Error: Book not found!")
            return False
        
        if not book.available_copies > 0:
            print("Error: No copies available!")
            return False
        
        if not member.can_borrow():
            print("Error: Member has reached borrowing limit!")
            return False
        
        book.borrow()
        member.add_borrowed_book(book_id)
        print(f"{member.name} borrowed '{book.title}'")
        return True

    def return_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if not member or not book:
            print("Error: Member or book not found!")
            return False
        
        if book_id not in member.borrowed_books:
            print("Error: This member hasn't borrowed this book!")
            return False
            
        book.return_copy()
        member.remove_borrowed_book(book_id)
        print(f"{member.name} returned '{book.title}'")
        return True

    def display_available_books(self):
        print("\n=== Available Books ===")
        available = [book for book in self.books.values() if book.available_copies > 0]
        if not available:
            print("No books currently available.")
            return
        for book in available:
            print(f"{book.title} by {book.author} - {book.available_copies} copies available")

    def display_member_books(self, member_id):
        member = self.find_member(member_id)
        if not member:
            print("Error: Member not found!")
            return
        
        print(f"\n=== Books borrowed by {member.name} ===")
        if not member.borrowed_books:
            print("No books currently borrowed")
        else:
            for book_id in member.borrowed_books:
                book = self.find_book(book_id)
                if book:
                    print(f"- {book.title} by {book.author}")
                    