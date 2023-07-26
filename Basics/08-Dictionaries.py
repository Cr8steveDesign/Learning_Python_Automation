import re
# A dictionary in python is a data structure with key value pairs. There is no other in which the members are, unlike a List or Tuple. Its values and key members can be modified or easily created. 

# Initialized with a curly brace with members/keys entered as a string, and values separated from members with a colon :

# The dictionary can contain other data structures within itself. including a dictionary too. 

my_dictionary = {'first_name': 'Stephen',
                 'last_name': 'Omoregie',
                 #'full_name': my_dictionary['first_name']
                 'Job': 'Student',
                 'Skills': ['Graphic Design', 'Video Editing', 'Web Development',],
                 'Education': 'B.Sc Computer Science'
                 }

# Access methods: .items() .keys() .values()


#Using a loop to print key value pairs: 
print("Details of the dictionary: ")
for (key, value) in my_dictionary.items():
    print(f"{key}: {value}")
    
# adding new member after initialization 
print("")

# setting member 
my_dictionary['full_name'] = my_dictionary['first_name'] + " " + my_dictionary['last_name']

my_dictionary['Skills'].append('Software Engineering')

#Printing the items of the dictionary
print(my_dictionary['full_name'])
print(my_dictionary['Skills'])

# retrieving the value of a member
x = my_dictionary.get('hobby', '(nil)')

#Setting a member with the method
my_dictionary.setdefault('hobby', 'Learning to code')

print(x)

