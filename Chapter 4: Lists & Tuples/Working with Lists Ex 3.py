#Exercise 3: Slicing the List
#Let's imagine Zoblik has a long list of order IDs, and you need to process just a batch from the middle or the end.

# Zoblik's list of recent order IDs
order_ids = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]
print(f"All Order IDs: {order_ids}")

# Get the first 5 order IDs for morning processing (indices 0 to 4)
morning_batch = order_ids[0:5]
print(f"Morning Batch: {morning_batch}")

#Get the first 7 orders (indices 0 to 8)
mid_morning_batch = order_ids [0:7]
print(f"Mid Morning Batch: {mid_morning_batch}")

#Get every third order starting from the second order
third_oder = order_ids [1::3]
print(f"Every third order starting from 2nd order: {third_oder}")

# Get order IDs from the 6th to the 8th (indices 5, 6, 7)
midday_batch = order_ids[5:8]
print(f"Midday Batch: {midday_batch}")

# Get the last 3 order IDs for evening processing (indices -3 to end)
evening_batch = order_ids[-3:]
print(f"Evening Batch: {evening_batch}")

# Get every other order ID to check for discrepancies
sampled_ids = order_ids[::2]
print(f"Sampled Order IDs (every other): {sampled_ids}")

#Negative step values experiment
negative_step = order_ids [::-1]
print(f"Negative step values: {negative_step}")