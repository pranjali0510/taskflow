# storage.py
import json
import os
from task import Task
from status import TaskStatus
from datetime import datetime

# Always resolve path relative to this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "tasks.json")

def save_tasks(tasks: dict):
    print(f"[DEBUG] Saving tasks to: {FILE_PATH}")  # <-- ADD THIS
    data = []
    for task in tasks.values():
        data.append({
            "task_id": task.task_id,
            "title": task.title,
            "description": task.description,
            "status": task.status.value,
            "created_at": task.created_at.isoformat()
        })

    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)

def load_tasks() -> dict:
    try:
        with open(FILE_PATH, "r") as f:
            data = json.load(f)

        tasks = {}
        for item in data:
            task = Task(
                task_id=item["task_id"],
                title=item["title"],
                description=item["description"]
            )
            task.status = TaskStatus(item["status"])
            task.created_at = datetime.fromisoformat(item["created_at"])
            tasks[task.task_id] = task

        return tasks

    except FileNotFoundError:
        return {}
