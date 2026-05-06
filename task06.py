class Student:

    def __init__(self, name: str, age: int, grade: int):
        self.n = name
        self.a = age
        self.g = grade 


    def info(self) -> None:
        print(f"information about student: Name: {self.n}, Age: {self.a}, Grade: {self.g}")

student01 = Student("ali", 15, 9)
student02 = Student("vali", 18, 11)
student03 = Student("sami", 16, 10)

student01.info()