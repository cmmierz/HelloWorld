# Simple To-Do List App
# This program lets you create, view, and delete tasks 
# It also saves your tasks to a file called "tasks.txt" so they don't disappear when you close the program

def load_tasks(): # loads tasks from file called task.txt (if it exists)
    try: # try to open file "tasks.txt" in read mode
        with open("tasks.txt", "r") as file: # "with" automatically closes the file when done
            tasks = [line.strip() for line in file.readlines()] # read each line, remove the "\n" at the end using .strip(), and put them in a list called tasks
    except FileNotFoundError:
        tasks = [] # If the file doesn't exist, start with an empty list
    return tasks # Return the list of tasks so it can be used elsewhere


def save_tasks(tasks): # Saves the current list of tasks to "tasks.txt"
    with open("tasks.txt", "w") as file: # open (or create) the file in write mode ("w"), which overwrites old contnet 
        for task in tasks: # write each task on its own line
            file.write(task + "\n")


def show_tasks(tasks): # Prints out all current tasks to the screen
    if not tasks: # if the list is empty, print a message
        print("No tasks available.")
    else: # otherwise, print each task with its number
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1): # enumerate() gives both the index (starting at 1) and the task itself
            print(f"{i}. {task}")
    print() # print a blank line for better formatting


def main(): # main program loop - shows menu and handles user input
    tasks = load_tasks() # load existing tasks from file (or empty list if none)

    while True: # start a loop that keeps running until the user chooses to exit
        # show the menu options
        print("===To-Do List Menu===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ") # ask the user to pick a menu option

        if choice == '1': # view tasks 
            show_tasks(tasks)
        
        elif choice == '2': # add a new task
            new_task = input("Enter the new task: ") # ask what task they want to add
            tasks.append(new_task) # add that task to the end of the list
            save_tasks(tasks) # save the updated list to the file
            print("Task added.\n")  
        
        elif choice == '3': # remove a task
            show_tasks(tasks)    # show all tasks so they can pick which one to delete
            task_num = input("Enter the task number to remove: ") # ask for the number of the task to remove

            if task_num.isdigit() and 1 <= int(task_num) <= len(tasks): # check if the unput is a number and within the valid range
                removed_task = tasks.pop(int(task_num) - 1) # convert input to a number and remove that task from the list
                save_tasks(tasks) # save the updated list to the file
                print(f"Removed task: {removed_task}\n")
            
            else: # if the input was invalid, show an error message
                print("Invalid task number.\n")
        
        elif choice == '4': # exit the program
            print("Goodbye!")
            break # "break" exits the while loop and ends the program

        else: # handle invalid menu choices
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__": # This line makes sure the program only runs if this file is executed directly (not imported as a module)
    main() # Call the main function to start the program