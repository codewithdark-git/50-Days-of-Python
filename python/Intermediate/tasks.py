import json
import os

class Task:
    """A class representing a task."""
    def __init__(self, title, due_date=None, priority="Medium", category="General"):
        self.title = title
        self.completed = False
        self.due_date = due_date
        self.priority = priority
        self.category = category

    def to_dict(self):
        """Convert the task to a dictionary."""
        return {
            "title": self.title,
            "completed": self.completed,
            "due_date": self.due_date,
            "priority": self.priority,
            "category": self.category
        }

    @staticmethod
    def from_dict(data):
        """Create a Task instance from a dictionary."""
        task = Task(data["title"], data.get("due_date"), data.get("priority"), data.get("category"))
        task.completed = data["completed"]
        return task


class TaskManager:
    """A class to manage tasks."""
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Load tasks from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                try:
                    data = json.load(file)
                    return [Task.from_dict(task) for task in data]
                except json.JSONDecodeError:
                    return []
        return []

    def save_tasks(self):
        """Save tasks to a JSON file."""
        with open(self.filename, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, title, due_date=None, priority="Medium", category="General"):
        """Add a new task."""
        self.tasks.append(Task(title, due_date, priority, category))
        self.save_tasks()

    def remove_task(self, title):
        """Remove a task by title."""
        self.tasks = [task for task in self.tasks if task.title != title]
        self.save_tasks()

    def mark_task_complete(self, title):
        """Mark a task as completed."""
        for task in self.tasks:
            if task.title == title:
                task.completed = True
        self.save_tasks()

    def list_tasks(self, completed=None):
        """List tasks with an optional filter (completed or not)."""
        filtered_tasks = self.tasks
        if completed is not None:
            filtered_tasks = [task for task in self.tasks if task.completed == completed]

        for task in filtered_tasks:
            status = "✓" if task.completed else "✗"
            print(f"{status} {task.title} (Priority: {task.priority}, Due: {task.due_date}, Category: {task.category})")

    def search_tasks(self, keyword):
        """Search for tasks by title."""
        results = [task for task in self.tasks if keyword.lower() in task.title.lower()]
        for task in results:
            print(f"- {task.title} (Priority: {task.priority}, Due: {task.due_date})")

    def sort_tasks(self, by="priority"):
        """Sort tasks using lambda functions."""
        if by == "priority":
            self.tasks.sort(key=lambda task: task.priority)
        elif by == "due_date":
            self.tasks.sort(key=lambda task: task.due_date or "")
        self.list_tasks()


# CLI for the Task Manager
def main():
    manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task Complete")
        print("4. List Tasks")
        print("5. Search Tasks")
        print("6. Sort Tasks")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Task title: ")
            due_date = input("Due date (optional): ") or None
            priority = input("Priority (Low/Medium/High): ") or "Medium"
            category = input("Category (optional): ") or "General"
            manager.add_task(title, due_date, priority, category)

        elif choice == "2":
            title = input("Task title to remove: ")
            manager.remove_task(title)

        elif choice == "3":
            title = input("Task title to mark as complete: ")
            manager.mark_task_complete(title)

        elif choice == "4":
            completed_filter = input("Show (all/completed/incomplete): ").lower()
            completed = None if completed_filter == "all" else (completed_filter == "completed")
            manager.list_tasks(completed)

        elif choice == "5":
            keyword = input("Enter search keyword: ")
            manager.search_tasks(keyword)

        elif choice == "6":
            sort_by = input("Sort by (priority/due_date): ").lower()
            manager.sort_tasks(sort_by)

        elif choice == "7":
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
