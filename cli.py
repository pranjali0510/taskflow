import argparse

from task_manager import TaskManager
from status import TaskStatus


def main():

    manager = TaskManager()

    parser = argparse.ArgumentParser(
        description="TaskFlow - Task Management System"
    )

    subparsers = parser.add_subparsers(dest="command")

    # ---------------- ADD ----------------

    add_parser = subparsers.add_parser(
        "add", help="Create new task"
    )

    add_parser.add_argument(
        "title", help="Task title"
    )

    add_parser.add_argument(
        "--desc", default="", help="Task description"
    )

    # ---------------- LIST ----------------

    subparsers.add_parser(
        "list", help="Show all tasks"
    )

    # ---------------- DELETE ----------------

    delete_parser = subparsers.add_parser(
        "delete", help="Delete task"
    )

    delete_parser.add_argument(
        "id", type=int, help="Task ID"
    )

    # ---------------- STATUS ----------------

    status_parser = subparsers.add_parser(
        "status", help="Update status"
    )

    status_parser.add_argument(
        "id", type=int, help="Task ID"
    )

    status_parser.add_argument(
        "new_status",
        choices=[s.name.lower() for s in TaskStatus],
        help="New status"
    )

    args = parser.parse_args()

    try:

        # ADD
        if args.command == "add":

            task = manager.create_task(
                args.title,
                args.desc
            )

            print(f"✅ Created task {task.task_id}")

        # LIST
        elif args.command == "list":

            tasks = manager.list_tasks()

            if not tasks:
                print("No tasks found.")
                return

            print("\nID | Title | Status")
            print("-" * 35)

            for t in tasks:
                print(
                    f"{t.task_id} | {t.title} | {t.status.value}"
                )

        # DELETE
        elif args.command == "delete":

            manager.delete_task(args.id)

            print("🗑️ Task deleted")

        # STATUS
        elif args.command == "status":

            status = TaskStatus[
                args.new_status.upper()
            ]

            manager.update_task_status(
                args.id,
                status
            )

            print("✅ Status updated")

        else:
            parser.print_help()

    except Exception as e:

        print("❌ Error:", e)


if __name__ == "__main__":
    main()
