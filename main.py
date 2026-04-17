from product import Product
from product_manager import ProductManager
from cart import Cart

manager = ProductManager()

p1 = Product("Laptop PRO", 1200, 3)
p2 = Product("Telefon X", 700, 8)
p3 = Product("Gaming miš", 40, 30)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

cart = Cart()

cart.add_to_cart(p1)
cart.add_to_cart(p2)
cart.add_to_cart(p3)

cart.display_cart()
print("Ukupno za naplatu:", cart.total_price())