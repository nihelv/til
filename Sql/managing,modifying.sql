-- 1
CREATE TABLE posts(
postID INT NOT NULL AUTO_INCREMENT,
title varchar(50) NOT NULL,
content varchar(200) NOT NULL,
PRIMARY KEY (postID) 
);

-- 2
ALTER TABLE posts
ADD writer varchar(100),
ADD created_at datetime;

-- 3
ALTER TABLE posts
MODIFY content TEXT;

-- 4
ALTER TABLE posts
DROP COLUMN wpostspostsriter;

-- 5
DROP TABLE posts;

-- 6
SELECT IF( EXISTS(
	SELECT * FROM classicmoderls WHERE posts
    exec('DROP TABLE posts')
    GO
GO
CREATE TABLE posts (
postID INT NOT NULL AUTO_INCREMENT
title VARCHAR(50) NOT NULL
content TEXT NOT NULL
writer VARCHAR(20) NOT NULL
created_at DATETIME CURRENT_TIMESTAMP DEFAULT GENERATED