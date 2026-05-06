class Book:
    def __init__(self, title: str, author: str, is_read: bool):
        self.title = title 
        self.author = author
        self.is_read = is_read

    def mark_as_read(self):
        self.is_read = True

    def status(self):
        if self.is_read:
            print(f"{self.title}: O'qilgan")
        else:
            print(f"{self.title}: O'qilmagan")

b1 = Book("Atomic Habits", "James Clear", True)
b2 = Book("Clean Code", "Robert C. Martin", False)
b3 = Book("1984", "George Orwell", True)
b4 = Book("The Alchemist", "Paulo Coelho", False)
b5 = Book("Deep Work", "Cal Newport", True)

books = [b1, b2, b3, b4, b5]

b1.mark_as_read()
b3.mark_as_read()

print("Barcha kitoblar holati:")
for book in books:
    book.status()

print("\n O'qilgan kitoblar:")
for book in books:
    if book.is_read:
        print(book.title)

