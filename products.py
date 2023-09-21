import sqlite3

db = 'product_manager.db'

with sqlite3.connect(db) as conn:
    conn.execute('CREATE TABLE IF NOT EXISTS products (product_id INTEGER PRIMARY KEY,name INTEGER UNIQUE, quantity TEXT)')

conn.close()


name = "why_you_"
quantity = "1"

try: 
    with sqlite3.connect(db) as conn:
        conn.execute('INSERT INTO products (name, quantity) VALUES (?, ?)', (name, quantity))

    conn.close()

except Exception as e:
    print("Error: ", e)
    
conn = sqlite3.connect(db)

results = conn.execute('SELECT * FROM products')

for row in results:
    print(row)

    
print("Program done")