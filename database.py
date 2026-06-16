import sqlite3

conn = sqlite3.connect('database/store.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders(
    order_id INTEGER PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    quantity INTEGER,
    price REAL,
    order_date TEXT
)
""")

sample_data = [
    (1,'Laptop','Electronics',2,50000,'2025-01-10'),
    (2,'Phone','Electronics',3,20000,'2025-02-15'),
    (3,'Shoes','Fashion',5,2500,'2025-03-20'),
    (4,'Headphones','Electronics',4,3000,'2025-03-25'),
    (5,'Tshirt','Fashion',8,800,'2025-04-05'),
    (6,'Laptop','Electronics',1,50000,'2025-04-10'),
    (7,'Phone','Electronics',2,20000,'2025-05-01'),
    (8,'Watch','Fashion',4,5000,'2025-05-10'),
    (9,'Keyboard','Electronics',3,1500,'2025-05-15'),
    (10,'Mouse','Electronics',5,800,'2025-05-20'),
    (11,'Jeans','Fashion',6,2000,'2025-06-01'),
    (12,'Tablet','Electronics',2,30000,'2025-06-05'),
    (13,'Speaker','Electronics',3,4000,'2025-06-08'),
    (14,'Jacket','Fashion',2,3500,'2025-06-12'),
    (15,'Power Bank','Electronics',7,1200,'2025-06-15')
]

cursor.executemany(
    "INSERT OR REPLACE INTO orders VALUES (?,?,?,?,?,?)",
    sample_data
)

conn.commit()
conn.close()

print("Database Created Successfully")