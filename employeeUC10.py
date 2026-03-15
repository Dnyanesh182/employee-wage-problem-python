import random


class EmployeeWage:

    EMP_ABSENT = 0
    EMP_FULL_TIME = 1
    EMP_PART_TIME = 2

    WAGE_PER_HOUR = 20
    FULL_DAY_HOURS = 8
    PART_TIME_HOURS = 4

    MAX_WORKING_DAYS = 20
    MAX_WORKING_HOURS = 100

    def __init__(self):
        self.total_emp_hours = 0
        self.total_working_days = 0

    def compute_employee_wage(self):

        while (self.total_emp_hours <= self.MAX_WORKING_HOURS and
               self.total_working_days < self.MAX_WORKING_DAYS):

            self.total_working_days += 1

            emp_check = random.randint(0, 2)

            if emp_check == self.EMP_FULL_TIME:
                emp_hours = self.FULL_DAY_HOURS
            elif emp_check == self.EMP_PART_TIME:
                emp_hours = self.PART_TIME_HOURS
            else:
                emp_hours = 0

            self.total_emp_hours += emp_hours

        total_wage = self.total_emp_hours * self.WAGE_PER_HOUR
        return total_wage


employee = EmployeeWage()

monthly_wage = employee.compute_employee_wage()

print("Total Employee Hours:", employee.total_emp_hours)
print("Monthly Wage:", monthly_wage)