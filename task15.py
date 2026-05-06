class Product:
    def __init__(self, name: str, price: float, in_stock: bool):
        self.name = name 
        self.price = price
        self.in_stock = in_stock


p1 = Product("Olma", 10.5, True)
p2 = Product("Banan", 8.0, False)
p3 = Product("Uzum", 15.0, True)
p4 = Product("Non", 5.0, True)
p5 = Product("Sut", 12.0, False)

products = [p1, p2, p3, p4, p5 ]
total_price = 0
for product in products:
    if product.in_stock:
        total_price += product.price

print(f"Ombordagi mahsulotlar narxi: {total_price}")