##### CONTROL STRUCTURES EXERCISES #####

#1. Conditional basics
#a. prompt the user for a day of the week, print out whether the day is Monday or not

# day_of_week = input("Please enter a day of the week: ")

# if day_of_week == "Monday" or day_of_week == "Mon" or  day_of_week == "M":
#     print("Today is Monday")
# else:
#     print("Today is not Monday")

#b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend

# day_of_week = input("Please enter a day of the week: ")

# if day_of_week in ["Saturday", "Sunday"]:
#     print("It's the weekend!")
# else:
#     print(f"{day_of_week} is a weekday.")

#c. create variables and make up values for
# the number of hours worked in one week
hours_worked = 46
# the hourly rate
hourly_rate = 25
# how much the week's paycheck will be
paycheck = 0
# write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

if hours_worked <= 40:
    paycheck = hours_worked * hourly_rate
else:
    paycheck = (hours_worked * hourly_rate) * 1.5

# print(paycheck)


#2. Loop Basics
# This is where I will practice for and while loops