import sqlite3


def create_table():
    with sqlite3.connect('example.db') as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS products (product_id INTEGER PRIMARY KEY,name INTEGER UNIQUE, quantity TEXT)')

    conn.close()

def insert_example_data():
    name = "hat"
    quantity = "1"

    try: 
        with sqlite3.connect('example.db') as conn:
            conn.execute('INSERT INTO products (name, quantity) VALUES (?, ?)', (name, quantity))

        conn.close()

    except Exception as e:
        print("Error: ", e)
        
def display_data():
    conn = sqlite3.connect('example.db')

    results = conn.execute('SELECT  * FROM products')

    for row in results:
        print(row)

        
    print("Program done")

def create_new_product():
    input_name = input("Enter product name: ")
    input_quantity = input("Enter product quantity: ")
    
    try: 
        with sqlite3.connect('example.db') as conn:
            conn.execute('INSERT INTO products (name, quantity) VALUES (?, ?)', (input_name, input_quantity))
            
        conn.close()
        
    except Exception as e:
        print("Error: ", e)
        
def update_product():
    input_id = input("Enter product id: ")
    input_name = input("Enter product name: ")
    input_quantity = input("Enter product quantity: ")
    
    try: 
        with sqlite3.connect('example.db') as conn:
            conn.execute('UPDATE products SET name = ?, quantity = ? WHERE product_id = ?', (input_name, input_quantity, input_id))
            
        conn.close()
        
    except Exception as e:
        print("Error: ", e)
          

def delete_product(product_id):
    try: 
        with sqlite3.connect('example.db') as conn:
            conn.execute('DELETE FROM products WHERE product_id = ?', (product_id))
            
        conn.close()
        
    except Exception as e:
        print("Error: ", e)

def main():
    create_table()
    insert_example_data()
    display_data()
    create_new_product()
    display_data()
    update_product()
    display_data()
    delete_product(1)
    display_data()


if __name__ == "__main__":
    main()