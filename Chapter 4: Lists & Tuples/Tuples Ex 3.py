#Exercise 3: Unpack Your Zoblik Order!
#You've received an order from Zoblik, and it's represented as a tuple. 
# Let's unpack it to access the individual details easily.

'''
Try it Yourself: 
reate your own tuple representing a simple "student record" with (student_name, student_id, grade). 
Then, unpack it into three separate variables and print each one!
'''


# Exercise 3: Unpack a Zoblik order tuple
zoblik_order = (12345, "Customer A", "Laptop Pro", 1)

# Unpack the order details into separate variables
order_id, customer_name, item_ordered, quantity = zoblik_order

# Print out each variable to confirm
print(f"Order ID: {order_id}")
print(f"Customer Name: {customer_name}")
print(f"Item Ordered: {item_ordered}")
print(f"Quantity: {quantity}")

#My tuple
student_record = ("Robert", "STID156", 11)
student_name, student_id, grade = student_record

#print each variable one by one
print(f"\nStudent's Name: {student_name}")
print(f"Student's ID: {student_id}")
print(f"Grade: {grade}")