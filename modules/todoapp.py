"""A todoapp that runs on the command line."""

import json
from pathlib import Path

from modules.task import Task
from modules.helper_functions import check_for_errors, check_quit_protocol

class ToDoApp():
    """A simple CLI representation of a todoapp."""

    def __init__(self):
        self.tasks = []
        self.load()
    
    def show_todo_list(self):
        """Show the to do list."""
        if self.tasks:
            for task in self.tasks:
                print(task.id, task.title, task.completed)
        else:
            print("______No tasks yet______")

    def add_task(self):
        """Add a task to the to do list."""

        task = input("Enter the task you want to add: ")
        # Check for 'q' response.
        check_quit_protocol(task)

        # Add object to tasks list
        id = len(self.tasks) + 1
        task = Task(id, task, False)
        self.tasks.append(task)
        self.save()

        print(f"ADDED TASK: {task.title}")
        

    def edit_task(self):
        """Edit a task at index:task_number in the to do list."""

        # Check for valid input using check_for_errors function. 
        question = "\nEnter the id of the task you want to edit: "
        id = check_for_errors(question, self.tasks)

        edit = input("Enter your edit: ")
        # Check for 'q' response.
        check_quit_protocol(edit)
        
        # The task is at index-1 to compensate python's off-by-one behavior.
        for task in self.tasks:
            if task.id == id:
                task.title = edit
        
        self.save()
        print(f"EDITED TO: {edit}")

    def finish_task(self):
        """Move task at index:task_number from to do list to completed tasks."""

        # Check for valid input using check_for_errors function. 
        question = "Enter the id of the task you finished: "
        id = check_for_errors(question, self.tasks)

        # The task is at index-1 to compensate python's off-by-one behavior.
        for task in self.tasks:
            if task.id == id:
                print(f"FINISHED TASK: {task.title}")
                self.tasks.remove(task)
                break

        self.save()
        
    def delete_task(self):
        """Delete task at index:id from our to do list."""
        # Check for valid input using check_for_errors function. 
        question = "Enter the id of the task you want deleted: "
        id = check_for_errors(question, self.tasks)

        # The task is at index-1 to compensate python's off-by-one behavior.
        for task in self.tasks:
            if task.id == id:
                print(f"DELETED: {task.title}")
                self.tasks.remove(task)
                break
        
        self.save()
    
    def clear_todos(self):
        """Delete all tasks in the to do list."""
        self.tasks = []
        self.save()

        print("TO DO LIST HAS BEEN CLEARED")
    
    # Saving data through json serialization 
    def save(self):
        with open("todos.json", "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f)

    # Retrieving data through deserialization
    def load(self):
        path = Path("todos.json")
        if path.exists():
            with open("todos.json", "r") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = []
                else:
                    self.tasks = [Task.from_dict(d) for d in data]
        else:
            # If no file at given file path, return an empty list.
            self.tasks = []
 