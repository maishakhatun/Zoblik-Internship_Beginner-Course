'''
👉 Try it Yourself:
Can you modify this so it also asks the user for their own product name and price, instead of using fixed values?
'''
# Exercise 3: Zoblik Product Summary
product_name = input("Enter your product name: ")
price_per_unit = float(input("Enter the price per unit: "))

# Ask the user for the quantity
quantity_str = input(f"How many '{product_name}' units would you like? ")

# Convert quantity to a number (we'll cover this more in depth later)
quantity = int(quantity_str)

# Calculate total cost
total_cost = quantity * price_per_unit

# Display the summary using an f-string
print(f"\n--- Zoblik Order Summary ---")
print(f"Product: {product_name}")
print(f"Quantity: {quantity}")
print(f"Price per unit: \u20B9{price_per_unit:.2f}")
print(f"Total cost: \u20B9{total_cost:.2f} ")
print(f"--------------------------")