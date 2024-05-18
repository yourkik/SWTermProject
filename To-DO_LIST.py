import datetime as dt

class Task:
    def __init__(self, description, deadline, priority):
        self.description = description
        self.deadline = deadline
        self.priority = priority
        self.deleted = False

        # Project 공유 변수, 함수 추가
        self.assignee = None

    def assign_to(self, user):
        self.assignee = user

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

# Project 기능
class Project:
    def __init__(self, title, owner):
        self.title = title
        self.owner = owner
        self.tasks = []
        self.is_public = False
        self.comments = []
        self.viewers = [owner]

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
                assignee = task.assignee.username if task.assignee else "Unassigned"
                print(f"Description: {task.description}, Deadline: {task.deadline}, Priority: {task.priority}, Assignee: {assignee}")

    def toggle_public(self):
        self.is_public = not self.is_public

    def add_comment(self, user, comment):
        if self.is_public or user in self.viewers:
            self.comments.append((user.username, comment))
        else:
            print(f"{user.username} does not have permission to comment on this project.")

    def grant_access(self, user):
        if user not in self.viewers:
            self.viewers.append(user)

    def assign_task(self, task, user):
        if self.owner == user or user in self.viewers:
            task.assign_to(user)
        else:
            print(f"{user.username} does not have permission to be assigned this task.")

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.todo_list = ToDoList()
        self.projects = []

    def add_task(self, task):
        self.todo_list.add_task(task)

    def remove_task(self, task):
        self.todo_list.remove_task(task)

    def delete_task(self, task):
        self.todo_list.delete_task(task)

    def restore_task(self, task):
        self.todo_list.restore_task(task)

    # project 생성
    def create_project(self, title):
        project = Project(title, self)
        self.projects.append(project)
        return project

    def show_tasks(self):
        self.todo_list.show_tasks()

# 사용 예시
if __name__ == "__main__":
    user1 = User("user1", "password123")
    user2 = User("user2", "password456")

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

    # Project 생성 및 작업 할당
    project1 = user1.create_project("New Project")
    project1.add_task(task1)
    project1.add_task(task2)
    project1.toggle_public()  # 프로젝트를 공개로 설정
    project1.add_comment(user1, "Let's work on this project together!")
    project1.grant_access(user2)  # user2에게 접근 권한 부여
    project1.add_comment(user2, "I will handle the grocery shopping task.")
    project1.assign_task(task2, user2)

    print("\nProject Tasks:")
    project1.show_tasks()  # 프로젝트의 작업을 출력