class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
        
    def display(self):
        print(f"[{self.product_id}] {self.name} - ₹{self.price} | Stock: {self.stock}")
        
    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }
        
class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        
    def get_total_price(self):
        return self.product.price * self.quantity
    
    def display(self):
        print(f"{self.product.name} X {self.quantity} = ₹{self.get_total_price()}")