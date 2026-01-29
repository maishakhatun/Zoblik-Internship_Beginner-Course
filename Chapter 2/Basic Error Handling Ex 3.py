#Exercise 3: Raising Your Own Errors
#Details and example:
#Imagine Zoblik has a strict policy: a product ID must be exactly 5 digits long. 
# Write a function that takes a product ID as input. 
# If the ID is not exactly 5 digits, raise a ValueError with a clear message. 
# Then, use a try-except block to call this function and catch the ValueError if it occurs.

print("\n--- Zoblik Product ID Validator ---")

class InvalidZoblikProductError(Exception):
    def __init__(self, product_id, message="Product ID must start with 'Z' for Zoblik products."):
        self.product_id = product_id
        self.message = message
        super().__init__(f"{message} (Got: {product_id})")

def validate_product_id(product_id):
    if not product_id.upper().startswith('Z'):
        raise InvalidZoblikProductError(product_id)
    numeric_part = product_id[1:]
    if not numeric_part.isdigit():
        raise ValueError("Product ID must contain only digits after 'Z'.")
    if len(product_id) != 6:
        raise ValueError("Product ID must start with 'Z' followed by exactly 5 digits (e.g., Z12345).")
    print(f"✅ Product ID '{product_id}' is valid for Zoblik products.")

try:
    user_id = input("Enter a 5-digit Zoblik product ID: ")
    validate_product_id(user_id)
except InvalidZoblikProductError as ze:
    print(f"Custom Error: {ze}")
    print("Hint: Make sure your product ID starts with 'Z'.")
except ValueError as ve:
    print(f"Validation Error: {ve}")
    print("Please check the product ID and try again.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print("\nProduct ID validation process completed.")