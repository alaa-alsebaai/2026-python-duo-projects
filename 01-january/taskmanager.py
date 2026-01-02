import os

exitsys = 0
tasks = []


def list_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r", encoding="utf-8") as file:
            return [line.strip() for line in file]
    return []


def add_task():
    valid_description = 0
    while valid_description == 0:
        description = input("Enter task description: ").strip()
        if len(description) == 0:
            print("Description can't be empty.")
        elif len(description) > 100:
            print("Description can't be longer than 100 characters.")
        else:
            valid_description += 1
    existing_tasks = list_tasks()
    existing_tasks.append(f"☐ {description}")
    with open("tasks.txt", "w", encoding="utf-8") as file:
        for task in existing_tasks:
            file.write(f"{task}\n")
    print(f"Task {description} added successfully.")


def delete_task():
    current_tasks = list_tasks()
    if not current_tasks:
        print("No tasks to delete\n")
        return
    print("Your tasks: \n")
    for i, task in enumerate(current_tasks, start=1):
        print(f"{i}. {task}")
    try:
        task_num = int(input("Enter number of task to delete: "))
        if 1 <= task_num <= len(current_tasks):
            valid_confirm = 0
            while valid_confirm == 0:
                confirm = input(
                    f"Are you sure you want to delete task{task_num}? (Y/n): ").lower().strip()
                if confirm == "y" or confirm == "yes":
                    deleted_task = current_tasks.pop(task_num - 1)
                    with open("tasks.txt", "w", encoding="utf-8") as file:
                        for task in current_tasks:
                            file.write(f"{task}\n")
                    print(f"Task {deleted_task} deleted successfully.")
                    valid_confirm += 1
                elif confirm == "n" or confirm == "no":
                    print("Deletion cancelled.")
                    valid_confirm += 1
                else:
                    print("Please enter(Y/n)")
        else:
            print(f"Please enter a number between 1 and {len(current_tasks)}")
    except ValueError:
        print("Please enter a valid number.\n")
    except Exception as e:
        print(f"An error occurred: {e}\n")


def complete_task():
    current_tasks = list_tasks()
    if not current_tasks:
        print("No tasks to check as completed.\n")
        return
    print("Your Tasks: \n")
    for i, task in enumerate(current_tasks, start=1):
        print(f"{i}. {task}")
    try:
        task_num = int(
            input("Enter number of task you want to check/uncheck.:"))
        if 1 <= task_num <= len(current_tasks):
            task = current_tasks[task_num-1]
            if task.startswith("☐"):
                current_tasks[task_num - 1] = task.replace("☐", "☑", 1)
                print(f"Task {task_num} checked as completed successfully.")
            elif task.startswith("☑"):
                current_tasks[task_num - 1] = task.replace("☑", "☐", 1)
                print(f"Task {task_num} unchecked as completed successfully.")
            with open("tasks.txt", "w", encoding="utf-8") as file:
                for t in current_tasks:
                    file.write(f"{t}\n")
        else:
            print(
                f"Please enter a task number between 1 and {len(current_tasks)}\n")
    except ValueError:
        print("Please enter a valid number.\n")


while exitsys == 0:
    print("\n" + "="*40)
    print("Welcome to task manager\nPlease enter the number of action\n")
    print("1.List Tasks 2.Add Task 3.Delete task 4.Check/uncheck tasks 5.Exit")

    action = input("Enter Action: ").strip()
    if not action.isdigit():
        print("Please enter a number 1-5.")
        continue

    action = int(action)
    if action == 1:
        current_tasks = list_tasks()
        if current_tasks:
            print("Your Tasks:\n")
            for i, task in enumerate(current_tasks, start=1):
                print(f"{i}. {task}\n")
        else:
            print("No tasks yet.")
    elif action == 2:
        add_task()
        print("Returning to main menu...")
    elif action == 3:
        delete_task()
        print("Returning to main menu...")
    elif action == 4:
        complete_task()
        print("Returning to main menu...")
    elif action == 5:
        print("Goodbye User.")
        print("\n" + "="*40)
        exitsys += 1
    else:
        print("Please Enter a valid action number.")
