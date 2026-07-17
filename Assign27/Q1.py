class BookStore:
    NoOfBooks = 0

    def __init__(self, BookName, Author):
        self.BookName = BookName
        self.Author = Author
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1
        
    def Display(self):
        print(f"{self.BookName} by {self.Author}. No of books: {self.NoOfBooks}")

obj1 = BookStore("Linux System Programming", "Robert Love")
obj1.Display()

obj2 = BookStore("C Programming", "Dennis Ritchie")
obj2.Display()

obj3 = BookStore("C++ Programming", "Vens Voogl")
obj3.Display()


