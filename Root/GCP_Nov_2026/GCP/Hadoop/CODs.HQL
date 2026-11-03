HQL


CREATE DATABASE [IF NOT EXISTS] training;

CREATE SCHEMA userdb;

SHOW DATABASES;

CREATE TABLE users (
    user_id INT PRIMARY KEY,          -- Proper PK
    name VARCHAR(100 NULL,              -- Required relationship
    age DECIMAL(10,2) NOT NULL,      -- age value
    region VARCHAR(20) DEFAULT 'new',  -- Controlled default
    FOREIGN KEY (user_id) REFERENCES users(user_id)  -- Enforce relationship
);



CREATE TABLE IF NOT EXISTS managed_user (
    name VARCHAR(100 NULL,              -- Required relationship
    age DECIMAL(10,2) NOT NULL,      -- age value
    region VARCHAR(20) DEFAULT 'new',  -- Controlled default
    FOREIGN KEY (user_id) REFERENCES users(user_id)  -- Enforce relationship
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;   



-- Load from local file system
LOAD DATA LOCAL INPATH '/path/to/local/user.csv' OVERWRITE INTO TABLE managed_user;

-- Load from HDFS
LOAD DATA INPATH '/user/hdfs/user.csv' OVERWRITE INTO TABLE managed_user;   



SELECT region, aggregate_function(column_name)
FROM table_name
GROUP BY region;   
