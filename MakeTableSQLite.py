import sqlite3

# SQLite 데이터베이스에 연결
conn = sqlite3.connect('example.db')

# 외래 키 제약 조건 활성화
conn.execute('PRAGMA foreign_keys = ON;')

# 커서 생성
cur = conn.cursor()

# users 테이블 생성
cur.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    password CHAR(30),
    email CHAR(25),
    phone_number CHAR(15),
    name CHAR(15)
)
''')

# tasks 테이블 생성
cur.execute('''
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    detail TEXT,
    priority INTEGER,
    startTime TEXT,
    excutionTime TEXT,
    status TEXT CHECK(status IN ('Todo', 'In Progress', 'Done')),
    FOREIGN KEY (user_id) REFERENCES users(id)
)
''')

# 연결 종료
conn.close()
