from enum import Enum
class TaskStatus(Enum):
    TODO = "To Do"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    BLOCKED = "Blocked"
    @ classmethod
    def all_statuses(cls):
        return [cls.TODO, cls.IN_PROGRESS, cls.COMPLETED, cls.BLOCKED]
    
class TaskPriority:
    HIGH = 1
    MEDIUM = 2
    LOW = 3
    @classmethod
    def all_priorities(cls):
        return [cls.HIGH, cls.MEDIUM, cls.LOW]
