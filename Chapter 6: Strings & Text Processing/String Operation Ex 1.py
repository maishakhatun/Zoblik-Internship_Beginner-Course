#Exercise 1: Product Name Transformation
#Zoblik is rebranding some products. You need to standardize their names.

# Current product name in Zoblik's inventory system
old_product_name = "zoblik advanced security camera"

# Task 1: Convert the product name to all uppercase for a new product ID label.
# Task 2: Capitalize the first letter of each word for display on the website.
#         (Hint: Look up a string method that capitalizes words!)
# Task 3: Replace "gaming headset" with "Pro Gaming Headphones" for updated marketing.

# --- Your code goes here ---

# Task 1
product_id_label = old_product_name.upper()
print(f"Product ID Label: {product_id_label}")

# Task 2 (Using .title() method)
website_display_name = old_product_name.title()
print(f"Website Display Name: {website_display_name}")

# Task 3
updated_marketing_name = old_product_name.replace("gaming headset", "Pro Gaming Headphones")
print(f"Updated Marketing Name: {updated_marketing_name}")