#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

print(fruits)
print(numbers)


# In[4]:


# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)
    
print(numbers_plus_one)


# In[5]:


# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

print(numbers_plus_one)


# In[7]:


# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())
    
print(output)


# In[9]:


# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]
uppercased_fruits = [fruit.upper() for fruit in fruits]

print(uppercased_fruits)


# In[10]:


# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
capitalized_fruits = [fruit.capitalize() for fruit in fruits]

print(capitalized_fruits)


# In[13]:


# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.
fruits_with_more_than_two_vowels = [fruit for fruit in fruits if [fruit, len([x for x in fruit if x in 'aeiouAEIOU'])][1] >= 2]
print(fruits_with_more_than_two_vowels)
# Not sure I completely understand what the nested list comprehension is doing here


# In[15]:


# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']
fruits_with_only_two_vowels = [fruit for fruit in fruits if [fruit, len([x for x in fruit if x in 'aeiouAEIOU'])][1] == 2]
print(fruits_with_only_two_vowels)
# Not sure I completely understand what the nested list comprehension is doing here


# In[16]:


# Exercise 5 - make a list that contains each fruit with more than 5 characters
more_than_five_characters = [fruit for fruit in fruits if len(fruit) > 5]
print(more_than_five_characters)


# In[17]:


# Exercise 6 - make a list that contains each fruit with exactly 5 characters
exactly_five_characters = [fruit for fruit in fruits if len(fruit) == 5]
print(exactly_five_characters)


# In[18]:


# Exercise 7 - Make a list that contains fruits that have less than 5 characters
less_than_five_characters = [fruit for fruit in fruits if len(fruit) < 5]
print(less_than_five_characters)


# In[19]:


# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
number_of_characters = [len(fruit) for fruit in fruits]
print(number_of_characters)


# In[20]:


# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
fruits_with_letter_a = [fruit for fruit in fruits if 'a' in fruit]
print(fruits_with_letter_a)


# In[21]:


# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)


# In[22]:


# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
odd_numbers = [number for number in numbers if number % 2 != 0]
print(odd_numbers)


# In[23]:


# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
positive_numbers = [number for number in numbers if number > 0]
print(positive_numbers)


# In[24]:


# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
negative_numbers = [number for number in numbers if number < 0]
print(negative_numbers)


# In[29]:


# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
two_or_more_numerals = [number for number in numbers if len(str(number).replace("-", "")) >= 2]
print(two_or_more_numerals)
# this works but I feel like I could find a better way to do this one


# In[30]:


# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]
numbers_squared = [number**2 for number in numbers]
print(numbers_squared)


# In[31]:


# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
odd_negative_numbers = [number for number in numbers if number % 2 != 0 and number < 0]
print(odd_negative_numbers)


# In[32]:


# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 
numbers_plus_5 = [number + 5 for number in numbers]
print(numbers_plus_5)


# In[44]:


# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.
def test_prime(n):
    if (n < 0):
        return False
    elif (n == 1):
        return False
    elif (n == 2):
        return True
    else:
        for x in range(2,n):
            if (n % x == 0):
                return False
        return True             

primes = [number for number in numbers if test_prime(number) == True]
print(primes)


# In[ ]:




