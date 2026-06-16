import sqlite3
import pandas as pd

conn = sqlite3.connect('database/store.db')

query = """
SELECT
    product_name,
    SUM(quantity) AS total_sold
FROM orders
GROUP BY product_name
ORDER BY total_sold DESC
"""

df = pd.read_sql_query(query, conn)

print(df)

df.to_excel(
    'reports/sales_report.xlsx',
    index=False
)

print("\nExcel Report Generated!")

conn.close()