# Trying hands on LinkedList using Classes in Python

# Create a Node Class
class Node:
	def __init__(self, value, next_item):
		self.value = value
		self.next = next_item


# List printing function
def print_list(head):
	index = 1
	current = head
	while current:
		print(f"{index} : {current.value}")
		current = current.next
		index += 1


def add_node_begin(head, value):
	new_node = Node(value, None)
	new_node.next = head

	return new_node


# Instantiate first member
item1 = Node(250, None)
item2 = Node(455, None)
item1.next = item2

item3 = Node(189, None)
item2.next = item3

print_list(item1)
print("========================")

new_item1 = add_node_begin(item1, 780)
print_list(new_item1)

print("========================")

new_item2 = add_node_begin(new_item1, 554)

print_list(new_item2)
