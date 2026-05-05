class User:

    def __init__(self, username: str, email: str | int, is_active: bool):
        self.username = username
        self.email = email 
        self.is_active = is_active

user01 = User("shox", "Jumanov@gmail.com", True)
user02 = User("sami", "samotov@gmail.ru", False)
user03 = User("ali", "umanov@gmail.uz", True)

print(user01.username, user01.email, user01.is_active)
print(user02.username, user02.email, user02.is_active)
print(user03.username, user02.email, user03.is_active)