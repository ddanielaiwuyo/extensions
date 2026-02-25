DROP TABLE IF EXISTS test_shows;

CREATE TABLE IF NOT EXISTS test_shows (
	id SERIAL PRIMARY KEY NOT NULL,
	name TEXT NOT NULL,
	rating INT NOT NULL
);

INSERT INTO test_shows(name, rating) 
VALUES ('Invincible', 9),
('Demolition', 10), ('Better Call Saul', 10);
