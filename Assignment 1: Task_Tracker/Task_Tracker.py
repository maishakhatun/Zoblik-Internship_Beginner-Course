# Assignment 1: Task Tracker

def main():
    todo = []   

    while True:
        command = input("\nWhat do you want to do? (add/view/complete/exit): ").lower() .strip()

        if command == "add":
            task = input("Write your task: ")
            if t != "":
                todo.append(t)
                print("Added!")
            else:
                print("Task was empty so not added.")

        elif command == "view":
            if len(todo) == 0:
                print("Nothing to show.")
            else:
                print("\nTasks right now:")
                num = 1
                for stuff in todo:
                    print(num, ".", stuff)
                    num += 1

        elif command == "complete":
            if len(todo) == 0:
                print("No tasks yet.")
                continue

            print("\nHere are your tasks:")
            for i, stuff in enumerate(todo, start=1):
                print(i, ".", stuff)

            done = input("Which one is done? (enter number): ")
            if done.isdigit():
                pos = int(done) - 1
                if pos >= 0 and pos < len(todo):
                    todo[pos] = "[x] " + todo[pos]
                    print("Marked as done.")
                else:
                    print("That number doesn't exist.")
            else:
                print("Please enter a valid number.")

        elif command == "exit":
            print("Goodbye!")
            break

        else:
            print("Please enter a valid command (add, view, complete, exit).")

if __name__ == "__main__":
    main()
