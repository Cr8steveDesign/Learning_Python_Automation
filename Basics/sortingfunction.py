# Simple Sorting Function.
# Returns the largest of two numbers

def qrsort(a, b):
    if (a - b) >= 0:
        return a
    else: 
        return b
    

max_var = qrsort(15, 55)

print(max_var)