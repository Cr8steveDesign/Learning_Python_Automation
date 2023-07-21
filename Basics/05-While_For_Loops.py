"""
While Loops - Running a statement of code repeatedly while a 
given condition is True
"""

# Testing

#Iterating through a string with a while loop, and testing the else statement of the while loop

sentence = "My name is omoregie stephen, I am a Senior Software Developer"

index = 0
newsentence = ""

#using the in keyword. This version of for loop iterates over every character in the string (can be used for other data collections) and automatically advances to the next till it reaches the end of the collection 

# for ch in sentence:
#     if ch == 'o':
#         newsentence += ch.upper()
#     else:
#         newsentence += ch

# print(newsentence)
# print("===Other Method==")

# Using the range function 

"""
for i in range(len(sentence)):
    if sentence[i] == 'o' and sentence[i + 1] == 'm':
        newsentence += sentence[i].upper()
        
    elif sentence[i] == 's' and sentence[i + 1] == 't':
        newsentence += sentence[i].upper()
        
    else:
        newsentence += sentence[i]
print(newsentence)

"""

# Implementing a While Loop
# Guessing Game

win_num = 18
guess_count = 0
guess = 0

print("=" * 30)
print("The Number Guessing Game")
print("=" * 30)

while True:
    guess = int(input("> Enter you guess: "))
    guess_count += 1
    guess_str = "guess" if guess_count < 2 else "guesses"
           
    if guess == win_num:
        print("=" * 60)
        print(f"Yaaay! 😎 You are correct! The number is {win_num} \nand you got it in {guess_count} {guess_str}")
        print("=" * 60)
        
        break
    
    else:
        if guess_count > 3:
            print("Ooops! Guess limit reached! 😅")
            break

        print("Soorry 😏. Wanna try again?")
        try:
            answer = input("> Enter Y to try again or N to quit: ")
        except TypeError:
            print("Wrong input")
            break
            
        if answer.upper() == "Y":
            continue       
        else:
            break
        


print("Thanks for playing!")
    
    
    
    
    

