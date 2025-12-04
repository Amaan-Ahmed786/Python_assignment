#!/usr/bin/env python3
"""
GradeBook Analyzer - gradebook.py
Name: Amaan Ahmed
Assignment: Mini Project - GradeBook Analyzer
"""

import csv
import sys
from statistics import median as stat_median

# -----------------------
# Helper / Core Functions
# -----------------------
def read_csv_to_dict(filename):
    """Reads a CSV with two columns: name,marks (marks numeric). Returns dict."""
    marks = {}
    try:
        with open(filename, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if not row:
                    continue
                # allow rows with name,marks or name, marks, ...
                name = row[0].strip()
                # attempt to find numeric in subsequent columns
                mark = None
                for cell in row[1:]:
                    cell = cell.strip()
                    if cell == '':
                        continue
                    try:
                        mark = float(cell)
                        break
                    except ValueError:
                        continue
                if name and mark is not None:
                    marks[name] = float(mark)
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except Exception as e:
        print("Error reading CSV:", e)
    return marks

def manual_input_marks():
    """Prompt user to manually enter names and marks, returns dict"""
    marks = {}
    print("Manual entry mode. Enter student data. Leave name blank to finish.")
    while True:
        name = input("Student name (blank to stop): ").strip()
        if name == "":
            break
        mark_raw = input(f"Mark for {name}: ").strip()
        try:
            mark = float(mark_raw)
        except ValueError:
            print("Invalid mark. Please enter a numeric value.")
            continue
        marks[name] = mark
    return marks

def calculate_average(marks_dict):
    if not marks_dict:
        return 0.0
    return sum(marks_dict.values()) / len(marks_dict)

def calculate_median(marks_dict):
    if not marks_dict:
        return 0.0
    return stat_median(list(marks_dict.values()))

def find_max_score(marks_dict):
    if not marks_dict:
        return None, None
    name = max(marks_dict, key=lambda k: marks_dict[k])
    return name, marks_dict[name]

def find_min_score(marks_dict):
    if not marks_dict:
        return None, None
    name = min(marks_dict, key=lambda k: marks_dict[k])
    return name, marks_dict[name]

def assign_grades(marks_dict):
    grades = {}
    distribution = {"A":0,"B":0,"C":0,"D":0,"F":0}
    for name, score in marks_dict.items():
        if score >= 90:
            g = "A"
        elif score >= 80:
            g = "B"
        elif score >= 70:
            g = "C"
        elif score >= 60:
            g = "D"
        else:
            g = "F"
        grades[name] = g
        distribution[g] += 1
    return grades, distribution

def pass_fail_lists(marks_dict, pass_threshold=40):
    passed = [n for n,s in marks_dict.items() if s >= pass_threshold]
    failed = [n for n,s in marks_dict.items() if s < pass_threshold]
    return passed, failed

def print_results_table(marks_dict, grades_dict):
    # Determine column widths
    name_w = max([len(name) for name in marks_dict.keys()] + [4])
    marks_w = 6
    grade_w = 5
    header = f"{'Name':<{name_w}}  {'Marks':>{marks_w}}  {'Grade':^{grade_w}}"
    print("\n" + header)
    print("-" * (name_w + marks_w + grade_w + 4))
    for name, mark in marks_dict.items():
        grade = grades_dict.get(name, "")
        print(f"{name:<{name_w}}  {mark:>{marks_w}.2f}  {grade:^{grade_w}}")
    print()

def export_to_csv(filename, marks_dict, grades_dict):
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Marks", "Grade"])
            for name, mark in marks_dict.items():
                writer.writerow([name, f"{mark:.2f}", grades_dict.get(name, "")])
        print(f"Exported results to {filename}")
    except Exception as e:
        print("Failed to export CSV:", e)

# -----------------------
# CLI / Main Program
# -----------------------
def run_analysis(marks):
    if not marks:
        print("No marks to analyze.")
        return

    avg = calculate_average(marks)
    med = calculate_median(marks)
    max_name, max_score = find_max_score(marks)
    min_name, min_score = find_min_score(marks)
    grades, distribution = assign_grades(marks)
    passed, failed = pass_fail_lists(marks)

    # Print summary stats
    print("\n=== Analysis Summary ===")
    print(f"Students analyzed: {len(marks)}")
    print(f"Average score: {avg:.2f}")
    print(f"Median score: {med:.2f}")
    print(f"Highest: {max_name} ({max_score:.2f})")
    print(f"Lowest:  {min_name} ({min_score:.2f})")
    print("\nGrade distribution:")
    for g in ["A","B","C","D","F"]:
        print(f"  {g}: {distribution[g]}")

    print("\nPass/Fail (pass if >= 40):")
    print(f"  Passed ({len(passed)}): {', '.join(passed) if passed else 'None'}")
    print(f"  Failed ({len(failed)}): {', '.join(failed) if failed else 'None'}")

    # Table
    print_results_table(marks, grades)

    # Ask to export
    while True:
        choice = input("Export results to CSV? (y/n): ").strip().lower()
        if choice == 'y':
            outname = input("Enter output filename (e.g., results.csv): ").strip()
            if outname == "":
                outname = "results.csv"
            export_to_csv(outname, marks, grades)
            break
        elif choice == 'n' or choice == "":
            break
        else:
            print("Type 'y' or 'n'.")

def main_menu():
    print("Welcome to GradeBook Analyzer")
    while True:
        print("\nMenu:")
        print("  1) Manual entry")
        print("  2) Load CSV file")
        print("  3) Exit")
        choice = input("Choose option (1/2/3): ").strip()
        if choice == '1':
            marks = manual_input_marks()
            run_analysis(marks)
        elif choice == '2':
            fname = input("Enter CSV filename (e.g., sample_marks.csv): ").strip()
            if fname == "":
                print("No filename entered.")
                continue
            marks = read_csv_to_dict(fname)
            if not marks:
                print("No valid data loaded from CSV.")
            else:
                run_analysis(marks)
        elif choice == '3':
            print("Exiting. Goodbye.")
            sys.exit(0)
        else:
            print("Invalid option. Choose 1, 2 or 3.")

if __name__ == "__main__":
    main_menu()
