# 📦 Inventory Management System

A console-based **Inventory Management System** built with Python to manage products, suppliers, stock levels, and inventory transactions using local JSON files.

This is **Project 04** in the **Python Mastery Projects** roadmap.

The project focuses on **Object-Oriented Programming, CRUD operations, stock management, business logic, data persistence, validation, and reporting**.

---

## 📖 About the Project

The Inventory Management System simulates a small inventory operation where users can manage products and suppliers, track stock entering and leaving the inventory, identify low-stock products, and generate basic inventory reports.

The application runs completely locally and uses JSON files for data storage.

There are no APIs, servers, or external databases.

The project intentionally uses a small amount of data, around **5–10 products and suppliers**, so the focus remains on understanding the software rather than handling large-scale data.

---

# 🎯 Project Objectives

The main goal is to learn how to design and build a software system that manages changing data and applies real-world business rules.

By completing this project, you will learn how to:

* Design applications using OOP
* Manage products and suppliers
* Track inventory quantities
* Handle stock-in and stock-out operations
* Apply business rules
* Validate inventory operations
* Maintain data consistency
* Store persistent data using JSON
* Generate inventory reports
* Write modular and maintainable Python code

---

# ✨ Features

## 📦 Product Management

* Add Product
* View Products
* Search Product
* Update Product
* Delete Product

Each product can contain information such as:

* Product ID
* Product Name
* Category
* Price
* Quantity
* Supplier ID
* Minimum Stock Level

---

## 🏢 Supplier Management

* Add Supplier
* View Suppliers
* Search Supplier
* Update Supplier
* Delete Supplier

---

## 📥 Stock Management

### Stock IN

Add products to inventory.

Example:

```text
Current Stock: 20
Stock IN: 10

New Stock: 30
```

### Stock OUT

Remove products from inventory.

Example:

```text
Current Stock: 30
Stock OUT: 5

New Stock: 25
```

The system must prevent stock from becoming negative.

---

## ⚠️ Low Stock Detection

The system checks whether a product has fallen below its minimum stock level.

Example:

```text
Product: Keyboard
Current Stock: 3
Minimum Stock: 5

⚠️ LOW STOCK
```

---

# 📊 Inventory Reports

The system will provide reports such as:

* Total Products
* Total Stock
* Low-Stock Products
* Total Inventory Value
* Product Summary
* Stock Transaction Summary

---

# 🔄 Application Workflow

```text
                    User
                      │
                      ▼
                  Main Menu
                      │
          ┌───────────┼───────────┐
          │           │           │
          ▼           ▼           ▼
       Product     Supplier    Inventory
       Manager      Manager     Manager
          │           │           │
          └───────────┼───────────┘
                      │
                      ▼
                 JSON Storage
                      │
                      ▼
                   Reports
```

---

# 🧩 Data Relationships

The basic relationship is:

```text
Supplier
    │
    │ supplies
    ▼
Product
    │
    │ contains
    ▼
Stock
```

Inventory changes are recorded as transactions:

```text
Product
   │
   ├── Stock IN
   │
   └── Stock OUT
```

---

# 📂 Project Structure

