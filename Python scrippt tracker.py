''' NAME- AMAAN AHMED
DATE- 8 NOVEMBER 2025
PROJECT TITTLE- DAILY CALORIE TRACKER CLI'''

print("WELCOME TO DAILY CALORIE TRACKER CLI - This is a simple command line interafce tool to track your daily calorie intake where you can log your meals, keep track of total calories consumed, save logs for future tracking and comapre against your own personal limit")

x=int(input("ENTER NO OF MEALS YOU WANT TO LOG TODAY: "))
meals = []
cal_amt=[]
for i in range(x):
    meal_name = input(f"ENTER NAME OF MEAL {i+1}: ")
    calories = int(input(f"ENTER CALORIES FOR {meal_name}: "))
    meals.append(meal_name)
    cal_amt.append(calories)

Total_calories = sum(cal_amt)
avg_calories = Total_calories / x
dally_limit = int(input("ENTER YOUR PERSONAL DAILY CALORIE LIMIT: "))
if Total_calories > dally_limit:
    print(f"YOU HAVE EXCEEDED YOUR DAILY CALORIE LIMIT BY {Total_calories - dally_limit} CALORIES")
else:
     print(f"YOU ARE WITHIN YOUR DAILY CALORIE LIMIT BY {dally_limit - Total_calories} CALORIES")
print("\nDAILY CALORIE INTAKE SUMMARY")
print(f"Meal Name\tCalories")
print("-" * 30)
for i in range(len(meals)):
    print(f"{meals[i]}\t\t{cal_amt[i]}")
print("-" * 30)
print(f"Total\t\t{Total_calories} ")
print(f"Average\t\t{avg_calories}")