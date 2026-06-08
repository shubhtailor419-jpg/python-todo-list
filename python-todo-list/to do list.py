tasks = []


def show_tasks():
    if not tasks:
        print("\nYou don't have any tasks yet.")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")


while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        task = input("Enter a new task: ").strip()

        if task:
            tasks.append(task)
            print("Task added.")
        else:
            print("Task cannot be empty.")

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        if not tasks:
            print("No tasks available to remove.")
            continue

        show_tasks()

        try:
            number = int(input("\nWhich task do you want to remove? "))

            if 1 <= number <= len(tasks):
                removed_task = tasks.pop(number - 1)
                print(f"Removed: {removed_task}")
            else:
                print("Please choose a valid task number.")

        except ValueError:
            print("Enter a number only.")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")