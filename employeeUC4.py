import random

# Constants
EMP_ABSENT = 0
EMP_FULL_TIME = 1
EMP_PART_TIME = 2

WAGE_PER_HOUR = 20
FULL_DAY_HOURS = 8
PART_TIME_HOURS = 4


# Function to calculate wage
def calculate_wage(hours):
    return hours * WAGE_PER_HOUR


# Random attendance
emp_check = random.randint(0,2)

if emp_check == EMP_FULL_TIME:
    emp_hours = FULL_DAY_HOURS
    print("Employee Full Time")

elif emp_check == EMP_PART_TIME:
    emp_hours = PART_TIME_HOURS
    print("Employee Part Time")

else:
    emp_hours = 0
    print("Employee Absent")


daily_wage = calculate_wage(emp_hours)

print("Employee Hours:", emp_hours)
print("Daily Wage:", daily_wage)