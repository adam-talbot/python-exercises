##### CONTROL STRUCTURES EXERCISES #####

#1. Conditional basics
#a. prompt the user for a day of the week, print out whether the day is Monday or not

day_of_week = input("Please enter a day of the week: ")

if day_of_week == "Monday" or day_of_week == "Mon" or  day_of_week == "M":
    print("Today is Monday")
else:
    print("Today is not Monday")

#b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend

day_of_week = input("Please enter a day of the week: ")

if day_of_week in ["Saturday", "Sunday"]:
    print("It's the weekend!")
else:
    print(f"{day_of_week} is a weekday.")

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
#a. While
# - Create an integer variable i with a value of 5.
# - Create a while loop that runs so long as i is less than or equal to 15
# - Each loop iteration, output the current value of i, then increment i by one.

i = 5
while i <= 15:
    print(i)
    i += 1

# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
i = 0
while i <= 100:
    print(i,'\n') # not sure this is exactly what they were looking for with the new line instruction (but it is the literal interpretation since the loop adds a new line automatically)
    i += 2

# Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i >= -10:
    print(i)
    i -= 5

# Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000.

i = 2
while i < 1000000:
    print(i)
    i = i ** 2

# Write a loop that uses print to create the output shown below.

i = 100
while i >= 5:
    print(i)
    i -= 5


#b. For Loops
# i. Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

number = int(input("Please enter a number: "))

for n in range(1, 11, 1):
    print(f"{number} x {n} = {number * n}")

# ii. Create a for loop that uses print to create the output shown below.

for n in range(1,10,1):
    print(str(n) * n)

#c. break and continue
# i. Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. 
# (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.

number = input("Please enter an odd number between 1 and 50: ")

while number.isdigit() == False:
    print(f"{number} isn't a number, try again.")
    number = input("Please enter an odd number between 1 and 50: ")

while int(number) < 1 or int(number) > 50 or int(number) % 2 == 0:
    if int(number) < 1:
        print(f"{number} is less than 1, please enter a number between 1 and 50: ")
    elif int(number) > 50:
        print(f"{number} is greater than 50, please enter a number between 1 and 50: ")
    else:
        print(f"{number} is not odd, please enter an odd number: ")
    number = input()

print(f"\nNumber to skip is: {number}\n")    
    
for n in range(51):
    if n % 2 == 0 or n == int(number):
        if n == int(number):
            print(f"Yikes! Skipping number: {n}")
        continue
    print(f"Here is odd number: {n}")

# need to redo this one to include a break statement
# also, this one can get very complicated in terms of the order of checking for valid responses (in above code, if they enter a response that passes the isdigit test, but doesn't pass another, and then enter one that doesn't it won't work)

# d. The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)

is_not_digit = True
while is_not_digit:
    count_to = input("Enter a positive number to count to: ")
    if count_to.isdigit():
        count_to = int(count_to) + 1
        if count_to >= 2:
            is_not_digit = False

for n in range(1, count_to):
    print(n)

#e. Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.

is_not_digit = True
while is_not_digit:
    count_from = input("Enter a positive number to countdown from: ")
    if count_from.isdigit():
        count_from = int(count_from)
        if count_from >= 1:
            is_not_digit = False

for n in range(count_from, 0, -1):
    print(n)



#3. Fizzbuzz

# One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
# - Write a program that prints the numbers from 1 to 100.
# - For multiples of three print "Fizz" instead of the number
# - For the multiples of five print "Buzz".
# - For numbers which are multiples of both three and five print "FizzBuzz".

for n in range(1, 100, 1):
    if n % 5 == 0 and n % 3 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)


#4. Display a table of powers.
# - Prompt the user to enter an integer.
# - Display a table of squares and cubes from 1 to the value entered.
# - Ask if the user wants to continue.
# - Assume that the user will enter valid data.
# - Only continue if the user agrees to.

number = int(input("What number would you like to go up to? "))
user_permission = input("Would you like to continue? ")

if user_permission == "Yes" or user_permission == "Y" or user_permission == "yes" or user_permission == "y":
    print("Here is your table!:\n")
    print("number|squared|cubed")
    print("---------------------")
          
    for n in range(1, number + 1, 1):
        if n ** 2 < 10:
            print(f"{n}     | {n ** 2}     | {n ** 3}")
        else:
            print(f"{n}     | {n ** 2}    | {n ** 3}")
        n += 1
else:
    print("No worries, participation is not mandatory.")
