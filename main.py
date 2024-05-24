class Task:
    def __init__(self, name, title, description, due_date):
        self.name = name
        self.title = title
        self.description = description
        self.due_date = due_date

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
    

class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def get_tasks(self):
        return self.tasks
    

class TaskManager:
    def __init__(self):
        self.task_list = TaskList()

    def add_task(self, task):
        self.task_list.add_task(task)

    def remove_task(self, task):
        self.task_list.remove_task(task)

    def get_tasks(self):
        return self.task_list.get_tasks()
    
    task = input("Enter the task: ")



if __name__ == "__main__":
    homework = Task("homework", "Math", "Do the math homework", "2021-10-10")
    
    


