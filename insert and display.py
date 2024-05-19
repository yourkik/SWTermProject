import sqlite3

# SQLite 데이터베이스에 연결
conn = sqlite3.connect('example.db')

# 외래 키 제약 조건 활성화
conn.execute('PRAGMA foreign_keys = ON;')

# 커서 생성
cur = conn.cursor()

def insert_user(password, email, phone_number, name):
    cur.execute('''
    INSERT INTO users (password, email, phone_number, name)
    VALUES (?, ?, ?, ?)
    ''', (password, email, phone_number, name))
    conn.commit()


def fetch_all_users():
    cur.execute('SELECT * FROM users')
    rows = cur.fetchall()
    return rows

# 데이터 삽입 및 조회 등 작업 수행
insert_user(1111,'swTerm', '010-2222-3333',"John")
users = fetch_all_users()
for user in users:
    print(user)

# 연결 종료
conn.close()