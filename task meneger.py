# Python Project: Task Manager

# Description:
# This is a simple task manager application that allows users to create, view, update, and delete tasks. 
# Tasks have attributes such as title, description, due date, and status.

# Import necessary libraries
import datetime

# Define the Task class
class Task:
    def __init__(self, title, description, due_date, status="Pending"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nStatus: {self.status}"

# Task Manager class
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"\nTask {i}:")
                print(task)

    def update_task(self, index, title=None, description=None, due_date=None, status=None):
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            if title:
                task.title = title
            if description:
                task.description = description
            if due_date:
                task.due_date = due_date
            if status:
                task.status = status
            print("Task updated successfully!")
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            print("Task deleted successfully!")
        else:
            print("Invalid task index.")

# Main function
def main():
    manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter task due date (YYYY-MM-DD): ")
            try:
                due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()
                task = Task(title, description, due_date)
                manager.add_task(task)
            except ValueError:
                print("Invalid date format. Please try again.")

        elif choice == "2":
            manager.view_tasks()

        elif choice == "3":
            index = int(input("Enter task index to update: ")) - 1
            title = input("Enter new title (leave blank to keep current): ")
            description = input("Enter new description (leave blank to keep current): ")
            due_date = input("Enter new due date (YYYY-MM-DD, leave blank to keep current): ")
            status = input("Enter new status (leave blank to keep current): ")

            try:
                due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d").date() if due_date else None
            except ValueError:
                print("Invalid date format. Please try again.")
                continue

            manager.update_task(index, title, description, due_date, status)

        elif choice == "4":
            index = int(input("Enter task index to delete: ")) - 1
            manager.delete_task(index)

        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
