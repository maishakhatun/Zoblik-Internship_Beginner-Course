# Exercise: List Manager
#Write a program that allows users to add, remove, and display items in a list.

#initializing the function 

#displaying the menu
def menu_displaying():
    print("\nDisplay Manager List: ")
    print("\n1 to ADD AN ITEM")
    print("\n2 to REMOVE AN ITEM")
    print("\n3 to DISPLAY ITEMS")
    print("\n4 to EXIT")
    print("------------------------------")

#function for adding the item
def add_item(list):
    item = input("Enter the item to add: ")
    list.append(item)
    print(f"{item} is added to the list.")

#function for removing the item
def remove_item (list):
    if not list:
        print("There is nothing to remove. The list is empty!")
        return
    remove_item = input("Enter the item to remove: ")
    if remove_item in list:
        list.remove(remove_item)
        print(f"{remove_item} is removed from the list.")
    else:
        print(f"{remove_item} is not found in the list.")

#function for displaying the items
def display_items (list):
    if not list:
        print("There is nothing to display in the list.")
    else: 
        print("Your current list items:")
        for i, item in enumerate(list, 1):
            print(f"{i}. {item}")

#function for exit
def exit_program():
    print("Exiting List Manager!")

#the main function
def main():
    list = []

    while True:
        print("\n----- List Manager -----")
        print("1. Add item")
        print("2. Remove item")
        print("3. Display items")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_item(list)
        elif choice == '2':
            remove_item(list)
        elif choice == '3':
            display_items(list)
        elif choice == '4':
            exit_program()
            break
        else:
            print("Invalid choice! Please try again.")


# Running the program
main()