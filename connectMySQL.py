import pymysql

# 1. mysql 연결
conn = pymysql.connect(host='127.0.0.1', user='root', password='12345', db='Schedule', charset='utf8')

# 2. 커서 생성하기
cur = conn.cursor()

# 3. 테이블 만들기 - 0이 나오면 잘 되는 것
cur.execute("CREATE TABLE userTable (id char(4), userName char(15), email char(20), birthYear int)" )

# 4. 데이터 입력하기 - 1이 나오면 잘 되는 것
cur.execute("INSERT INTO userTable VALUES('hong', '홍지윤', 'hong@naver.com', 1996)")
cur.execute("INSERT INTO userTable VALUES('kim', '김태연', 'kim@daum.com', 2011)")
cur.execute("INSERT INTO userTable VALUES('star', '별사랑', 'star@paran.com', 1990)")
cur.execute("INSERT INTO userTable VALUES('yang', '양지은', 'yang@gmail.com', 1993)")

# 5. 입력한 데이터 저장하기
conn.commit()

# 6. MySQL 연결 종료하기
conn.close()