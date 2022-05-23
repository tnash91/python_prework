# Question 1:
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
# The first line of the code has been defined as below.
def hello_name(user_name):
    print(f"\nHello_{user_name}!")
        
user_name = ("Trent") 
hello_name(user_name)

# Question 2:
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds(odds):
    """function that prints odds and returns nothing"""
    odds = list(range(1,101,2))
    print(odds)
print(first_odds(f"odds"))

# Question 3:
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
def max_num_in_list(digits):
     """Return the max number of given list"""
     digits = (1,2,3,4)
     return max(digits)

print(max_num_in_list(f"digits"))

# Question 4:
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_leap_year(a_year):
    """Return true/false if the given year is/is not a leap year"""
    if a_year % 4 == 0:
       return True
    elif a_year % 400 == 0:
        return True
    else:
       return False
print(is_leap_year(2024))

# Question 5:
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
def is_consecutive(a_list):
    """Function that sees if all numbers are consecutive"""
    if a_list [x += 1]
        input("Please provide a list of numbers and I will tell you if it's consecutive or not ")
        range(len(a_list))
        return True
    else:
        return False
print(is_consecutive)
