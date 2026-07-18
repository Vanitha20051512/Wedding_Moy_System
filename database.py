import sqlite3

conn = sqlite3.connect("moy.db", check_same_thread=False)
cursor = conn.cursor()

# Parent Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS parents(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    village TEXT NOT NULL,
    mobile TEXT UNIQUE NOT NULL,
    login_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Moy Records Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS moy_records(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_name TEXT NOT NULL,
    guest_name TEXT NOT NULL,
    village TEXT NOT NULL,
    mobile TEXT NOT NULL,
    moy_amount REAL NOT NULL,
    payment_status TEXT DEFAULT 'Pending',
    receipt_no TEXT,
    transaction_id TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()

def get_connection():
    return conn

def get_cursor():
    return cursor

if __name__ == "__main__":
    print("Database Created Successfully")