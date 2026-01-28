# task.py
from datetime import datetime
from status import TaskStatus


class Task:

    def __init__(
        self,
        task_id: int,
        title: str,
        description: str = "",
        status: TaskStatus = TaskStatus.TODO,
        created_at: datetime | None = None
    ):

        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status
        self.created_at = created_at or datetime.now()

    def update_status(self, new_status: TaskStatus):

        if not self._is_valid_transition(new_status):

            raise ValueError(
                f"Invalid state transition from "
                f"{self.status.value} to {new_status.value}"
            )

        self.status = new_status

    def _is_valid_transition(self, new_status: TaskStatus) -> bool:

        if self.status == TaskStatus.TODO and new_status == TaskStatus.IN_PROGRESS:
            return True

        if self.status == TaskStatus.IN_PROGRESS and new_status == TaskStatus.COMPLETED:
            return True

        return False

    # ----------------- JSON SUPPORT -----------------

    def to_dict(self):

        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "status": self.status.name,
            "created_at": self.created_at.isoformat()
        }

    @staticmethod
    def from_dict(data):

        return Task(
            task_id=data["task_id"],
            title=data["title"],
            description=data.get("description", ""),
            status=TaskStatus[data["status"]],
            created_at=datetime.fromisoformat(data["created_at"])
        )

    # ----------------- DISPLAY -----------------

    def __str__(self):

        return (
            f"[ID: {self.task_id}] "
            f"{self.title} | "
            f"Status: {self.status.value} | "
            f"Created: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
        )
