-- Retrieves all the cities in California from the database hbtn_0d_usa
-- Selects all rows from a column in the database
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
