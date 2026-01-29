# Exercise 1: Unique Friends List

# Your messy list of friends
invite_list = ["Alice", "Bob", "Charlie", "Alice", "David", "Bob", "Eve", "Steve", "Robert", "Eve", "Robert", "Mike", "William"]

#An empty set using set() and adding names one by one using .add()
empty_list = set()
empty_list.add("Max")
empty_list.add("Thomas")
empty_list.add("Harper")
empty_list.add("Joyce")

# Create a set from the list to get unique invitees
unique_invitees = set(invite_list)

print(f"Original invite list: {invite_list}")
print(f"Unique invitees: {unique_invitees}")

# How many unique people are invited?
print(f"Number of unique invitees: {len(unique_invitees)}")

print(f"Names in the empty list: {empty_list}")