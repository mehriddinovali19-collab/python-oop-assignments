class Student:

    def __init__(self, name: str, age: int, grade: int):
        self.name = name
        self.age = age
        self.grade = grade 

student01 = Student("ali", "jamshidov", 9)
student02 = Student("guli", "jamshidova", 8)
student03 = Student("Jamshid", "Jumanov", 4)

print(student01.name, student01.age, student01.grade)
print(student02.name, student02.age, student02.grade)
print(student03.name, student03.age, student03.grade)
