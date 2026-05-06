class Book:

    def __init__(self, Title: str, author: str, is_read: bool):
        self.title = Title
        self.author = author
        self.is_read = is_read
    

    def mark_as_read(self):
        self.title = True
        print(f"{self.title} o'qilgan deb belgilandi")

    
    def status(self):
        if self.is_read:
            print(f"{self.title}: O'qilgan")
        else:
            print(f"{self.title}: O'qilmagan")
        

book1 = Book("Atomic Habits", "James Clear", True)
book2 = Book("Deep Work", "Cal Newport", False)
book3 = Book("Clean Code", "Robert C. Martin", True)
book4 = Book("The Alchemist", "Paulo Coelho", False)

book1.mark_as_read()
book3.mark_as_read()

book1.status()
book2.status()
book3.status()
book4.status()