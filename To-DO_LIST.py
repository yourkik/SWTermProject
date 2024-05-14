import datetime as dt

class Task:
    def __init__(self, description, deadline, priority):
        #태스크를 초기화 설명, 마감기한, 우선순위를 설정
        self.description = description
        self.deadline = deadline
        self.priority = priority
        self.deleted = False
        self.start_time = None  # 태스크 시작 시간

class ToDoList:
    def __init__(self):
        #할 일 목록을 초기화
        self.tasks = []
        self.work_start = dt.time(9, 0)  # 하루 작업 시작 시간
        self.work_end = dt.time(21, 0)  # 하루 작업 종료 시간
        self.unavailable_start = None  # 이용 불가 시작 시간 초기화
        self.unavailable_end = None  # 이용 불가 종료 시간 초기화

    def set_unavailable_hours(self, start_hour, start_minute, end_hour, end_minute):
        #이용 불가 시간을 설정, 유효성 검사 후 시간을 저장
        try:
            start_time = dt.time(start_hour, start_minute)
            end_time = dt.time(end_hour, end_minute)
            if start_time >= end_time:
                print("Error: End time must be later than start time.")
                return
            if start_time < self.work_start or end_time > self.work_end:
                print("Error: Unavailable hours must be within the working hours (09:00-21:00).")
                return
            self.unavailable_start = start_time
            self.unavailable_end = end_time
            print(f"Unavailable hours set from {self.unavailable_start} to {self.unavailable_end}.")
            self.plan_day()  # 새로운 이용 불가 시간으로 일정 재계획
        except ValueError as e:
            print("Invalid time input:", e)

    def add_task(self, task):
        #태스크를 추가하고 일정을 재계획
        self.tasks.append(task)
        self.plan_day()
        
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

    def plan_day(self):
        #태스크의 시작 시간을 이용 불가 시간을 고려해 계획
        today = dt.datetime.now().date()
        current_time = dt.datetime.combine(today, self.work_start)
        for task in self.tasks:
            if not task.deleted:
                if self.unavailable_start and self.unavailable_end:
                    if (current_time.time() >= self.unavailable_start and
                        current_time.time() < self.unavailable_end):
                        current_time = dt.datetime.combine(today, self.unavailable_end)
                
                if current_time.time() >= self.work_end:
                    today += dt.timedelta(days=1)
                    current_time = dt.datetime.combine(today, self.work_start)

                task.start_time = current_time
                current_time += dt.timedelta(hours=2)

class User:
    def __init__(self, username, password):
        #사용자 초기화/ 사용자 이름과 비밀번호를 설정
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

    def set_unavailable_hours(self, start_hour, start_minute, end_hour, end_minute):
        #사용자를 위한 여가 시간을 설정
        self.todo_list.set_unavailable_hours(start_hour, start_minute, end_hour, end_minute)

# 사용 예시
if __name__ == "__main__":
    user1 = User("user1", "password123")
    # 사용자가 필요에 따라 여가 시간을 설정할 수 있습니다.
    user1.set_unavailable_hours(13, 0, 15, 0)  # 사용자 지정 이용 불가 시간 설정

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
    # 태스크 및 일정 출력
    user1.show_tasks()

    user1.todo_list.check_schedule_and_notify();
