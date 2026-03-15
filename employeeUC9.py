import random

# Constants
EMP_ABSENT = 0
EMP_FULL_TIME = 1
EMP_PART_TIME = 2

WAGE_PER_HOUR = 20
FULL_DAY_HOURS = 8
PART_TIME_HOURS = 4

MAX_WORKING_DAYS = 20
MAX_WORKING_HOURS = 100

total_emp_hours = 0
total_working_days = 0

daily_wage_dict = {}

while total_emp_hours <= MAX_WORKING_HOURS and total_working_days < MAX_WORKING_DAYS:

    total_working_days += 1

    emp_check = random.randint(0,2)

    if emp_check == EMP_FULL_TIME:
        emp_hours = FULL_DAY_HOURS
    elif emp_check == EMP_PART_TIME:
        emp_hours = PART_TIME_HOURS
    else:
        emp_hours = 0

    total_emp_hours += emp_hours

    daily_wage = emp_hours * WAGE_PER_HOUR

    daily_wage_dict[total_working_days] = daily_wage

total_wage = total_emp_hours * WAGE_PER_HOUR

print("Daily Wage Dictionary:", daily_wage_dict)
print("Total Wage:", total_wage)