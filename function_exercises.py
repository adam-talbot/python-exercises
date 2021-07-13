##### PYTHON FUNCTION EXERCISES #####

#1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

def is_two(incoming): # accepts one parameter, could be any type, returns a boolean
    if incoming == 2 or incoming == "2": # checks to see if incoming is 2 or '2'
        return True # if meets conditions, returns True
    else:
        return False # if doesn't meet conditions, returns False

# Walkthrough

# First test
print(is_two("2"))
# When we pass "2" into the function, the if condition will evaluate to True, so the function will return True and this will be printed via the print function

# Second test
print(is_two(2))
# When we pass 2 into the function, the if condition will evaluate to True, so the function will return True and this will be printed via the print function

# Third test
print(is_two("anything else"))
# When we pass anything else into the function, the if condition will evaluate to Falso, so the function will return False and this will be printed via the print function

#2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(string): # accepts one parameter (a string), returns a boolean
    if string.lower() in "aeiou": # makes the string that was passed in lowercase and checks if it is in the list of vowels
        return True # if it is, it returns True
    else:
        return False # if it isn't, it returns False

# Walkthrough

# First test
print(is_vowel("A"))
# When we pass "A" into the function, it will be changed to lowercase, and it will check if this string is in the list of vowels provided.
# It is in the list, so it will return True and this will be printed via the print function 

# Second test
print(is_vowel("b"))
# When we pass "b" into the function, it will check if this string is in the list of vowels provided.
# It is not in the list, so it will return False and this will be printed via the print function

#3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(string): # accepts one parameter (a string) and returns a boolean
    if is_vowel(string) == False: # checks if string passed in is not a vowel
        return True # if this is true, it returns True (since that means it must be a consonant)
    else:
        return False # if this isn't true, it returns False (since that means it is a vowel)

# Walkthrough

# First test
print(is_consonant("A"))
# When we pass "A" into the function, it will check if it is not a vowel
# It is a vowel, so it will return False and this will be printed via the print function

# Second test
print(is_consonant("b"))
# When we pass "b" into the function, it will check if it is not a vowel
# It isn't a vowel, so it will return True and this will be printed via the print function

#4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

def cap_if_starts_with_con(string): # accepts one parameter (a string), and returns a string
    if is_consonant(string[0]) == True: # checks if first letter of string that was passed in is a consonant using the is_consonant function
        return string.capitalize()  # if it is, it capitalizes the first letter of that string using the capitalize() string method 
    else:
        return string # if it is not, it returns the string in it's original form

# Walkthrough

# First test
print(cap_if_starts_with_con("hello"))
# When we pass in a word that starts with a consonant, the if condition is true and therefore the first letter of that string is capitalized
# and this new string is printed via the print function

# Second test
print(cap_if_starts_with_con("exactly"))
# When we pass in a word that starts with a vowel, the if condition is false and therefore the first letter of that string is not capitalized
# and the original string is printed via the print function
        
#5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(tip_percentage, bill_total): # accepts two parameters, first parameter should be a number from 0 to 1, second number should be total bill in dollars
    return tip_percentage * bill_total # returns arguments multiplied by one another

# Walkthrough

####

#6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

def apply_discount(original_price, discount_percentage):
    return original_price * (1 - (discount_percentage/100))

#7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

def handle_commas(string):
    return float(string.replace(",", ""))

#8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(number):
    if number >= 90:
        return "A"
    elif number < 90 and number >= 80:
        return "B"
    elif number < 80 and number >= 70:
        return "C"
    elif number < 70 and number >= 65:
        return "D"
    else:
        return "F"

#9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(string):
    new_string = str()
    for letter in string:
        if is_consonant(letter.lower()) == True:
            new_string += letter
    return new_string

#10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# - anything that is not a valid python identifier should be removed
# - leading and trailing whitespace should be removed
# - everything should be lowercase
# - spaces should be replaced with underscores
# - for example:
#  - Name will become name
#  - First Name will become first_name
#  - % Completed will become completed

def normalize_name(name): #receives a string
    name = name.strip().lower().replace(" ", "_") #strips all pre and appending white space, replaces all spaces with underscores, lower() is actually not needed for identifier but was specified in question
    id = str() #creates an empty string for new string to return
    for char in name: #for loop to check each character and make sure it is valide identifier
        if char.isidentifier():
            id += char #if valid, it is added to new string
    while id[0].isnumeric(): #while loop used to eliminate numbers at front since not allowed
        id = id[1:]
    return id #returns string of final valid identifier
#if someone enters a string of all numeric characters, this will not work since the while loop will have a string index out of range

#11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# - cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# - cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumulative_sum(some_list):
    cum_sum = 0
    new_list = []
    for number in some_list:
        cum_sum += number
        new_list.append(cum_sum)
    return new_list

