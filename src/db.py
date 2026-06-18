import mysql.connector
from mysql.connector import Error

def get_connection():
    """Establishes a connection to the MySQL server."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="@Yadavhr26"  
    )

def setup_database():
    """Creates the database, table, and inserts seed data."""
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # 1. Create Database
        cursor.execute("CREATE DATABASE IF NOT EXISTS sales_dashboard;")
        cursor.execute("USE sales_dashboard;")
        print("✅ Database 'sales_dashboard' ready.")

        # 2. Create Table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            id INT AUTO_INCREMENT PRIMARY KEY,
            product_name VARCHAR(255) NOT NULL,
            category VARCHAR(100),
            quantity INT NOT NULL,
            price DECIMAL(10, 2) NOT NULL,
            sale_date DATE NOT NULL
        );
        """)
        print("✅ Table 'sales' ready.")

        # 3. Check if data already exists to prevent duplication
        cursor.execute("SELECT COUNT(*) FROM sales;")
        if cursor.fetchone()[0] == 0:
            # Insert sample data
            sample_data = [
                ('Laptop', 'Electronics', 2, 999.99, '2026-06-10'),
                ('Wireless Mouse', 'Electronics', 5, 25.50, '2026-06-11'),
                ('Gaming Chair', 'Furniture', 1, 199.99, '2026-06-12'),
                ('Coffee Mug', 'Kitchen', 10, 12.00, '2026-06-12'),
                ('Mechanical Keyboard', 'Electronics', 3, 85.00, '2026-06-13'),
                ('Desk Mat', 'Office', 4, 15.00, '2026-06-14'),
                ('Smart Watch', 'Electronics', 2, 150.00, '2026-06-15')
            ]
            
            query = "INSERT INTO sales (product_name, category, quantity, price, sale_date) VALUES (%s, %s, %s, %s, %s);"
            cursor.executemany(query, sample_data)
            conn.commit()
            print("✅ Mock data inserted successfully.")
        else:
            print("ℹ️ Table already has data. Skipping insertion.")

    except Error as e:
        print(f"❌ Error while connecting to MySQL: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("🔒 MySQL connection closed.")

if __name__ == "__main__":
    setup_database()