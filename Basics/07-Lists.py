# Introduction to Lists in Python 

# Lists constants are surrounded by square brackets and the elements in the list are separated by commas. 

#A List element can be any Python object - even another list. A list can equally be empty

# Lists are mutable and passed by reference to functions. If you want to modify a list without affecting the original, use the .copy() method or use the slice notation [:] you can specify start and end positions

# You can split a string into a list string.split()
#You can join a list by appending the separator wihth the method
# ".".join(mylist)


import swapfunction

# swap_array = swapfunction 

mylist = [13, 15, 8, 5]

print(mylist)


#Basic of list comrepehsion Technically puts x from the first loop if it meets the second condition

first_num = [1, 2, 34, 5, 6, 2, 3, 5, 9, 6, 4, 1, 8, 5, 3, 22, 789]
second_num = [3, 4, 3, 78, 4, 2, 5, 5, 67, 88, 0, -0, 7, 5, 4, 23, 54, 65, 789]

third_num = [x for x in first_num]

for x in second_num:
    third_num.append(x)

print(third_num)

# Combining dictionaries to take count:

num_dict = dict()

for x in third_num:
    num_dict[x] = num_dict.get(x, 0) + 1
    

for k, v in num_dict.items():
    print(f"The number {k}\tappears {v} times")

