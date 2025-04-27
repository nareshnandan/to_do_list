# Simple To-Do List with a function

tasks = []

def show_menu():
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added successfully!")
    elif choice == '2':
        print("\nYour Tasks:")
        for t in tasks:
            print("-", t)
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
