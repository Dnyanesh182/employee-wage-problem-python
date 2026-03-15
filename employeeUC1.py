import random

# Constants
IS_PRESENT = 1

# Generate random attendance
attendance = random.randint(0, 1)

if attendance == IS_PRESENT:
    print("Employee is Present")
else:
    print("Employee is Absent")