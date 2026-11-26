import json
from models import Product

class Inventory:
    def __init__(self):
        self.products = []
        self.file_name = "products.json"
        self.load_products()
        
    def load_products(self):
        try:
            with open(self.file_name, "r") as f:
                data = json.load(f)
                for item in data:
                    product = Product(item["product_id"], item["name"], item["price"], item["stock"])
                    self.products.append(product)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Opening first time shop, so there are added some default products.")
            self.products = [
                Product(101, "Laptop", 50000, 5),    
                Product(102, "Wireless Mouse", 500, 20),    
                Product(103, "Machanical Keyboard", 1500, 10),    
                Product(104, "Headphones", 2000, 8),    
            ]
            self.save_products()
            
    def save_products(self):
        data = []
        for p in self.products:
            data.append(p.to_dict())
            
        with open(self.file_name, "w") as f:
            json.dump(data, f, indent=4)
            
    def display_products(self):
        if len(self.products) == 0:
            print("There is no goods in the shop.")
            return
        else:
            for p in self.products:
                p.display()
            
    def get_product(self, product_id):
            for p in self.products:
                if p.product_id == product_id:
                    return p
            return None

    def reduce_stock(self, product_id, qty):
        product = self.get_product(product_id)
        if product:
            product.stock -= qty
            self.save_products()