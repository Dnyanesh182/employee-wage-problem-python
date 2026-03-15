import random

# Constants
EMP_ABSENT = 0
EMP_FULL_TIME = 1
EMP_PART_TIME = 2

WAGE_PER_HOUR = 20
FULL_DAY_HOURS = 8
PART_TIME_HOURS = 4
WORKING_DAYS = 20

total_monthly_wage = 0

for day in range(1, WORKING_DAYS + 1):

    emp_check = random.randint(0, 2)

    if emp_check == EMP_FULL_TIME:
        emp_hours = FULL_DAY_HOURS
    elif emp_check == EMP_PART_TIME:
        emp_hours = PART_TIME_HOURS
    else:
        emp_hours = 0

    daily_wage = emp_hours * WAGE_PER_HOUR
    total_monthly_wage += daily_wage

print("Total Monthly Wage:", total_monthly_wage)