from inventory import Inventory
from cart import Cart
from datetime import datetime

inventory = Inventory()
cart = Cart()

while True:
    print("""
          
        |====================================|
        |       🛍️  APNA STORE CLI  🛍️         |
        |====================================|
        |    1. View All Products            |
        |------------------------------------|
        |    2. Add to Cart                  |
        |------------------------------------|
        |    3. View Cart                    |
        |------------------------------------|
        |    4. Remove from Cart             |
        |------------------------------------|
        |    5. Checkout & Print Bill        |
        |------------------------------------|
        |    6. Exit                         |
        |====================================|
            """)
    try:
        choice = int(input("Choose option.: ").strip())
    except ValueError:
        print("Enter only numbers!")
        
    if choice == 1:
        inventory.display_products()
        
    elif choice == 2:
        while True:
            try:
                p_id = int(input("Enter product ID.: ").strip())
            except ValueError:
                print("Enter only numbers!")

            product = inventory.get_product(p_id)
            if product is None:
                print("This product is not in store yet!")
                
            else:
                try: 
                    qty = int(input(f"How many pcs of {product.name} do you need? ").strip())
                    cart.add_to_cart(product, qty)
                    
                except ValueError:
                    print("Enter only numbers!")
                    
            more = input("\nDo you want to bye anything else?(y/n) ").strip().lower()
            
            if more != 'y':
                break
            
                
    elif choice == 3:
        cart.view_cart()
        
    elif choice == 4:
        cart.view_cart()
        try:
            p_id = int(input("Enter Product ID to remove: "))
            cart.remove_from_cart(p_id)
        except ValueError:
            print("Enter Valid ID (only numbers.)")
        
    elif choice == 5:
        if len(cart.items) == 0:
            print("Cart id emmpty. First few purchased items.")
            
        else:
            subtotal = cart.get_subtotal()
            coupon = input("Is there a coupon code? (If not then press enter!)").strip().upper()
            
            discount = 0
            if coupon == "DISCOUNT10":
                discount = subtotal*0.10
                print("Coupon Code has beed Applied, and you got a flat 10% Discount!")
            
            elif coupon == "":
                print("No Coupon Code Found. No Discount.")
                
            else:
                print(f"Coupon code ({coupon}) is invalid. No Discount!")
                
            gst = (subtotal - discount) * 0.18
            final_total = (subtotal-discount)  + gst
            
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            print("\n"+ "="*60)
            print("             🧾  TAX INVOICE / CASH RECEIPT")
            print("                🛍️  APNA STORE PVT LTD")
            print(f"             Date: {now}")
            print("=" * 60)
            print(f"{'Item Name':<22}{'Qty':<8}{'Price':<14}{'Total':<14}")
            print("-" * 60)
            
            for item in cart.items:
                name = item.product.name[:20]
                qty = item.quantity
                price = f"₹{item.product.price:.2f}"
                total_p = f"₹{item.get_total_price():.2f}"
                print(f"{name:<22}{qty:<8}{price:<14}{total_p:<14}")
                
            print("=" * 60)
            print(f"{'Subtotal Amount:':<44}₹{subtotal:.2f}")
            if discount > 0:
                print(f"{'Discount (' + coupon + '):':<44}-₹{discount:.2f}")
            print(f"{'GST (18%):':<44}₹{gst:.2f}")
            print("=" * 60)
            print(f"{'GRAND TOTAL PAYABLE:':<44}₹{final_total:.2f}")
            print("=" * 60)
            print("        🎉 Thank You For Shopping With Us! 🎉")
            print("               Visit Again Soon! 👋")
            print("=" * 60 + "\n")
            # 📦 Stock update karo aur cart khali karo:
            for item in cart.items:
                inventory.reduce_stock(item.product.product_id, item.quantity)
            cart.clear_cart()
            
    elif choice == 6:
        print("Thank You For Shopping With Us!")
        break
    else:
        print("Enter a valid option (1-6)")