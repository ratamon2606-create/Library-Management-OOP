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
    