from inventory import Inventory
from cart import Cart
from coupon import CouponManager
from datetime import datetime

def main():
    inventory = Inventory()
    cart = Cart()
    coupon_mgr = CouponManager()

    try:
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
                |    5. Play Quiz & win Coupon       |
                |------------------------------------|
                |    6. Checkout & Print Bill        |
                |------------------------------------|
                |    7. Exit                         |
                |====================================|
                    """)
            try:
                choice = int(input("Choose option.: ").strip())
            except ValueError:
                print("Enter only numbers!")
                continue
            
            if choice == 1:
                inventory.display_products()
                
            elif choice == 2:
                while True:
                    try:
                        p_id = int(input("Enter product ID.: ").strip())
                    except ValueError:
                        print("Enter only numbers!")
                        continue
                        
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
                coupon_mgr.play_quiz()
                        
                
            elif choice == 6:
                if len(cart.items) == 0:
                    print("Cart is empty. First few purchased items.")
                    
                else:
                    subtotal = cart.get_subtotal()
                    coupon = input("Is there a coupon code? (If not then press enter!)").strip().upper()
                    
                    discount = 0
                    if coupon in coupon_mgr.active_coupons:
                        discount = subtotal*0.10
                        print("Coupon Code has beed Applied, and you got a flat 10% Discount!")
                        coupon_mgr.active_coupons.remove(coupon)
                    
                    elif coupon == "":
                        print("No Coupon Code Found. No Discount.")
                        
                    else:
                        print(f"Coupon code ({coupon}) is invalid. No Discount!")
                        
                    gst = (subtotal - discount) * 0.18
                    final_total = (subtotal-discount)  + gst
                    
                    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    
                    while True:
                        customer_name = input("Enter Customer name: ")
                        
                        if customer_name != "":
                            break
                        print("Please Enter Customer name!")
                            
                        
                    bill_text = f"""
                {"=" * 60}
                            🧾  TAX INVOICE / CASH RECEIPT
                                🛍️  APNA STORE PVT LTD
                            Customer Name: {customer_name}
                            Date: {now}
                {"=" * 60}
                {'Item Name':<22}{'Qty':<8}{'Price':<14}{'Total':<14}
                {"-" * 60}
                """
                    for item in cart.items:
                        name = item.product.name[:20]
                        qty = item.quantity
                        price = f"₹{item.product.price:.2f}"
                        total_p = f"₹{item.get_total_price():.2f}"
                        bill_text += f"{name:<22}{qty:<8}{price:<14}{total_p:<14}\n"
                    bill_text +=f"""
                {"=" * 60}
                {'Subtotal Amount:':<44}₹{subtotal:.2f}\n"""

                    if discount > 0:
                        bill_text +=f"                {'Discount (' + coupon + '):':<44}-₹{discount:.2f}\n"

                    bill_text += f"""
                {'GST (18%):':<44}₹{gst:.2f}
                {"=" * 60}
                {'GRAND TOTAL PAYABLE:':<44}₹{final_total:.2f}
                {"=" * 60}
                        🎉 Thank You For Shopping With Us! 🎉
                                Visit Again Soon! 👋
                {"=" * 60}
                """
                    
                    print(bill_text)
                    
                    filename = f"receipt_{customer_name}_{datetime.now().strftime('%Y-%m-%d')}.txt"
                    with open(filename, "w", encoding="utf-8") as f:
                        f.write(bill_text)
                        
                    print(f"\nReceipt successfully saved as '{filename}'!")

                    for item in cart.items:
                        inventory.reduce_stock(item.product.product_id, item.quantity)
                    cart.clear_cart()
                    
            elif choice == 7:
                print("Thank You For Shopping With Us!")
                break
            else:
                print("Enter a valid option (1-7)")
                
    except KeyboardInterrupt:
        print("Thank You For Shopping With Us! See you again.")
        
if __name__=="__main__":
    main()