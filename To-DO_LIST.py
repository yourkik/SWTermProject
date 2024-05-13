import datetime as dt

class Task:
    def __init__(self, description, deadline, priority):
        self.description = description
        self.deadline = deadline
        self.priority = priority
        self.deleted = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def delete_task(self, task):
        task.deleted = True

    def restore_task(self, task):
        task.deleted = False

    def show_tasks(self):

        sorted_tasks = sorted(self.tasks, key=lambda task: task.deadline)

        for task in sorted_tasks:
            if not task.deleted: 
                print(f"Description: {task.description}, Deadline: {task.deadline}, Priority: {task.priority}")

    def check_schedule_and_notify(self):
        now = dt.datetime.now()
        for task in self.tasks:
            if not task.deleted and task.deadline - now <= dt.timedelta(hours=1):
                print(f"Notification: Your task '{task.description}' is starting soon.")

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.todo_list = ToDoList()

    def add_task(self, task):
        self.todo_list.add_task(task)

    def remove_task(self, task):
        self.todo_list.remove_task(task)

    def delete_task(self, task):
        self.todo_list.delete_task(task)

    def restore_task(self, task):
        self.todo_list.restore_task(task)

    def show_tasks(self):
        self.todo_list.show_tasks()

# 사용 예시
if __name__ == "__main__":
    user1 = User("user1", "password123")

    now = dt.datetime.now()

    task1 = Task("Study for exam", now + dt.timedelta(hours=2), "High")
    task2 = Task("Grocery shopping", now + dt.timedelta(hours=1), "Medium")
    task3 = Task("Call mom", now + dt.timedelta(days=1), "Low")

    user1.add_task(task1)
    user1.add_task(task2)
    user1.add_task(task3)

    user1.delete_task(task2)  # task2를 휴지통으로 이동

    user1.show_tasks()  # task2는 표시되지 않음

    user1.restore_task(task2)  # task2를 복원

    user1.show_tasks()

    user1.todo_list.check_schedule_and_notify()
