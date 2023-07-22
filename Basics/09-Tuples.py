# A Tuple is also another data structure in Python. Unlike lists and dictionary, tuples are immutable. That is they cannot be reassigned or modified after initialization. 

# Tuples are iterable. Just like loop, they also have subscript indexing access. 


my_tuple = ( 'Joveth', 'Stephen', 'Blessing', 'Faith', 'Joy', 'Mummy', 'Stephen')

print(my_tuple)

# Using the sorted function to sort the member of the tuple. The function returns a LIST of the sorted iterable which can then be assigned to a new variable or reassigned to the original.

# The sorted function can also receive a 'reverse=True' parameter to return # a list sorted in reverse order

new_tuple = sorted(my_tuple, reverse=True)

#Accessing with indexing
print(my_tuple[0])


print(my_tuple)

print("")

#Count the number of times a value occurs in the tuple
num = my_tuple.count('Stephen')

