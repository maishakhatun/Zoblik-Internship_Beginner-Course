#Exercise 1: Finding a Specific Company Name
#Let's start simple. Zoblik Corp. needs to find every mention of their own name in a marketing draft.

import re

# Marketing draft text
marketing_text = "This quarter, Zoblik Corp. achieved record sales. Zoblik is expanding globally, and the team at Zoblik is excited."
search_pattern = r"Zoblik" # Our simple pattern for "Zoblik"

# Use re.findall to get all occurrences
all_mentions = re.findall(search_pattern, marketing_text)

print(f"Original text: {marketing_text}")
print(f"All mentions of '{search_pattern}': {all_mentions}")

'''
search_pattern = r"team"
all_mentions = re.findall(search_pattern, marketing_text)
print(all_mentions)
O/P ['team']
'''

'''
search_pattern = r"record"
all_mentions = re.findall(search_pattern, marketing_text)
print(all_mentions)
O/P ['record']
'''

'''
search_pattern = r"the"
all_mentions = re.findall(search_pattern, marketing_text)
print(all_mentions)
print(len(all_mentions))
O/P 
['the']
1
'''