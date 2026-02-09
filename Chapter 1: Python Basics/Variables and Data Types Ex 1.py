#Excercise 1 Working with numbers
# calculate the total number of items in a small shipment and their combined weight.
item_a_quantity=int(input("Enter the quantity of first item: "))
item_b_quantity=int(input("Enter the quantity of second item: "))
weight_a=float(input("Enter the weight of item A: "))
weight_b=float(input("Enter the weight of item B: "))
print(f"Item A quantity: {item_a_quantity}")
print(f"Item B quantity: {item_b_quantity}")
print(f"Item A weight: {weight_a}")
print(f"Item B weight: {weight_b}")
total_quantity=item_a_quantity+item_b_quantity
print(f"Total quantity: {total_quantity}")
total_weight=weight_a+weight_b
print(f"Total weight: {total_weight}")