--  creates the table unique_id on your MySQL server.
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1, unique (ID), name VARCHAR(256)
 );
