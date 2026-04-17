from product import Product
from product_manager import ProductManager

manager = ProductManager()

p1 = Product("Laptop PRO", 1200, 3)
p2 = Product("Telefon X", 700, 8)
p3 = Product("Gaming miš", 40, 30)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

# manager.display_products()
# print("Ukupna vrednost:", manager.total_value())


