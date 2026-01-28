# main.py
from task_manager import TaskManager
from status import TaskStatus

def print_menu():
    print("\n--- TaskFlow Menu ---")
    print("1. Create Task")
    print("2. List Tasks")
    print("3. Update Task Status")
    print("4. Delete Task")
    print("5. Exit")

def main():
    manager = TaskManager()

    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        try:
            # CREATE TASK
            if choice == "1":
                title = input("Enter task title: ").strip()
                if not title:
                    print("Task title cannot be empty.")
                    continue

                description = input("Enter task description: ").strip()
                task = manager.create_task(title, description)
                print(f"Task created with ID {task.task_id}")

            # LIST TASKS
            elif choice == "2":
                tasks = manager.list_tasks()
                if not tasks:
                    print("No tasks available.")
                else:
                    for task in tasks:
                        print(task)

            # UPDATE TASK STATUS
            elif choice == "3":
                try:
                    task_id = int(input("Enter task ID: "))
                except ValueError:
                    print("Task ID must be a number.")
                    continue

                print("Select new status:")
                print("1. TODO")
                print("2. IN_PROGRESS")
                print("3. COMPLETED")

                status_choice = input("Enter choice: ").strip()
                status_map = {
                    "1": TaskStatus.TODO,
                    "2": TaskStatus.IN_PROGRESS,
                    "3": TaskStatus.COMPLETED
                }

                if status_choice not in status_map:
                    print("Invalid status selection.")
                    continue

                manager.update_task_status(task_id, status_map[status_choice])
                print("Task status updated successfully.")

            # DELETE TASK
            elif choice == "4":
                try:
                    task_id = int(input("Enter task ID to delete: "))
                except ValueError:
                    print("Task ID must be a number.")
                    continue

                manager.delete_task(task_id)
                print("Task deleted successfully.")

            # EXIT
            elif choice == "5":
                print("Exiting TaskFlow.")
                break

            else:
                print("Invalid menu option.")

        except ValueError as ve:
            print(f"Error: {ve}")
        except KeyError as ke:
            print(f"Error: {ke}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
