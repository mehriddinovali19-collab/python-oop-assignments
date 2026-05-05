class Car:

    def __init__(self, brand: str, model: str | int, year: int):
        self.brand = brand
        self.model = model
        self.year = year



c1 = Car("BMW", "X5", "2022")

print(c1.brand, c1.model, c1.year)