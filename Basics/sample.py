#First Python File
# print("Hello World")

# print("Please Enter your name:")
# name = input()
# print(f"Hello {name}")

# print("Thank you for your time")

def qrsort(a, b):
    if (a - b) >= 0:
        return a
    else: 
        return b
    

max = qrsort(15, 55)

print(max)