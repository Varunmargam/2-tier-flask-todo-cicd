CREATE DATABASE IF NOT EXISTS to_do;

USE to_do;

CREATE TABLE IF NOT EXISTS tasks (
    id INT PRIMARY KEY AUTO_INCREMENT,
    task VARCHAR(255) NOT NULL
);
