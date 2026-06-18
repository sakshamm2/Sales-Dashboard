import mysql.connector
# Import the connection function from your db.py file
from db import get_connection

def fetch_all_sales():
    """Fetches all sales records from the database as a list of dictionaries."""
    conn = get_connection()
    # dictionary=True allows us to access columns by name (e.g., row['price'])
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("USE sales_dashboard;")
    cursor.execute("SELECT * FROM sales;")
    sales_records = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return sales_records

def calculate_total_revenue(sales):
    """Calculates the total revenue across all sales."""
    total = 0.0
    for row in sales:
        total += float(row['quantity']) * float(row['price'])
    return total

def get_revenue_by_category(sales):
    """Groups and totals revenue by product category."""
    category_totals = {}
    for row in sales:
        category = row['category']
        revenue = float(row['quantity']) * float(row['price'])
        
        # If category exists, add to it; otherwise, start at 0
        category_totals[category] = category_totals.get(category, 0.0) + revenue
    return category_totals

if __name__ == "__main__":
    print("📊 Connecting to MySQL and fetching sales data...")
    data = fetch_all_sales()
    
    print(f"✅ Successfully retrieved {len(data)} records.\n")
    
    # 1. Calculate Total Revenue
    total_rev = calculate_total_revenue(data)
    print(f"💰 Total Revenue: ${total_rev:,.2f}")
    
    # 2. Calculate Category Breakdown
    print("\n🗂️  Revenue Breakdown by Category:")
    breakdown = get_revenue_by_category(data)
    for category, amount in breakdown.items():
        print(f"   - {category}: ${amount:,.2f}")