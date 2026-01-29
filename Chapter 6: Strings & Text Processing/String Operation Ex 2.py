#Exercise 2: Extracting Order Details
#You're processing order confirmations for Zoblik. Each confirmation has a standard format.

# A sample Zoblik order confirmation string
order_confirmation = "CONFIRMATION_ZOB_PY2024_ORD12345_CUST987_DATE20240415"
# New Zoblik order confirmation string (custom example)
order_confirmation = "CONFIRMATION_ZOB_PY2025_ORD99999_CUST555_DATE20250130"

# Task 1: Extract Order ID (starts at index 24, length 8)
order_id = order_confirmation[24:32]
print(f"Order ID: {order_id}")

# Task 2: Extract Customer ID (starts at index 33, length 8)
customer_id = order_confirmation[33:41]
print(f"Customer ID: {customer_id}")

# Task 3: Extract Date (starts at index 46, length 8)
order_date = order_confirmation[46:54]
print(f"Order Date: {order_date}")

# Extra Task: What happens if slicing is out of bounds?
out_of_bounds = order_confirmation[200:300]  # Beyond string length
print(f"Out-of-bounds result: '{out_of_bounds}'")


'''
# Task 1: Order ID starts after 'ORD' and is 7 characters long
order_id = order_confirmation[20:27] # CONFIRMATION_ZOB_PY2024_ORD12345_...
print(f"Order ID: {order_id}")

# Task 2: Customer ID starts after 'CUST' and is 7 characters long
customer_id = order_confirmation[32:39] # ..._CUST987_DATE...
print(f"Customer ID: {customer_id}")

# Task 3: Date starts after 'DATE' and is 8 characters long
order_date = order_confirmation[43:51] # ..._DATE20240415
print(f"Order Date: {order_date}")
'''