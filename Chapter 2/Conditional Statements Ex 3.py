# Exercise 3: Zoblik Event Registration
# Zoblik is hosting an event! We need to check if a person is eligible to register based on multiple criteria.

# taking user input
is_student = input("Are you a student? (True/False): ").strip().lower() == "true"
has_coupon = input("Do you have a coupon? (True/False): ").strip().lower() == "true"
is_vip = input("Are you a VIP? (True/False): ").strip().lower() == "true"
age = int(input("Mention your age: "))

print("\nChecking if the user is eligible for the registration of Zoblik Event...")

# applying conditions
if is_vip:
    print("VIP Registration: Welcome to Zoblik Event!")

elif age >= 16:  # Non-VIP users must be at least 16 years old
    if is_student or has_coupon:
        print("Standard Registration (Age 16 or above): Welcome to Zoblik Event!")
    else:
        print("Registration Denied: Must be a student or have a coupon.")
else:
    print("Registration Denied: Age must be at least 16 for non-VIP registration.")

print("-----Eligibility checking completed-----")