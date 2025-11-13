from library_oop import Book, Member, Library

def test_book_class():
    print("="*60)
    print("Testing Book Class")
    print("="*60)

    book = Book(1, "Test Book", "Test Author", 2)
    
    # Test initial state
    print(f"Initial: {book}")
    assert book.available_copies == 2
    
    # Test successful borrow
    assert book.borrow() == True
    print(f"After 1st borrow: {book}")
    assert book.available_copies == 1
    
    # Test second successful borrow
    assert book.borrow() == True
    print(f"After 2nd borrow: {book}")
    assert book.available_copies == 0
    
    # Test failed borrow (no copies left)
    assert book.borrow() == False
    print(f"After failed borrow: {book}")
    assert book.available_copies == 0
    
    # Test return
    book.return_copy()
    print(f"After 1st return: {book}")
    assert book.available_copies == 1
    
    # Test returning more than total (should not exceed total)
    book.return_copy()
    book.return_copy()
    print(f"After over-return: {book}")
    assert book.available_copies == 2
    
    print("="*60)
    print("Book Class Tested")
    print("="*60+"\n")


def test_member_class():
    print("="*60)
    print("Testing Member Class")
    print("="*60)

    member = Member(101, "Alice", "alice@email.com")
    
    print(f"Initial: {member}")
    assert member.can_borrow() == True
    assert len(member.borrowed_books) == 0
    
    member.add_borrowed_book(1)
    print(f"After 1st borrow: {member}")
    assert len(member.borrowed_books) == 1
    
    member.add_borrowed_book(2)
    print(f"After 2nd borrow: {member}")
    assert member.can_borrow() == True
    
    member.add_borrowed_book(3)
    print(f"After 3rd borrow: {member}")
    assert member.can_borrow() == False
    
    member.remove_borrowed_book(2)
    print(f"After returning book 2: {member}")
    assert len(member.borrowed_books) == 2
    assert member.can_borrow() == True
    
    member.remove_borrowed_book(99)
    print(f"After failed return: {member}")
    assert len(member.borrowed_books) == 2

    print("="*60)
    print("Member Class Tested")
    print("="*60+"\n")


def test_library_class_basic():
    print("="*60)
    print("Testing Library Class (Basic)")
    print("="*60)

    library = Library()
    
    # Test adding books
    library.add_book(1, "Book A", "Author A", 1)
    assert library.find_book(1).title == "Book A"
    
    # Test adding members
    library.add_member(101, "Member 1", "m1@email.com")
    assert library.find_member(101).name == "Member 1"
    
    # Test finding non-existent items
    assert library.find_book(99) is None
    assert library.find_member(999) is None
    
    print("="*60)
    print("Library Class Basic Tested")
    print("="*60)

if __name__ == "__main__":
    test_book_class()
    test_member_class()
    test_library_class_basic()