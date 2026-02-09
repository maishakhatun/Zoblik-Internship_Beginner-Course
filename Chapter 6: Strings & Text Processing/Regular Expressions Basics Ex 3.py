#Exercise 3: Understanding re.match, re.search, and re.findall
#Let's see the different behaviors of match, search, and findall in action with a single string. 
# We want to find "project".

import re

data_string = "Our new project is launching soon. This project will be a game changer for Zoblik."
target_pattern = r"project"

# --- Using re.match() ---
print("--- Using re.match() ---")
match_result = re.match(target_pattern, data_string)
if match_result:
    print(f"re.match found: '{match_result.group()}' at position {match_result.start()}")
else:
    print(f"re.match did NOT find '{target_pattern}' at the beginning of the string.")


# --- Using re.search() ---
print("--- Using re.search() ---")
search_result = re.search(target_pattern, data_string)
if search_result:
    print(f"re.search found: '{search_result.group()}' at position {search_result.start()}")
else:
    print(f"re.search did NOT find '{target_pattern}'.")


# --- Using re.findall() ---
print("--- Using re.findall() ---")
findall_results = re.findall(target_pattern, data_string)
print(f"re.findall found all occurrences: {findall_results}")

'''
re.match() = finds 'project' at position 0

re.search() = finds 'project' at position 0

re.findall() = returns ['project']
'''