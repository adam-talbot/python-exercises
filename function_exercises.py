##### PYTHON FUNCTION EXERCISES #####

#1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

def is_two(incoming):
    if incoming == 2 or incoming == '2':
        return True
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
        return 
        
#5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(tip_percentage, bill_total):
    return tip_percentage * bill_total

#6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

def apply_discount(original_price, discount_percentage):
    return original_price * (1 - (discount_percentage/100))

#7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

def handle_commas(string):
    return string.replace(",", "")

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
        if is_consonant(letter) == True:
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

def normalize_name(string):
    return string.strip().lower().replace(' ', "_")


