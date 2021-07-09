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

# print(movies)

total_price = 0

for movie in movies:
    price = movie['Rental Duration (days)'] * movie['Price Per Day (dollars)']
    total_price += price

print("--------------")
print(f"Total price for all movie rentals is ${total_price}.")


# another way
price_per_day = 3
little_mermaid_days = 3
brother_bear_days = 5
hercules_days = 1
days = little_mermaid_days + brother_bear_days + hercules_days
total = days * price_per_day
print(f"Total rental price is ${total}.")

print("--------------")

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

print(f"Your weekly paycheck is ${weekly_paycheck}.")

# or we can build it out more

google_pay = google_wage * google_hours
amazon_pay = amazon_wage * amazon_hours
facebook_pay = facebook_wage * facebook_hours

total_wage = google_pay + amazon_pay + facebook_pay

print(f"Total weekly pay is ${total_wage}.")

print("--------------")

#3. A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.

is_not_full = True 
no_schedule_conflict = False

can_be_enrolled = is_not_full and no_schedule_conflict

print(f"Class is not full: {is_not_full}")
print(f"There isn't a schedule conflict: {no_schedule_conflict}")
print(f"Therefore, the student can be enrolled: {can_be_enrolled}")

# both would need ot be true for student to enroll

print("--------------")

#4. A product offer can be applied only if person buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.

more_than_two = True
offer_not_expired = True
is_premium_member = False

offer_applicable = offer_not_expired and (more_than_two or is_premium_member)

print(f"More than 2 items?: {more_than_two}")
print(f"Offer still valid?: {offer_not_expired}")
print(f"Is premium member?: {is_premium_member}")
print(f"Offer is applicable?: {offer_applicable}")

print("--------------")

#5. Use the following code to follow the instructions below:

username = 'codeup'
password = 'notastrongpassword'

# Create a variable that holds a boolean value for each of the following conditions:

# - the password must be at least 5 characters

more_than_five = len(password) >= 5
print(f"Password long enough?: {more_than_five}")

# - the username must be no more than 20 characters

less_than_twenty = len(username) <= 20
print(f"Username short enough?: {less_than_twenty}")

# - the password must not be the same as the username

username_diff_password = username != password
print(f"Username and password different?: {username_diff_password}")

# - bonus neither the username or password can start or end with whitespace

# no_whitespace_start_end = username[0] != ' ' and password[0] != ' ' and username[-1] != ' ' and password[-1] != ' '
# print(no_whitespace_start_end)

# better way
username_no_spaces = username == username.strip()
print(f"Username doesn't have prepending or appending white space: {username_no_spaces}")
password_no_spaces = password == password.strip()
print(f"Password doesn't have prepending or appending white space: {password_no_spaces}")

username_valid = less_than_twenty and username_diff_password and username_no_spaces
print(f"Username is valid: {username_valid}")

password_valid = more_than_five and username_diff_password and password_no_spaces
print(f"Password is valid: {password_valid}")

credentials_valid = username_valid and password_valid
print(f"Credentials are valid: {credentials_valid}")

