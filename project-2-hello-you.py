# Basic Hello World Program
# Brian Snitzer
# July 5, 2019

# imports
import datetime


# Time the execution
starttime = datetime.datetime.now()
print(starttime)

# Explore strings
name = "Brian"
print(type(name))
message = 'John said to me "See you later, alligator"'
print(message)
romeo = '''Romeo said:
    My bounty is as boundless as the sea,
    My love as deep; the more I give to thee,
    The more I have, for both are infinite.'''
print(romeo)

# Main program logic here
# Ask the user's name
user_name = input('What is your name?: ')
# Ask the user's age
user_age = input('What is your age?: ')

# Ask the user's city
user_city = input('What is your city?: ')

# Ask the user what they enjoy
user_activity = input('What do you enjoy?: ')

# Create output text

output_string = "Hello {}.  You are {} years old and live in {}.  You love {}."

output_text = output_string.format(user_name,user_age,user_city,user_activity)
print(output_text)


# Calculate and print total execution time
endtime = datetime.datetime.now()
print("Execution time = ",
       starttime.microsecond - endtime.microsecond,
       "microseconds.")
