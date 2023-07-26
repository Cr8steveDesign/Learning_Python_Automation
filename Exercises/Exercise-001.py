
# PROJECT OO1

"""Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers."""

user_entry = input("Enter your values here: ")
new_list = list()
new_tuple = tuple()

old_list = user_entry.split(',')

for num in old_list:
    new_list.append(num.lstrip())
    
    # Use the tuple creation function to create a
    # tuple for the variable
    new_tuple = tuple(new_list)
       
print(new_list)
print(new_tuple)
# print(user_entry)
# print(new_tuple)



