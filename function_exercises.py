##### PYTHON FUNCTION EXERCISES #####

#1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

def is_two(incoming): # accepts one parameter, could be any type
    if incoming == 2 or incoming == '2': # checks to see if incoming is 2 or '2'
        return True # if meets conditions, returns True
    else:
        return False

#2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(string):
    if string.lower() in "aeiou":
        return True
    else:
        return False

#3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(string):
    if is_vowel(string) == False:
        return True
    else:
        return False

#4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

def cap_if_starts_with_con(string):
    if is_consonant(string[0]) == True:
        return string.capitalize()
    else:
        return string
        
#5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(tip_percentage, bill_total):
    return tip_percentage * bill_total

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

