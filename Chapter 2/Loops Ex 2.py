#Exercise 2: Mastering while Loops
#Let's simulate a Zoblik factory machine that processes items one by one until its internal counter reaches zero.

items_to_process = 5  # Imagine this is a sensor reading from the machine

print("--- Zoblik Factory Processing ---")
#loop starts
while items_to_process > 2:
    print(f"Processing item {items_to_process}... Machine humming!")
    ready = input("Ready for next item? (yes/no): ").strip().lower()
    # Stop immediately if user says no
    if ready == "no":
        break  
    else:
        items_to_process = items_to_process - 1  # Crucial step!

print("--- Machine done processing! Moving to next batch. ---")
