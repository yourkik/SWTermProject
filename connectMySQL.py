import pymysql

# 1. mysql 연결
conn = pymysql.connect(host='127.0.0.1', user='root', password='12345', db='Schedule', charset='utf8')

# 2. 커서 생성하기
cur = conn.cursor()

# 3. 테이블 만들기 - 0이 나오면 잘 되는 것
cur.execute("Drop table users")
cur.execute("CREATE TABLE users (user_id int(20) PRIMARY KEY, userName char(20), email char(30), birth int(8))" )

# 4. 데이터 입력하기 - 1이 나오면 잘 되는 것
cur.execute("INSERT INTO users VALUES(1, '홍지윤', 'hong@naver.com', 19960410)")
cur.execute("INSERT INTO users VALUES(2, '김태연', 'kim@daum.com', 20110229)")
cur.execute("INSERT INTO users VALUES(3, '별사랑', 'star@paran.com', 19901118)")
cur.execute("INSERT INTO users VALUES(4, '양지은', 'yang@gmail.com', 19931223)")

# 5. 입력한 데이터 저장하기
conn.commit()

# 6. MySQL 연결 종료하기
conn.close()