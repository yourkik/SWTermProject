create database schedule;
use schedule;

select * from users;

CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    detail TEXT,
    priority INT,
    status ENUM('Todo', 'In Progress', 'Done'),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
select * from tasks;

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
