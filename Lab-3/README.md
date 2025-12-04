# 📚 Library Inventory Management System (Python Assignment)

This project is a simple **Library Inventory Management System** built using **Object-Oriented Programming (OOP)** in Python.  
It allows users to **add**, **issue**, **return**, and **search** books through a **Command Line Interface (CLI)**.

All book data is saved in a `books.json` file for persistent storage.

---

## 🔥 Features

### ✅ Book Management  
- Add new books  
- Store title, author, ISBN, and status (available/issued)

### ✅ Issue & Return Books  
- Mark a book as issued  
- Mark a book as returned  
- Prevent issuing an already-issued book

### ✅ Search Features  
- Search by **title**  
- Search by **ISBN**

### ✅ JSON Storage  
- Books are stored in `books.json`  
- Automatically created if it doesn’t exist

### ✅ Logging + Error Handling  
- Logs all operations  
- Handles missing files, invalid input, duplicate ISBN, etc.

### ✅ Clean Folder Structure  
project_folder/
│
├── library_manager/
│ ├── init.py
│ ├── book.py
│ └── inventory.py
│
├── cli/
│ └── main.py
│
└── books.json (auto-created)

---

## 🧱 Technologies Used

- Python 3  
- OOP Principles  
- JSON (data storage)  
- Logging module  
- Pathlib (file handling)

---

# 🚀 How to Run the Project

## 1️⃣ Open Terminal / CMD  
Navigate to your project folder:

cd path/to/your/project_folder


Example:

cd "C:\Users\ACER\OneDrive\Desktop\Python_assignment\library-inventory-manager-amaan"


---

## 2️⃣ Run the CLI Program

Use this command:

python -m cli.main



=== LIBRARY INVENTORY CLI ===

Add Book

Issue Book

Return Book

View All Books

Search by Title

Search by ISBN

Exit


Follow the menu options to use the system.

---

# 📝 What is ISBN?

**ISBN (International Standard Book Number)** is a **unique identifier for each book**.  
It helps the system identify a specific book when issuing, returning, or searching.

Example ISBNs:

12345
567876543



In this assignment, **you can use any unique number as ISBN**.

---

# 📂 books.json File

`books.json` is created automatically after adding your first book.

Example content:

```json
[
  {
    "title": "Harry Potter",
    "author": "J.K. Rowling",
    "isbn": "123",
    "status": "available"
  }
]

