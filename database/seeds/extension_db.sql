DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS stock_items;

-- save prices as £12990 and 
-- transformed to 129.90 on application code
-- to avoid rounding errors
CREATE TABLE IF NOT EXISTS stock_items (
	id  SERIAL PRIMARY KEY NOT NULL,
	name TEXT NOT NULL,
	price INT NOT NULL, 
	quantity INT NOT NULL
);

CREATE TABLE IF NOT EXISTS orders (
	id SERIAL PRIMARY KEY NOT NULL,
	customer_name TEXT NOT NULL,
	quantity INT NOT NULL,
	total_price INT NOT NULL,
	purchased_at DATE NOT NULL,
	stock_id INT REFERENCES stock_items(id),
	created_at TIMESTAMP
);


INSERT INTO stock_items(name, price, quantity) 
VALUES ('Airpods', 40000, 103), 
('Sony Headphones', 80099, 300),
('El Cinco', 49999, 5),
('Mercedes Pen', 39999, 30);

INSERT INTO orders (
	customer_name, quantity, total_price, purchased_at, stock_id
) VALUES 
('Bill Evans', 1, 13999,  '2021-11-12', 3),
('Jonathan Blow', 3, 42000,'2026-04-25', 1);


