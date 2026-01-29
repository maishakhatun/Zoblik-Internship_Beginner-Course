#Exercise 3: Managing Zoblik's Project Tasks
# Initial set of active tasks
active_tasks = {"Design Mockups", "Develop Frontend", "Write API Docs", "Set Up Database"}
print(f"Current active tasks: {active_tasks}\n")

# A new task is assigned: Add "Implement User Auth"
active_tasks.add("Implement User Auth")
print(f"After adding 'Implement User Auth': {active_tasks}")

'''#Trying to remove a task not mentioned in active_tasks
active_tasks.remove("Develop Backend")
print(f"{active_tasks}")'''

# "Design Mockups" is completed: Remove it
active_tasks.remove("Design Mockups")
print(f"After removing 'Design Mockups': {active_tasks}")

# A task that might or might not be there: "Refactor Old Code"
# Use discard() to avoid errors if it's not present
active_tasks.discard("Refactor Old Code")
print(f"After attempting to discard 'Refactor Old Code': {active_tasks}")

# Simulate a random task being picked for urgent review
if active_tasks: # Make sure the set isn't empty before popping
    urgent_task = active_tasks.pop()
    print(f"\nUrgent task picked (randomly): {urgent_task}")
    print(f"Remaining active tasks: {active_tasks}")

'''# All tasks completed for the day! Clear the set.
active_tasks.clear()
print(f"After clearing all tasks: {active_tasks}")'''

#Using POP until the set is empty
while active_tasks:
    task = active_tasks.pop()
    print(f"Popped task: {task} | Remaining tasks: {active_tasks}")

# Trying to pop after the set is empty
print("\nTrying to pop again after the set is empty...")

try:
    active_tasks.pop()
except KeyError as e:
    print(f"Error occurred: {e}")