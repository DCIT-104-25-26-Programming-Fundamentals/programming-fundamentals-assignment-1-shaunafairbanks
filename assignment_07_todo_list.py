
# List to store tasks
tasks = []


# Function to add a task
def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print(f'Task added: "{task}"')


# Function to view all tasks
def view_tasks():
    if len(tasks) == 0:
        print("Your to-do list is empty.")
    else:
        print("\nYour Tasks:")
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")


# Function to delete a task
def delete_task():
    if len(tasks) == 0:
        print("Your to-do list is empty.")
        return

    view_tasks()

    task_number = int(input("Enter task number to delete: "))

    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f'Task "{removed_task}" has been removed.')
    else:
        print("Error: Invalid task number.")


# Main function
def main():
    while True:
        print("\n============================")
        print("      TO-DO LIST MENU")
        print("============================")
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number from 1 to 4.")


# Run the program
main()