class User: 
    def __init__(self, username: str, email: str, is_active: bool):
        self.username = username
        self.email = email
        self.is_active = is_active

    def activate(self) -> None:
        self.is_active = True
        print(f"{self.username} foydalanuvchisi faollashtirildi")
    

    def deactivate(self) -> None:
        self.is_active = False
        print(f"{self.username} foydalanuvchisi bloklandi")

user1 = User("ali123", "ali@gmail.com", False)
user1.activate()
user1.deactivate()