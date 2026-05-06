class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age 
    

    def show_info(self):
        print(f"Ismi: {self.name}, Yosh: {self.age}")

s1 = Student("Ali", 17)
s2 = Student("Vali", 19)
s3 = Student("Sami", 18)
s4 = Student("Olim", 20)
s5 = Student("Zara", 16)

students = [s1, s2, s3, s4, s5]

oldest = max(students, key= lambda students: students.age)

oldest.show_info()