# task_manager.py
from task import Task
from status import TaskStatus
from storage import save_tasks, load_tasks

class TaskManager:
    def __init__(self):
        # Load tasks from disk on startup
        self.tasks = load_tasks()
        self.next_task_id = (
            max(self.tasks.keys()) + 1 if self.tasks else 1
        )

    def create_task(self, title: str, description: str = "") -> Task:
        task = Task(self.next_task_id, title, description)
        self.tasks[self.next_task_id] = task
        self.next_task_id += 1
        save_tasks(self.tasks)
        return task

    def get_task(self, task_id: int) -> Task:
        if task_id not in self.tasks:
            raise KeyError(f"Task with ID {task_id} not found")
        return self.tasks[task_id]

    def delete_task(self, task_id: int):
        if task_id not in self.tasks:
            raise KeyError(f"Task with ID {task_id} not found")
        del self.tasks[task_id]
        save_tasks(self.tasks)

    def list_tasks(self):
        return list(self.tasks.values())

    def update_task_status(self, task_id: int, new_status: TaskStatus):
        task = self.get_task(task_id)
        task.update_status(new_status)
        save_tasks(self.tasks)
