import random

class CouponManager:
    def __init__(self):
        self.active_coupons = ["DISCOUNT10"]
        
    def play_quiz(self):
        a = random.randint(20, 50)
        b = random.randint(30, 40)
        c = random.randint(2, 20)
        d = random.randint(10, 30)
        e = random.randint(20, 70)
        f = random.randint(30, 100)
        g = random.randint(50, 80)
        
        template = [
            f"({a} + {b}) * {c} - ({d} * {e})",
            f"{a} * ({c} - {d}) + ({e} + {f}) * {b}",
            f"({a} * {b}) + ({c} - {d}) * ({e} + {f}) - {g}"
        ]
        problem = random.choice(template)
        correct_ans = eval(problem)
        
        print("\nSolve this to get 10% OFF")
        print(f"Question: {problem}")
        try:
            user_ans = int(input("Enter your answer --> "))
        except ValueError:
            print("Invalid Answer! Please Enter a whole number.")
            return
        
        if user_ans == correct_ans:
            print("\nCorrect Answer.")
            
            word = [
            "SAVE", "DEAL", "OFFER", "FLAT", "EXTRA", "BONUS", "CASH", "DISC", "PROMO", "COUPON",
            "SALE", "MEGA", "SUPER", "BIG", "WOW", "FLASH", "HURRY", "TODAY", "LUCKY", "SPECIAL",
            "FREE", "GIFT", "REWARD", "VIP", "PRO", "GOLD", "ELITE", "PREMIUM", "MEMBER", "LOYAL",
            "WELCOME", "HELLO", "NEW", "FIRST", "START", "JOIN", "FRESH", "FESTIVE", "SEASON", "WEEKEND",
            "MIDNIGHT", "EARLY", "FINAL", "LAST", "BEST", "TOP", "HOT", "SMART", "EASY", "THANKS",
            ]
            chosen_word = random.choice(word)
            rand_num = random.randint(1000, 9999)
            
            coupon = f"{chosen_word}{rand_num}"
            self.active_coupons.append(coupon)
            
            print(f"Your Coupon Code is {coupon}")
        else:
            print(f"\nWrong Answer! Correct answer was: {correct_ans}. Better luck next time!")