```text
04-Inventory-Management/
│
├── data/
│   ├── products.json
│   ├── suppliers.json
│   └── transactions.json
│
├── logs/
│
├── tests/
│
├── product.py
├── supplier.py
├── inventory_transaction.py
├── inventory.py
├── config.py
├── logger.py
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 🛠 Technologies Used

* Python 3.x
* JSON
* Object-Oriented Programming
* Python Standard Library

No external API, server, or database is required.

---

# 📚 Python Concepts Covered

This project reinforces:

* Classes and Objects
* Constructors (`__init__`)
* Methods
* Lists
* Dictionaries
* Modules
* Type Hints
* File Handling
* JSON Serialization
* Exception Handling
* Logging
* Testing

---

# 🧠 Software Engineering Concepts

The project introduces and reinforces:

* Separation of Concerns
* Single Responsibility Principle
* Object Relationships
* Business Logic
* Data Validation
* State Management
* Data Integrity
* CRUD Operations
* Modular Programming
* Clean Code
* Basic Reporting

---

# 🚀 Development Roadmap

The project was built in this order:

1. Project Setup
2. Product
3. Supplier
4. Inventory Transaction
5. Inventory Manager
6. JSON Storage
7. Product CRUD
8. Supplier CRUD
9. Stock IN
10. Stock OUT
11. Low Stock
12. Reports
13. Main Menu
14. Exception Handling
15. Logging
16. Testing
17. Refactoring
18. Final Audit

### Phase 1 — Project Setup

* [ ] Create project structure
* [ ] Configure JSON files
* [ ] Configure project settings

### Phase 2 — Product

* [ ] Product class
* [ ] Product attributes
* [ ] Product display
* [ ] Product serialization

### Phase 3 — Supplier

* [ ] Supplier class
* [ ] Supplier management
* [ ] Supplier serialization

### Phase 4 — Inventory Transactions

* [ ] Inventory transaction class
* [ ] Stock IN
* [ ] Stock OUT
* [ ] Transaction records

### Phase 5 — Inventory Manager

* [ ] Inventory class
* [ ] Product management
* [ ] Supplier management
* [ ] Inventory operations

### Phase 6 — Data Persistence

* [ ] Save products
* [ ] Load products
* [ ] Save suppliers
* [ ] Load suppliers
* [ ] Save transactions
* [ ] Load transactions

### Phase 7 — Inventory Operations

* [ ] Add stock
* [ ] Remove stock
* [ ] Prevent negative stock
* [ ] Low-stock detection

### Phase 8 — Reports

* [ ] Total products
* [ ] Total stock
* [ ] Inventory value
* [ ] Low-stock report
* [ ] Transaction report

### Phase 9 — Quality

* [ ] Exception handling
* [ ] Logging
* [ ] Testing
* [ ] Code review
* [ ] Final project audit

---

# ▶️ How to Run

Make sure Python 3.x is installed.

From the project directory:

```bash
python main.py
```

The application will start with the main inventory menu.

---

# 💾 Data Storage

All project data is stored locally using JSON.

```text
data/
│
├── products.json
├── suppliers.json
└── transactions.json
```

The project uses a small dataset for learning purposes.

Example:

```text
Products: 5–10
Suppliers: 5–10
Transactions: 5–10
```

---

# 🔐 Business Rules

The system should enforce important inventory rules.

### Stock cannot be negative

```text
Current Stock = 5
Stock OUT = 8

❌ Operation rejected
```

### Low-stock detection

```text
Quantity <= Minimum Stock Level
        ↓
⚠️ Low Stock
```

### Product IDs must be unique

```text
Product ID: 101

❌ Product ID already exists
```

### Supplier must exist

A product should not reference a supplier that does not exist.

---

# 📈 Python Mastery Project Progress

```text
Python Basics
      │
      ▼
Project 01
📚 Library Management
      │
      ▼
Project 02
🏥 Hospital Management
      │
      ▼
Project 03
🏦 Banking Management
      │
      ▼
Project 04
📦 Inventory Management
      │
      ▼
Project 05
📊 CSV Data Analyzer
```

---

# 🎓 Learning Outcomes

After completing this project, you should be able to:

* Build a medium-sized Python application
* Model real-world entities using classes
* Manage relationships between objects
* Implement CRUD operations
* Track changing application state
* Apply business rules
* Maintain data consistency
* Store structured data locally
* Build basic reports
* Test and debug Python applications
* Organize a multi-file Python project

---

# 🔮 Future Upgrades

After completing the Python version, the project can later be upgraded to technologies such as:

```text
Python
   ↓
SQL
   ↓
PostgreSQL
   ↓
FastAPI
   ↓
REST API
   ↓
React
   ↓
Docker
   ↓
Cloud Deployment
```

---

# 📌 Project Status

✅ **Complete and verified**

Verification result:

```text
25 tests passed
```

---

# 👨‍💻 Author

**Shrinivas Mudabe**

Part of the **Python Mastery Projects** roadmap — a hands-on journey focused on building real-world software while developing strong programming and software engineering fundamentals.
