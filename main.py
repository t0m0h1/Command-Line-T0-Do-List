import json
import os
import tkinter as tk



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
        self.root.title = "To-Do-List App"
        self.root.geometry("600x600")
        self.root.resizable(False, False)

        # input frame
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=10)

        # input fields
        self.name_label = tk.Label(self.input_frame, text="Name: ")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.input_frame)
        self.name_entry.pack()

        # label fields
        self.title_label = tk.Label(self.input_frame, text="Title: ")
        self.title_label.pack()
        self.title_entry = tk.Entry(self.input_frame)
        self.title_entry.pack()

        # description fields
        self.description_label = tk.Label(self.input_frame, text="Description: ")
        self.description_label.pack()
        self.description_entry = tk.Entry(self.input_frame)
        self.description_entry.pack()

        # due date fields
        self.due_date_label = tk.Label(self.input_frame, text="Due Date: MM/DD/YYYY")
        self.due_date_label.pack()
        self.due_date_entry = tk.Entry(self.input_frame)
        self.due_date_entry.pack()

        # add task button
        self.add_task_button = tk.Button(self.input_frame, text="Add Task", command=self.add_task)
        self.add_task_button.pack()

        # main frame
        root.mainloop()


    def add_task(self):
        name = self.name_entry.get()
        title = self.title_entry.get()
        description = self.description_entry.get()
        due_date = self.due_date_entry.get()

        task = Task(name, title, description, due_date)
        self.task_manager.add_task(task)
        print("Task added successfully.")

        self.name_entry.delete(0, tk.END)
        self.title_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.due_date_entry.delete(0, tk.END)

        tasks = self.task_manager.get_tasks() # get all tasks
        for task in tasks:
            if task.completed:
                status = "Completed"
            else:
                status = "Pending"



    # placeholder 
    def remove_task(self):
        pass









if __name__ == "__main__":
    root = tk.Tk()
    task_app = TaskApp(root)


# if __name__ == "__main__":
#     task_manager = TaskManager()
    
#     while True:
#         print("\nTask Manager")
#         print("1. Add Task")
#         print("2. Remove Task")
#         print("3. List Tasks")
#         print("4. Mark Task as Completed")
#         print("5. Exit")

#         choice = input("Enter your choice: ")
        
#         if choice == "1":
#             task = task_manager.input_task()
#             task_manager.add_task(task)
#             print("Task added successfully.")
        
#         elif choice == "2":
#             task_name = input("Enter the task name to remove: ")
#             task_to_remove = task_manager.task_list.find_task_by_name(task_name)
#             if task_to_remove:
#                 task_manager.remove_task(task_to_remove)
#                 print("Task removed successfully.")
#             else:
#                 print("Task not found.")
        
#         elif choice == "3":
#             tasks = task_manager.get_tasks()
#             if not tasks:
#                 print("No tasks available.")
#             else:
#                 for task in tasks:
#                     status = "Completed" if task.completed else "Pending"
#                     print(f"Name: {task.name}, Title: {task.title}, Description: {task.description}, Due Date: {task.due_date}, Status: {status}")
        
#         elif choice == "4":
#             task_name = input("Enter the task name to mark as completed: ")
#             task_to_mark = task_manager.task_list.find_task_by_name(task_name)
#             if task_to_mark:
#                 task_to_mark.mark_completed()
#                 task_manager.save_tasks()
#                 print("Task marked as completed.")
#             else:
#                 print("Task not found.")
        
#         elif choice == "5":
#             print("Exiting Task Manager.")
#             break
        
#         else:
#             print("Invalid choice. Please try again.")
