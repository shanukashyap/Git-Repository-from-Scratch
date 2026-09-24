def print_menu():
    print("\n===== TASK MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Exit")


def get_task_details():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    return title, description