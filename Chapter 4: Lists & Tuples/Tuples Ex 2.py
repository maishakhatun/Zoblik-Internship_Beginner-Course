#Exercise 2: Understanding Immutability - The Attempted Change
#Now, let's try to change an element in a tuple to really understand immutability. 
# You'll see Python's strictness in action!

# Exercise 2: Attempt to change an element in a tuple
# We have a tuple for a Zoblik "Compact Keyboard".
keyboard_info = ("CK303", "Compact Keyboard", 59.99)

print(f"Original keyboard info: {keyboard_info}")

# Try to change the price to 65.50.
# Uncomment the line below and run the code to see the error!
#keyboard_info[2] = 65.50

print("If you uncommented the line above, you'd see an error!")

'''
We cannot insert data into a tuple using the append() method like we do with lists, because tuples are immutable.
If we need to modify a tuple, there are two approaches:
--Create a new tuple with the desired changes.
--Convert the tuple into a list (since lists are mutable), make the necessary modifications, and then convert it back to a tuple when no further changes are needed.
'''