#### DATA TYPES AND VARIABLES EXERCISES ####

# Write some Python code, that is, variables and operators, to describe the following scenarios. Do not worry about the real operations to get the values, 
# the goal of these exercises is to understand how real world conditions can be represented with code.

#1. You have rented some movies for your kids: 
# The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). 
# If price for a movie per day is 3 dollars, how much will you have to pay?

# create a dictionary that holds name of movie, length rented, and cost per day
movies = [
    {
        'Title' : 'The Little Mermaid',
        'Rental Duration (days)' : 3,
        'Price Per Day (dollars)' : 3
    } 
    ,  
    {   
        'Title' : 'Brother Bear',
        'Rental Duration (days)' : 5,
        'Price Per Day (dollars)' : 3
    }
    ,       
    {       
        'Title': 'Hercules',
        'Rental Duration (days)' : 1,
        'Price Per Day (dollars)' : 3            
    }
]

print(movies)

#2. Suppose you're working as a contractor for 3 companies: 
# Google, Amazon and Facebook, they pay you a different rate per hour. 
# Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? 
# You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

google_wage = 400
amazon_wage = 380
facebook_wage = 350
google_hours = 6
amazon_hours = 4
facebook_hours = 10

weekly_paycheck = (google_wage * google_hours)+(amazon_wage * amazon_hours)+(facebook_wage * facebook_hours)

print(weekly_paycheck)

#3. A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.

is_not_full = True 
no_schedule_conflict = False

can_be_enrolled = is_not_full and no_schedule_conflict

print(can_be_enrolled)

# both would need ot be true for student to enroll

#4. A product offer can be applied only if person buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.

more_than_two = True
offer_not_expired = True
is_premium_member = False

offer_applicable = offer_not_expired and (more_than_two or is_premium_member)

print(offer_applicable)

#5. Use the following code to follow the instructions below:

username = 'codeup'
password = 'notastrongpassword'

# Create a variable that holds a boolean value for each of the following conditions:

# - the password must be at least 5 characters

more_than_five = len(username) >= 5
print(more_than_five)

# - the username must be no more than 20 characters

less_than_twenty = len(username) <= 20
print(less_than_twenty)

# - the password must not be the same as the username

username_diff_password = username != password
print(username_diff_password)

#-  bonus neither the username or password can start or end with whitespace

no_whitespace_start_end = username[0] != ' ' and password[0] != ' ' and username[-1] != ' ' and password[-1] != ' '
print(no_whitespace_start_end)



