import random

# Constants
EMP_ABSENT = 0
EMP_FULL_TIME = 1
EMP_PART_TIME = 2

WAGE_PER_HOUR = 20
FULL_DAY_HOURS = 8
PART_TIME_HOURS = 4

# Random employee check
emp_check = random.randint(0, 2)

match emp_check:
    case 1:
        emp_hours = FULL_DAY_HOURS
        print("Employee is Full Time")

    case 2:
        emp_hours = PART_TIME_HOURS
        print("Employee is Part Time")

    case _:
        emp_hours = 0
        print("Employee is Absent")

# Calculate wage
daily_wage = emp_hours * WAGE_PER_HOUR

print("Employee Hours:", emp_hours)
print("Daily Wage:", daily_wage)