📘 GradeBook Analyzer

A Python CLI application that helps teachers/students analyze class performance using statistical functions, grade assignment, pass/fail classification, and CSV import/export features.

✨ Features

Manual entry of students & marks

CSV file import (supports pandas & standard csv module)

Statistical analysis

Mean (average)

Median

Highest & lowest score

Automatic grade assignment (A–F) based on score ranges

Grade distribution summary

Pass/Fail classification using list comprehensions

Formatted tabular output

Optional export of results to CSV

Interactive CLI menu loop to repeat analysis without restarting the program

📂 Project Structure
gradebook_analyzer/
│
├── gradebook.py
├── students.csv        (sample input file)
└── README.md

📝 Requirements

Python 3.8+

Optional: pandas (pip install pandas)

The script automatically falls back to the built-in csv module if pandas is not installed.

🚀 How to Run
1. Clone the project
git clone <your-repo-url>
cd gradebook_analyzer

2. Run the application
python gradebook.py

🖥️ Menu Preview (Screenshot Placeholder)

Insert your screenshot here

Welcome to GradeBook Analyzer

Menu:
  1) Manual entry of students & marks
  2) Load from CSV file
  3) Exit
Choose option (1/2/3):

📥 Input Options
Option 1 → Manual Entry

Enter names and scores. Leave name blank to finish.

Example:

Student name: Alice
Score for Alice: 78
Student name: Bob
Score for Bob: 92
Student name:

Option 2 → CSV Import

You can load a CSV file with the format:

Sample students.csv
Name,Marks
Alice,78
Bob,92
Charlie,65
Deepa,55
Ethan,34
Farah,88


Insert screenshot of CSV import output

📊 Example Output Table
Name                Marks     Grade
----------------------------------------
Bob                 92        A
Farah               88        B
Alice               78        C
Charlie             65        D
Deepa               55        F
Ethan               34        F
----------------------------------------

📈 Analysis Summary Example

Insert screenshot here

=== Analysis Summary ===
Total students : 6
Average (mean) : 68.67
Median         : 69.50
Max score      : 92  (Bob)
Min score      : 34  (Ethan)

🎓 Grade Distribution Example
Grade distribution:
  A : 1
  B : 1
  C : 1
  D : 1
  F : 2

✔️ Pass/Fail Classification

Implemented using list comprehensions.

Example:

Passed (4): Bob, Farah, Alice, Charlie
Failed (2): Deepa, Ethan

📤 Export to CSV

After generating results, the script asks:

Export final table to CSV? (y/n):


If yes, it creates:

grade_report.csv

🧪 Testing Requirements

As required in the assignment:

✔️ Test manually with at least 5 students

✔️ Test using at least 1 CSV file

✔️ Verify stats, grades, pass/fail, and exported CSV

📚 Assignment Coverage

This project satisfies all required tasks:

Task	Description	Status
1	Interactive menu	✅ Completed
2	Manual & CSV input	✅ Completed
3	Statistical functions	✅ Completed
4	Grade assignment & distribution	✅ Completed
5	Pass/Fail using list comprehension	✅ Completed
6	Formatted table + loop + CSV export	✅ Completed

Add the following screenshots before submitting:

Menu interface

Manual entry example

CSV import example

Analysis summary

Grade table

Exported CSV opened in Excel/Sheets

🧑‍💻 Author

AMAAN AHMED
GradeBook Analyzer – Python CLI Project
Created for Lab Assignment 2