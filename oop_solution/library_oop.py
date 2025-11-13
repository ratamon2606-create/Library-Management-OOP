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