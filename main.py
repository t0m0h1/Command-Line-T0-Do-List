import json
import os
import tkinter as tk
from tkinter import messagebox


class Task:
    def __init__(self, name, title, description, due_date):
        self.name = name
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def set_due_date(self, due_date):
        self.due_date = due_date

    def get_due_date(self):
        return self.due_date

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {
            "name": self.name,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, task_dict):
        task = cls(task_dict["name"], task_dict["title"], task_dict["description"], task_dict["due_date"])
        if task_dict.get("completed"):
            task.mark_completed()
        return task


class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def get_tasks(self):
        return self.tasks

    def find_task_by_name(self, name):
        for task in self.tasks:
            if task.name == name:
                return task
        return None

    def to_dict(self):
        return [task.to_dict() for task in self.tasks]

    def from_dict(self, tasks_dict):
        self.tasks = [Task.from_dict(task) for task in tasks_dict]


class TaskManager:
    def __init__(self):
        self.task_list = TaskList()
        self.load_tasks()

    def add_task(self, task):
        self.task_list.add_task(task)
        self.save_tasks()

    def remove_task(self, task):
        self.task_list.remove_task(task)
        self.save_tasks()

    def get_tasks(self):
        return self.task_list.get_tasks()

    def input_task(self):
        name = input("Enter the task name: ")
        title = input("Enter the task title: ")
        description = input("Enter the task description: ")
        due_date = input("Enter the task due date (YYYY-MM-DD): ")
        return Task(name, title, description, due_date)

    def save_tasks(self):
        with open('tasks.json', 'w') as file:
            json.dump(self.task_list.to_dict(), file)

    def load_tasks(self):
        if os.path.exists('tasks.json'):
            with open('tasks.json', 'r') as file:
                tasks_dict = json.load(file)
                self.task_list.from_dict(tasks_dict)


class TaskApp:
    def __init__(self, root):
        self.task_manager = TaskManager()
        self.root = root
        self.root.title("To-Do-List App")
        self.root.geometry("600x600")
        self.root.resizable(False, False)

        # Input frame
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=10)

        # Input fields
        self.name_label = tk.Label(self.input_frame, text="Name: ")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.input_frame)
        self.name_entry.pack()

        self.title_label = tk.Label(self.input_frame, text="Title: ")
        self.title_label.pack()
        self.title_entry = tk.Entry(self.input_frame)
        self.title_entry.pack()

        self.description_label = tk.Label(self.input_frame, text="Description: ")
        self.description_label.pack()
        self.description_entry = tk.Entry(self.input_frame)
        self.description_entry.pack()

        self.due_date_label = tk.Label(self.input_frame, text="Due Date: YYYY-MM-DD")
        self.due_date_label.pack()
        self.due_date_entry = tk.Entry(self.input_frame)
        self.due_date_entry.pack()

        self.add_task_button = tk.Button(self.input_frame, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=10)

        # Task list frame
        self.task_list_frame = tk.Frame(self.root)
        self.task_list_frame.pack(pady=20)

        self.tasks_label = tk.Label(self.task_list_frame, text="Tasks:")
        self.tasks_label.pack()

        self.task_listbox = tk.Listbox(self.task_list_frame, width=80, height=15)
        self.task_listbox.pack()

        self.remove_task_button = tk.Button(self.task_list_frame, text="Remove Task", command=self.remove_task)
        self.remove_task_button.pack(pady=10)

        self.display_tasks()

        self.root.mainloop()

    def add_task(self):
        name = self.name_entry.get()
        title = self.title_entry.get()
        description = self.description_entry.get()
        due_date = self.due_date_entry.get()

        if not (name and title and description and due_date):
            messagebox.showerror("Error", "All fields must be filled out.")
            return

        task = Task(name, title, description, due_date)
        self.task_manager.add_task(task)
        self.display_tasks()

        self.name_entry.delete(0, tk.END)
        self.title_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.due_date_entry.delete(0, tk.END)

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if not selected_task_index:
            messagebox.showerror("Error", "No task selected.")
            return

        task_name = self.task_listbox.get(selected_task_index).split(" - ")[0]
        task_to_remove = self.task_manager.task_list.find_task_by_name(task_name)
        if task_to_remove:
            self.task_manager.remove_task(task_to_remove)
            self.display_tasks()
        else:
            messagebox.showerror("Error", "Task not found.")

    def display_tasks(self):
        self.task_listbox.delete(0, tk.END)
        tasks = self.task_manager.get_tasks()
        for task in tasks:
            status = "Completed" if task.completed else "Pending"
            self.task_listbox.insert(tk.END, f"{task.name} - {task.title} - {task.description} - {task.due_date} - {status}")


if __name__ == "__main__":
    root = tk.Tk()
    task_app = TaskApp(root)
