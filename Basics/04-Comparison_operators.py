"""
Comparisons are used to check between two conditions and it also 
returns a boolean value of either True or False. 

e.g if temperature > 30
    if name == "Stephen"
    if 1 >= 0
    if number <= 100
    if name != "Faith"
"""

#Implement the rule below
"""
If the name of the user is less than 3, prompt user that name must be more than 3. if more than 50 characters, then prompt user to use less than 50
"""

name = input("Enter your name: ")

if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Sorry, name has to be less than 50 characters")
else:
    print("Name looks good! 😎")


