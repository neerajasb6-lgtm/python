
import math
import random
import datetime
import statistics
import os
import string
import calendar
import datetime

# Math package
num = 16
print("\n Number=",num)
print("Square root:", math.sqrt(num))

# Random package
print("\n Random number between 1 to 10:", random.randint(1, 10))

# Date and time package
today = datetime.datetime.now()
print("\n Today's date:", today.date())

# Statistics package
numbers = [10, 20, 30, 40, 50]
print("\n Numbers: 10,20,30,40,50")
print("Average:", statistics.mean(numbers))

# OS package
print("\n Current folder:", os.getcwd())

# String package
print("\n Letters:", string.ascii_lowercase)

#Calendar
today = datetime.date.today()
year = today.year
month = today.month
print("Current Month Calendar:")
print(calendar.month(year, month))


