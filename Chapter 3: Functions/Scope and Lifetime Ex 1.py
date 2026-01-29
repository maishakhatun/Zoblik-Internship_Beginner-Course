#Exercise 1: Local vs. Global Interaction
#This exercise will help you see the difference between local and global variables in action.

# Global variable for Zoblik's main product line
main_product = "Zoblik Quantum Processors"
#global variable for product focus
team_product_focus = "Zoblik NanoBots"
def introduce_product_team(team_name):
    # Local variable for the team's specific focus
    #team_product_focus = "Zoblik NanoBots"
    print(f"Team '{team_name}' focuses on: {team_product_focus}")
    print(f"Overall Zoblik's main product is: {main_product}")

def display_global_product():
    print(f"From global context: {main_product}")
    # Uncommented the line below 
    print(team_product_focus)

print("\n--- Initial Product Overview ---\n")
display_global_product()

print("\n--- Introducing a Team ---")
introduce_product_team("Innovation Squad")

print("\n--- After Team Introduction (Global Context) ---")
display_global_product()

#QNA
#Inside display_global_product(), uncomment the line print(team_product_focus). What error do you get? Why? (Hint: Think about local scope!)
'''
ANSWER: Uncommenting print(team_product_focus) caused an error because team_product_focus was defined in the local scope of another function, making it inaccessible here. Declaring it in the global scope allows all functions to access it.
'''