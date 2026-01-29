#Exercise 2: Parameters and Arguments
#Now, let's make our greeting function more personalized by adding a parameter.

# Exercise 2: Define a function with a parameter
def greet_person(name_to_greet, city_name):
    print(f"Hi there, {name_to_greet}!")
    print(f"Greetings to you in {city_name}")
    print(f"Glad you're learning about functions.\n")

# Call the function with different arguments
greet_person("Zoblik Trainee", "Kolkata")
greet_person("Python Fan", "Hyderabad")
greet_person("Aisha", "London")