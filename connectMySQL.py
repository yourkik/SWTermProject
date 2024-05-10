import pymysql
import uuid

def insert_task(cur, user_id, detail, priority, status):
    sql = "INSERT INTO tasks (user_id, detail, priority, status) VALUES (%s, %s, %s, %s)"
    val = (user_id, detail, priority, status)
    cur.execute(sql, val)

def insert_daily_plan(cur, user_id, date, task_id, start_time, end_time):
    sql = "INSERT INTO daily_plans (user_id, date, task_id, start_time, end_time) VALUES (%s, %s, %s, %s, %s)"
    val = (user_id, date, task_id, start_time, end_time)
    cur.execute(sql, val)

def insert_project_plan(cur, user_id, project_id, description, is_public):
    sql = "INSERT INTO project_plans (user_id, project_id, description, is_public) VALUES (%s, %s, %s, %s)"
    val = (user_id, project_id, description, is_public)
    cur.execute(sql, val)

def insert_notification(cur, user_id, message, is_read, datetime):
    sql = "INSERT INTO notifications (user_id, message, is_read, datetime) VALUES (%s, %s, %s, %s)"
    val = (user_id, message, is_read, datetime)
    cur.execute(sql, val)

#start
#mysql 연결
conn = pymysql.connect(host='127.0.0.1', user='root', password='12345', db='Schedule', charset='utf8')

#커서 생성하기
cur = conn.cursor()

#테이블 만들기 - 0이 나오면 잘 되는 것
#테이블 생성 전에 테이블이 존재하는지 확인
cur.execute("SHOW TABLES LIKE 'users'")
exists = cur.fetchone()

#테이블이 존재하지 않으면 테이블 생성
if not exists:
    cur.execute("CREATE TABLE users (user_id int(20) PRIMARY KEY, userName char(20), email char(30), birth int(8))")

#데이터 입력하기 - 1이 나오면 잘 되는 것
#cur.execute("INSERT INTO users VALUES(1, '홍지윤', 'hong@naver.com', 19960410)")
#cur.execute("INSERT INTO users VALUES(2, '김태연', 'kim@daum.com', 20110229)")
#cur.execute("INSERT INTO users VALUES(3, '별사랑', 'star@paran.com', 19901118)")
#cur.execute("INSERT INTO users VALUES(4, '양지은', 'yang@gmail.com', 19931223)")

insert_task(cur, 1, 'test', 2, 'Todo')

#입력한 데이터 저장하기
conn.commit()

#MySQL 연결 종료하기
conn.close()