class Book:

    def __init__(self, Title: str, author: str, is_read: bool):
        self.title = Title
        self.author = author
        self.is_read = is_read
    

    def mark_as_read(self):
        self.is_read = True
        print(f"{self.title} o'qilgan deb belgilandi")
    

    def status(self):
        if self.is_read:
            print("o'qilgan")
        else:
            print("O'qilmagan")

book1 = Book("Atomic Habits", "James Clear", False)
book1.status()        
book1.mark_as_read() 
book1.status() 



