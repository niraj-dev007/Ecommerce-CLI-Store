# 🛍️ E-Commerce Cart & Billing System (CLI)

A production-grade, modular Command Line Interface (CLI) shopping cart and billing application built with Python. Designed using Object-Oriented Programming (OOP) principles, clean separation of concerns, and defensive input validation.

---

## 🚀 Key Features

- **Inventory Management**:
  - Auto-initializes default products on first run.
  - Persists real-time stock levels into `products.json`.
  - Automatic stock reduction after checkout.
- **Smart Cart Logic**:
  - **Auto-Aggregation**: Merges duplicate item additions and updates quantities instead of creating duplicate entries.
  - **Combined Stock Guard**: Prevents adding more items than currently available in warehouse inventory.
  - **Defensive Quantity Checks**: Disallows 0 or negative quantities.
  - **Item Removal**: Allows removing individual items with instant user feedback.
- **Dynamic Billing & Invoicing**:
  - Promo/Coupon discount code system (e.g. `DISCOUNT10` for 10% off).
  - 18% GST (Tax) calculation.
  - Generates a beautifully formatted ASCII cash receipt invoice with live timestamps.
- **Modular OOP Architecture**:
  - Clean separation into Models, Inventory Manager, Cart Manager, and CLI Controller.

---

## 📁 Project Architecture

```text
E-Commerce Cart/
│
├── models.py        # Domain Entities (Product, CartItem)
├── inventory.py     # Inventory Manager (JSON Storage & Stock Management)
├── cart.py          # Cart Manager (Item Aggregation, Subtotal & Stock Guards)
├── main.py          # CLI Execution Controller & Formatted Invoice Engine
├── .gitignore       # Git ignore rules for cached and local database files
└── README.md        # Comprehensive documentation
```

---

## 🧾 Sample Invoice Output

```text
============================================================
             🧾  TAX INVOICE / CASH RECEIPT
                🛍️  APNA STORE PVT LTD
             Date: 2026-11-26 15:30:00
============================================================
Item Name              Qty     Price         Total         
------------------------------------------------------------
Laptop                 1       ₹50000.00     ₹50000.00     
Wireless Mouse         2       ₹500.00       ₹1000.00      
============================================================
Subtotal Amount:                            ₹51000.00
Discount (DISCOUNT10):                      -₹5100.00
GST (18%):                                  ₹8262.00
============================================================
GRAND TOTAL PAYABLE:                        ₹54162.00
============================================================
        🎉 Thank You For Shopping With Us! 🎉
               Visit Again Soon! 👋
============================================================
```

---

## 🛠️ How to Run

1. **Clone this repository:**
   ```bash
   git clone https://github.com/niraj-dev007/Ecommerce-CLI-Store.git
   cd Ecommerce-CLI-Store
   ```

2. **Run the store application:**
   ```bash
   python main.py
   ```

---

## 💻 Tech Stack
- **Language**: Python 3.x
- **Concepts**: Object-Oriented Programming (OOP), Data Structures (Aggregation), File I/O (JSON), Defensive Programming, Exception Handling, CLI UX Design.
