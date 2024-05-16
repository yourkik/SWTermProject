create database schedule;
use schedule;

select * from users;

create table users(
	id int auto_increment,
    password char(30),
    email char(25),
    phone_number char(15),
    name char(15),
    primary key(id, password)
);

CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    detail TEXT,
    priority INT,
    startTime datetime,
    excutionTime datetime,#여기에는 timedelta로 시간과 분만 들어감
    status ENUM('Todo', 'In Progress', 'Done'),#현재 여기서 상태를 구분하지만 휴지통을 따로 만들거랴면 startTime과 excutionTime을 계산해서 다 끝난 task를 따로 저장할 수 있음
    FOREIGN KEY (user_id) REFERENCES users(id)
);
select * from tasks;

/*
#task에서 따로 시간을 관리하는 table을 저장하는 ver, 시간의 변동이 많으면 task에 저장하는 것보다 효율적이라고 생각
create table taskTime(
	id int auto_increment primary key,
    task_id int,
    startTime datetime,
    excutionTime datetime,
    foreign key(task_id) references tasks(id)
)
*/

/*
불필요하다고 생각해 주석 처리함
CREATE TABLE daily_plans (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    date DATE,
    task_id INT,
    start_time TIME,
    end_time TIME,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (task_id) REFERENCES tasks(id)
);

CREATE TABLE project_plans (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    project_id INT,
    description TEXT,
    is_public BOOLEAN,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);


CREATE TABLE notifications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    message TEXT,
    is_read BOOLEAN,
    datetime DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
*/