# Reading Files in Python

# You use the open(filename, mode) function to open a file
# It returns an object 

#open the file
filehandler = open('helloworld.txt', 'r')

# Use .read() to retrieve all words and split the returned object with .split()

#This returns a list of each line
textfile = filehandler.readlines()

#close the file after you're done
filehandler.close()

seen_line = ""
count_big_words = 0

for lines in textfile:
    if "practice" in lines:
        seen_line = lines
        print("==================")

#Best Still, remove newline or trailing whitespace with .rstrip()
seen_line = seen_line.replace("\n", "").split(" ")

print(seen_line)

for word in seen_line:
    if len(word) > 5:
        print(word)
        count_big_words += 1

print(f"There are  {count_big_words} big words in the search list.")

"""
# Example content to add
new_content = "This is new content.\n"

# Open the file in append mode ('a')
with open('example.txt', 'a') as file:
    # Write the new content to the file
    file.write(new_content)


# Example content to add (multiple lines)
new_content = ["Line 1\n", "Line 2\n", "Line 3\n"]

# Open the file in append mode ('a')
with open('example.txt', 'a') as file:
    # Write the new content to the file
    file.writelines(new_content)



"""

#Other File Methods 
# .startswith("text")