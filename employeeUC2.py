import random

# Constants
IS_PRESENT = 1
WAGE_PER_HOUR = 20
FULL_DAY_HOURS = 8

# Check attendance
attendance = random.randint(0,1)

if attendance == IS_PRESENT:
    daily_wage = WAGE_PER_HOUR * FULL_DAY_HOURS
    print("Employee Present")
    print("Daily Wage:", daily_wage)
else:
    print("Employee Absent")
    print("Daily Wage: 0")