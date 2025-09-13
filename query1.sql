CREATE SCHEMA IF NOT EXISTS sandbox;

CREATE TABLE IF NOT EXISTS sandbox.sales (
    id SERIAL PRIMARY KEY,
    sale_date DATE,
    product TEXT,
    region TEXT,
    quantity INT,
    price NUMERIC(10,2)
);

INSERT INTO sandbox.sales (sale_date, product, region, quantity, price) VALUES
('2025-09-01','Laptop','West',3,1200.00),
('2025-09-02','Phone','East',5,800.00),
('2025-09-02','Tablet','West',2,500.00),
('2025-09-03','Laptop','East',1,1200.00),
('2025-09-03','Phone','West',4,800.00);
