class Product:
    def __init__(self, Name: str, Price: float, Category: str, In_stock: bool): 
        self.name = Name
        self.Price = Price
        self. Category =  Category
        self.In_stock= In_stock
    

    def check_stock(self) -> None:
        if self.In_stock:
             print(f"{self.name} omborda mavjud")
        else:
            print(f"{self.name} hozirda tugagan")


product1 = Product("AirPods", 199.99, "electronics", True)
product2 = Product("iPhone 13", 999.99, "electronics", False)

product1.check_stock()
product2.check_stock()

       
