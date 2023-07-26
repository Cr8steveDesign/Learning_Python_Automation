# A Function that receives input from the user and converts it to
# the binary representation of that number


# Retrieve number from user and validate
def get_decimal():

	num_convert = 0

	while True:
		user_input = input("Please enter the positive integer: ")
		continue_choice = "YES"

		if user_input.isdigit():
			num_convert = int(user_input)
			break
		else:
			print("=" * 50)
			print(f"Sorry, the number you entered [{user_input}] is not a valid number.")
			print("=" * 50)

			while True:
				choice = input("Type YES to try again or NO to quit the program. ").upper()

				if choice == continue_choice:
					break
				else:
					quit()
	return num_convert

# Define function to handle conversion

def binary_convert(decimal):

	binary_conv = []

	if decimal == 0:
		return (decimal)

	while decimal > 0:
		binary_conv.insert(0, int(decimal % 2))
		decimal //= 2

	final_str = "".join(str(el) for el in binary_conv)

	return final_str


# Call program function
decimal = get_decimal()

binary_str = binary_convert(decimal)

# Print output
print("=" * 50)
print(f"The number you entered: {decimal} \nRepresented in binary as: {binary_str}")
print("=" * 50)