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

def calculate_tip(tip_percentage, bill_total): # accepts two parameters, first parameter should be a number from 0 to 1, second number should be total bill in dollars, returns a float
    return tip_percentage * bill_total # returns arguments multiplied by one another

# Walkthrough

# First test
print(calculate_tip(0.3, 100))
# When we pass in the two above arguments, they are multiplied by one another and the product is returned and is printed via the print function

#6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

def apply_discount(original_price, discount_percentage): # accepts two parameters, first parameter is original price in dollars and second is discount % as a number
    return original_price * (1 - (discount_percentage/100)) # returns float of product of original price and 1 minus the discount percentage (a number between 0 and 1)

# Walkthrough

# First test
print(apply_discount(100, 30))
# When we pass in the two above arguments, operations are performed and discounted price is returned and is printed via the print function

#7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

def handle_commas(string): # accepts one parameter (a string) and returns a string
    return string.replace(",", "") # string method replaces all commas with nothing (removes them)

# Walkthrough

# First test
print(handle_commas('100,000'))
# When we pass in the two above arguments, operations are performed and string without commas is returned and is printed via the print function

#8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(number): # accepts one parameter (an integer) and will return letter grade as a string
    if number >= 90: # if passed argument is greater or equal to 90
        return "A" # that is an A
    elif number < 90 and number >= 80: # if passed argument is 80 - 89
        return "B" # that is a B
    elif number < 80 and number >= 70: # if passed argument is 70 - 79
        return "C" # that is a C
    elif number < 70 and number >= 65: # if passed argument is 65 - 69
        return "D" # that is a D
    else: # anything else (64 or lower)
        return "F" # that is an F

# Walkthrough

# First test
print(get_letter_grade(90))
# When we pass in the above argument, operations are performed and string for the letter grade is returned and is printed via the print function

# Second test
print(get_letter_grade(80))
# When we pass in the above argument, operations are performed and string for the letter grade is returned and is printed via the print function

# Third test
print(get_letter_grade(70))
# When we pass in the above argument, operations are performed and string for the letter grade is returned and is printed via the print function

# Fourth test
print(get_letter_grade(65))
# When we pass in the above argument, operations are performed and string for the letter grade is returned and is printed via the print function

# Fifth test
print(get_letter_grade(64))
# When we pass in the above argument, operations are performed and string for the letter grade is returned and is printed via the print function

#9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# strings are immutable
# therefore, you cannot edit the current string, but must create a new, empty string and add to it

def remove_vowels(string): #accepts on parameter (a string) and outputs a string
    new_string = str() # must create a new empty string to hold consonants from passed argument
    for letter in string: # start a for loop to iterate through passed string argument
        if is_consonant(letter) == True: # check if each letter is a consonant
            new_string += letter # if letter is a consonant, add to new string
    return new_string # return new string

# Walkthrough

# First test
print(remove_vowels("Adam"))
# When we pass in the above argument, operations are performed and string without vowels is returned and is printed via the print function

# Second test
print(remove_vowels("fffffff"))
# When we pass in the above argument, operations are performed and string without vowels (same as imput since no vowels present) is returned and is printed via the print function

# Third test
print(remove_vowels("aeiou"))
# When we pass in the above argument, operations are performed and string without vowels is returned (no output since all letters are vowels) and is printed via the print function

#10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# - anything that is not a valid python identifier should be removed
# - leading and trailing whitespace should be removed
# - everything should be lowercase
# - spaces should be replaced with underscores
# - for example:
#  - Name will become name
#  - First Name will become first_name
#  - % Completed will become completed

def normalize_name(name): #receives a string and returns a string
    name = name.strip().lower().replace(" ", "_") #strips all pre and appending white space, replaces all spaces with underscores, lower() is actually not needed for identifier but was specified in question
    id = str() #creates an empty string for new string to return
    for char in name: #for loop to check each character and make sure it is valide identifier
        if char.isidentifier():
            id += char #if valid, it is added to new string
    while id[0].isnumeric(): #while loop used to eliminate numbers at front since not allowed
        id = id[1:]
    return id #returns string of final valid identifier
# EDGE CASE if someone enters a string of all numeric characters, this will not work since the while loop will have a string index out of range

# Walkthrough

# Tests
print(normalize_name('9546465hello')) # removed prepended numeric characters
print(normalize_name('Name')) # lower cased 
print(normalize_name('First Name')) # added underscores to replace spaces
print(normalize_name('% Completed')) # eliminated invalid characters
print(normalize_name('_hello')) # allowed identifier to start with underscore
print(normalize_name('1 2 3 $()&^$( T#%^H#%^i%^s%^ i%^&S %&(*(a v$%&AlI#%^d p#%^YTh#%^on id#%^%&en$%&TI#$^%%$&^*Fi@$%^*(er  #^#^#@')) # returned a valid identifier

# depending on the order of performing operations on the imputed string, the final valid identifier could be different

#11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# - cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# - cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumulative_sum(some_list): # accepts one parameter (a list) and returns a list
    cum_sum = 0 # create and set accumulator to 0
    new_list = [] # create a new list to hold new values
    for number in some_list: # start for loop to iterate through passed argument (list)
        cum_sum += number # add each element to total as you go through for loop
        new_list.append(cum_sum) # append current value to new list each time through the loop
    return new_list # return final list

# Walkthrough

# First Test
cumulative_sum([1,2,3,4])
# When we pass in the above argument, operations are performed and new list is returned and is printed via the print function

