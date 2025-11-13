from library_oop import Book

def test_book_class():
    print("=" * 60)
    print("Testing Book Class")
    print("=" * 60)

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
    
    print("\n" + "=" * 60)
    print("TEST COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    test_book_class()
    