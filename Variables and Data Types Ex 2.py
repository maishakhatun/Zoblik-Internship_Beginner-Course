#Crafting Strings
# Generate welcome messages for new employees and product announcement headlines.
#Enter first and last name
First_name=input("Enter your first name: ")
last_name=input("Enter your last name: ")
#product name and version
product_name="Zoblik Connect"
product_version="2.0"
#creating a welcome message for the new employee
message="Welcome,"+First_name+" "+last_name+" to the Zoblik Team! "
print(f"Message: {message}")
#product announcement headline
headline= product_name+" "+product_version+" is now available!"
print(f"Product Announcement: {headline}")