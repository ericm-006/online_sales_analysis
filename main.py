from product import Product
from product_manager import ProductManager

manager = ProductManager()

p1 = Product("Laptop", 1000, 5)
p2 = Product("Telefon", 500, 10)
p3 = Product("Miš", 20, 50)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

manager.display_products()
print("Ukupna vrednost:", manager.total_value())



from cart import Cart

cart = Cart()

cart.add_to_cart(p1)
cart.add_to_cart(p2)
cart.add_to_cart(p3)

cart.display_cart()
print("Ukupno za naplatu:", cart.total_price())