#Exercise 2: Extracting Phone Numbers
#Your task is to extract all valid phone numbers from a support ticket system. 
# For this exercise, assume phone numbers are in the format XXX-XXX-XXXX (e.g., 123-456-7890).

import re

# Support ticket description
ticket_description = "Customer's contact: 555 123 4567. Another number: (123) 456-7890. Old contact was 987 654 3210. Incorrect format: 1234567890."

# Regex pattern for XXX-XXX-XXXX format
# \d{3} matches exactly three digits
# - matches the literal hyphen
# We use parentheses around the whole pattern to capture it as a group
#phone_pattern = r"\d{3}-\d{3}-\d{4}"
phone_pattern = r"\d{3}\s\d{3}\s\d{4}"
# Find all occurrences of the pattern
found_phones = re.findall(phone_pattern, ticket_description)

print(f"Original description: {ticket_description}")
print(f"Found phone numbers: {found_phones}")