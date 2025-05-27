-- Creates the database hbtn_0d_usa and the table states within it on your MySQL server
-- Create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Select the database for use
USE hbtn_0d_usa;
-- Create the table
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
