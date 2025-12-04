📌 Daily Calorie Tracker — Python CLI Application

A simple and beginner-friendly Python Command Line Interface (CLI) tool that allows users to track their daily calorie intake by entering meals, calculating totals, comparing with a daily limit, and optionally saving the session in a text file.

This project is created as part of the Programming for Problem Solving using Python course mini-project.

📖 Table of Contents

Overview

Features

Project Structure

How the Program Works

Technologies Used

How to Run the Program

Sample Workflow

Screenshots

Bonus Feature

Academic Integrity

Author

📌 Overview

Maintaining daily food and calorie logs is essential for a healthy lifestyle, yet most students struggle with complex mobile apps or forget to track their meals entirely.
This project solves that problem by providing a simple, offline, and easy-to-use Python CLI tool that records meals and calorie amounts, calculates totals and averages, checks if the user exceeds their daily limit, and shows a neat summary.

This makes it a helpful tool for students, beginners, and anyone learning basic Python concepts such as:
✔ Input handling
✔ Lists
✔ Loops
✔ Conditionals
✔ Arithmetic operations
✔ f-string formatting
✔ File handling

✨ Features

Add multiple meals with calorie values

Stores meal names and calorie amounts in lists

Calculates:

Total calorie intake

Average calories per meal

Compares intake with a user-defined daily limit

Displays a clean summary table

Warning system if the user exceeds the limit

Bonus: Save the entire session to a text file (calorie_log.txt)

Beginner-friendly and works fully offline

📁 Project Structure
daily_calorie_tracker/
│── tracker.py             # Main Python program
│── calorie_log.txt        # Saved session output (optional)
│── README.md              # Project documentation
│── sample_runs/           # Screenshots for report
│     ├── run1.png
│     ├── run2.png
│     └── run3.png

⚙️ How the Program Works

User enters the number of meals they want to log

For each meal:

Enter meal name

Enter calorie value

Program calculates:

Total calories

Average calories per meal

User enters a daily calorie limit

Program compares total intake vs. limit

Displays formatted table of results

Asks the user if they want to save the session as a log file

🧰 Technologies Used

Python 3.x

Basic Python modules (no external libraries)

Concepts Used:

Input/output handling

Lists and loops

Type conversion (int / float)

Conditional statements

Arithmetic operations

f-string formatting

File handling (open, write)

▶️ How to Run the Program

Install Python 3.x

Open a terminal or command prompt

Navigate to the project folder

Run the script using:

python tracker.py

🔄 Sample Workflow

Example flow:

Enter the number of meals: 3
Meal 1 name: Breakfast
Calories for Breakfast: 350

Meal 2 name: Lunch
Calories for Lunch: 600

Meal 3 name: Snack
Calories for Snack: 150

Enter your daily calorie limit: 1200

----- Summary -----
Meal Name       Calories
Breakfast       350
Lunch           600
Snack           150
--------------------------------
Total:          1100
Average:        366.67

Status: Within limit ✔️

🖼 Screenshots

Add your outputs here:

Sample Run 1
[Insert screenshot]

Sample Run 2
[Insert screenshot]

Sample Run 3
[Insert screenshot]

💾 Bonus Feature

If the user chooses to save the session, a file named calorie_log.txt is generated containing:

Timestamp

Meals and calories

Total & average

Limit comparison message

This introduces basic file I/O operations in Python and makes the tool more practical.

📜 Academic Integrity

This project is created for educational purposes as part of the Programming for Problem Solving using Python course.

All code is written individually by the student.
External sources such as tutorials or documentation, if used for understanding concepts, are not copied directly and are credited appropriately.

👤 Author

Name: Amaan Ahmed
Roll Number: 2501730305
Course: Programming for Problem Solving using Python
University: K.R. Mangalam University