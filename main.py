from task import Task
from task_manager import TaskManager
from utils import print_menu, get_task_details


def main():
    manager = TaskManager()

    while True:
        print_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            title, description = get_task_details()
            task = Task(title, description)
            manager.add_task(task)

        elif choice == "2":
            manager.show_tasks()

        elif choice == "3":
            manager.show_tasks()

            try:
                task_number = int(input("Enter task number to complete: "))
                manager.complete_task(task_number - 1)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            print("Thank you for using Task Manager.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()