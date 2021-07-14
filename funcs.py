# 1
def is_two(incoming): # accepts one parameter, could be any type, returns a boolean
    if incoming == 2 or incoming == "2": # checks to see if incoming is 2 or '2'
        return True # if meets conditions, returns True
    else:
        return False # if doesn't meet conditions, returns False

# 2
def is_vowel(string): # accepts one parameter (a string), returns a boolean
    if string.lower() in "aeiou": # makes the string that was passed in lowercase and checks if it is in the list of vowels
        return True # if it is, it returns True
    else:
        return False # if it isn't, it returns False

# 3
def is_consonant(string): # accepts one parameter (a string) and returns a boolean
    if is_vowel(string) == False: # checks if string passed in is not a vowel
        return True # if this is true, it returns True (since that means it must be a consonant)
    else:
        return False # if this isn't true, it returns False (since that means it is a vowel)

# 4
def cap_if_starts_with_con(string): # accepts one parameter (a string), and returns a string
    if is_consonant(string[0]) == True: # checks if first letter of string that was passed in is a consonant using the is_consonant function
        return string.capitalize()  # if it is, it capitalizes the first letter of that string using the capitalize() string method 
    else:
        return string # if it is not, it returns the string in it's original form

# 5
def calculate_tip(tip_percentage, bill_total): # accepts two parameters, first parameter should be a number from 0 to 1, second number should be total bill in dollars, returns a float
    return tip_percentage * bill_total # returns arguments multiplied by one another

# 6
def apply_discount(original_price, discount_percentage): # accepts two parameters, first parameter is original price in dollars and second is discount % as a number
    return original_price * (1 - (discount_percentage/100)) # returns float of product of original price and 1 minus the discount percentage (a number between 0 and 1)

# 7
def handle_commas(string): # accepts one parameter (a string) and returns a string
    return string.replace(",", "") # string method replaces all commas with nothing (removes them)

# 8
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

# 9
def remove_vowels(string): #accepts on parameter (a string) and outputs a string
    new_string = str() # must create a new empty string to hold consonants from passed argument
    for letter in string: # start a for loop to iterate through passed string argument
        if is_consonant(letter) == True: # check if each letter is a consonant
            new_string += letter # if letter is a consonant, add to new string
    return new_string # return new string

# 10 
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

# 11
def cumulative_sum(some_list): # accepts one parameter (a list) and returns a list
    cum_sum = 0 # create and set accumulator to 0
    new_list = [] # create a new list to hold new values
    for number in some_list: # start for loop to iterate through passed argument (list)
        cum_sum += number # add each element to total as you go through for loop
        new_list.append(cum_sum) # append current value to new list each time through the loop
    return new_list # return final list