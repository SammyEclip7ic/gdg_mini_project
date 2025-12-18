# Task object that acts as a model for a task

class Task:
    def __init__(self, id, title, completed):
        self.id = id
        self.title = title
        self.completed = completed
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["title"],
            data["completed"]
        )
