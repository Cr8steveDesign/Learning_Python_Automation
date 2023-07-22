# Variables are declared without type

name = 'Stephen'
age = 55

#Receiving input
# print('What is your name?')
#full_name = input("Tell me your name")

# print(full_name)


# Multi-line strings done with three ''' Enter text here in multiline'''

multiLine = '''
Hello World!

Welcome to learning python!
'''

print(multiLine)

#Formatted Strings 

first_name = "Stephen"
last_name = "Omoregie"
skills = "Graphic Designer and Software Engineer"

details = f"Name: {first_name} {last_name}, Skills: {skills} "

print(details)

#String Functions 
# Getting the length of a string: len(var)
length_details = len(details)

print(length_details)


#Some String Methods
#Intellisence can actually suggest for you by appending the . before a given type


#Arithmetic Operations 
# For divisions / returns the whole including the decimal 
# To get the exact number of time a number divides another // 
# The Modulus % gives the remainder of division 

# Enhanced (compound) assignment operators 
# x += 10       y -= 2      z *= 4      w **=2

#Operator Precedence - Nearly BODMAS - PEMDAS
#Parentheses Exponentiation Multiplication Division Addition Subtraction


# You can slice a variable within the print statement
print(skills[:8])

