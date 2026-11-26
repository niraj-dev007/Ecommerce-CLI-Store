from models import CartItem 

class Cart:
    def __init__(self):
        self.items = []
        
    def add_to_cart(self, product, qty):
        if qty > product.stock:
            print(f"Stock kam hai! Sirf {product.stock} available hai.")
            return
        
        elif qty<=0:
            print("The Quantity must be at least 1.")
            
        else:
            new_item = CartItem(product, qty)
            
            existing_item = None
            for item in self.items:
                if item.product.product_id == product.product_id:
                    existing_item = item
                    break
            if existing_item:
                current_qty = existing_item.quantity + qty
            else:
                current_qty = qty
                
            if current_qty > product.stock:
                print(f"Stock is low. You already have {existing_item.quantity if existing_item else 0} units in your cart. Only {product.stock} units are avaliable in the store.")
                return
            
            if existing_item:
                existing_item.quantity += qty
                print(f"Updated {product.name} quantity to {existing_item.quantity}!")
                
            else:
                self.items.append(new_item)
                print(f"{product.name} ({qty} pcs) cart mein add ho gaya!")
    
    def get_subtotal(self):
        total = 0
        for item in self.items:
            total += item.get_total_price()
        return total
            
    def view_cart(self):
        if len(self.items) == 0:
            print("Empty Cart!")
        else:
            for item in self.items:
                item.display()
            print(f"Subtotal: ₹{self.get_subtotal()}")
    
    def remove_from_cart(self, product_id):
        if len(self.items) == 0:
            print("Empty cart!")
        else:
            for i in self.items:
                if i.product.product_id == product_id:
                    self.items.remove(i)
                    print(f"Item {i.product.name} has removed!")
                    return
            print(f"This product ID {product_id} is not in your cart!")
                    
    def clear_cart(self):
        self.items = []
        return