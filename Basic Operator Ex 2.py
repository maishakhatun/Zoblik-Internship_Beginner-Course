# Exercise 2: Zoblik Inventory Alert

# Zoblik warehouse stock user input and data
product_name = input("Enter the product name: ")
current_stock = int(input("Enter the current stock: "))
stock_threshold = 20

# checking if the stock needs restock by using comparison operator
is_stock_low = current_stock < stock_threshold

# displaying the user input values
print(f"\nProduct Name: {product_name}")
print(f"Current Stock: {current_stock}")
print(f"Stock Threshold: {stock_threshold}")
print(f"Is the stock low? {is_stock_low}")

# Clear message for reordering
if is_stock_low:
    print(f"Stock is below {stock_threshold}! Reordering needed.")
else:
    print(f"Stock is sufficient (no reorder needed).")

# condition: is the stock low
if is_stock_low:
    # displaying the required stock to meet threshold
    stock_required = stock_threshold - current_stock
    print(f"Amount you need to meet the threshold: {stock_required}")
    
    # taking user input exact amount to be restocked
    new_shipment_amount = int(input("Stock is low! Enter shipping amount: "))

    # updating the stock after shipment
    updated_stock = new_shipment_amount + current_stock
    print(f"Updated stock amount: {updated_stock}")
    
    # rechecking
    is_stock_low_after_shipment = updated_stock < stock_threshold
    print(f"Is the stock low after shipment? {is_stock_low_after_shipment}")
else:
    print("Product stock is sufficient. No restock needed!")