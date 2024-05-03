class Task:
    def __init__(self, description, deadline, priority):
        self.description = description
        self.deadline = deadline
        self.priority = priority

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def show_tasks(self):
        for task in self.tasks:
            print(f"Description: {task.description}, Deadline: {task.deadline}, Priority: {task.priority}")

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.todo_list = ToDoList()

    def add_task(self, task):
        self.todo_list.add_task(task)

    def remove_task(self, task):
        self.todo_list.remove_task(task)

    def show_tasks(self):
        self.todo_list.show_tasks()

# 사용 예시
if __name__ == "__main__":
    user1 = User("user1", "password123")

    task1 = Task("Study for exam", "2024-04-14", "High")
    task2 = Task("Grocery shopping", "2024-04-12", "Medium")
    task3 = Task("Call mom", "2024-04-11", "Low")

    user1.add_task(task1)
    user1.add_task(task2)
    user1.add_task(task3)

    user1.show_tasks()
