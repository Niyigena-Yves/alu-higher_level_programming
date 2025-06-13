-- Retrieves all cities from the database hbtn_0d_usa
-- Selects all rows from specific columns in the database
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.state_id ORDER BY cities.id;
