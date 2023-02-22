-- 1
CREATE TABLE users(
userID INT NOT NULL auto_increment,
first_name VARCHAR(20) NOT NULL,
last_name VARCHAR(20) NOT NULL,
birthday DATE NOT NULL,
city VARCHAR(100),
country VARCHAR(100),
email VARCHAR(100),
created_at datetime
PRIMARY KEY (userId)
);

-- 괄호를 닫았는데 왜 인식을 못하냐..


-- 2
UPDATE users
set 
first_name = Beemo,
last_name = Jeong,
birthday = 1000-01-01,
email = beemo@hphk.kr
WHERE userid = 1

