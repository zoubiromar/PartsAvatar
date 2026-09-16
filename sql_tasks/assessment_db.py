import sqlite3

def setup_complex_db():
    conn = sqlite3.connect('parts_avatar.db')
    cursor = conn.cursor()
    
    # Create Tables
    cursor.execute("DROP TABLE IF EXISTS Order_Items")
    cursor.execute("DROP TABLE IF EXISTS Orders")
    cursor.execute("DROP TABLE IF EXISTS Customers")

    cursor.execute("""
    CREATE TABLE Customers (
        customer_id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT UNIQUE,
        join_date DATE
    )""")
    
    cursor.execute("""
    CREATE TABLE Orders (
        order_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        order_date DATE,
        status TEXT,
        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
    )""")
    
    cursor.execute("""
    CREATE TABLE Order_Items (
        item_id INTEGER PRIMARY KEY,
        order_id INTEGER,
        sku TEXT,
        price REAL,
        quantity INTEGER,
        FOREIGN KEY (order_id) REFERENCES Orders(order_id)
    )""")

    # Populate Data
    customers = [
        (1, 'John Doe', 'john@example.com', '2023-01-01'),
        (2, 'Jane Smith', 'jane@example.com', '2023-05-15'),
        (3, 'Alex Rivard', 'alex@parts.ca', '2024-01-10'),
        (4, 'Fraudulent User', 'bad@actor.com', '2024-03-01')
    ]
    orders = [
        (101, 1, '2024-02-10', 'Shipped'),
        (102, 1, '2024-02-25', 'Pending'),
        (103, 2, '2024-03-01', 'Shipped'),
        (104, 3, '2024-03-05', 'Pending')
    ]
    items = [
        (1, 101, 'BRK-99', 50.0, 2), # John spent 100
        (2, 101, 'OIL-5W30', 15.0, 1), # John spent 15
        (3, 102, 'ENG-01', 500.0, 1), # John spent 500 (Pending)
        (4, 103, 'BRK-99', 50.0, 3), # Jane spent 150
        (5, 104, 'WIPER-22', 25.0, 2)  # Alex spent 50
    ]

    cursor.executemany("INSERT INTO Customers VALUES (?,?,?,?)", customers)
    cursor.executemany("INSERT INTO Orders VALUES (?,?,?,?)", orders)
    cursor.executemany("INSERT INTO Order_Items VALUES (?,?,?,?,?)", items)
    
    conn.commit()
    conn.close()
    print("Database initialized with enhanced data.")

if __name__ == "__main__":
    setup_complex_db()