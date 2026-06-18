-- 1. Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS sales_dashboard;

-- 2. Tell MySQL to use this database
USE sales_dashboard;

-- 3. Create the sales table
CREATE TABLE IF NOT EXISTS sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    category VARCHAR(100),
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    sale_date DATE NOT NULL
);

-- 4. Insert some mock sales data to play with
INSERT INTO sales (product_name, category, quantity, price, sale_date) VALUES
('Laptop', 'Electronics', 2, 999.99, '2026-06-10'),
('Wireless Mouse', 'Electronics', 5, 25.50, '2026-06-11'),
('Gaming Chair', 'Furniture', 1, 199.99, '2026-06-12'),
('Coffee Mug', 'Kitchen', 10, 12.00, '2026-06-12'),
('Mechanical Keyboard', 'Electronics', 3, 85.00, '2026-06-13'),
('Desk Mat', 'Office', 4, 15.00, '2026-06-14'),
('Smart Watch', 'Electronics', 2, 150.00, '2026-06-15');