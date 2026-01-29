#Exercise 2: Using List Methods
#Now, let's update Zoblik's team list using append, remove, and sort.

# Start with our marketing team list
marketing_team = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
print(f"Initial Team: {marketing_team}")

# A new member, Frank, joins the team. Add him.
marketing_team.append("Frank")
print(f"Team after Frank joins: {marketing_team}")

# A new member, Adam, joins the team. Add him.
marketing_team.append("Adam")
print(f"Team after Adam joins: {marketing_team}")

# A new member, Steve, joins the team. Add him.
marketing_team.append("Steve")
print(f"Team after Steve joins: {marketing_team}")

'''#Removing a name that is not in the list. "Stacy" 
marketing_team.remove("Stacy")
print(f"Team after Stacy Leaves : {marketing_team}")
'''
# Charlie moved to a different department. Remove him.
marketing_team.remove("Charlie")
print(f"Team after Charlie leaves: {marketing_team}")

# The manager wants the list sorted reverse alphabetically for roll call.
marketing_team.sort(reverse=True)
print(f"Team sorted in reverse alphabetically: {marketing_team}")