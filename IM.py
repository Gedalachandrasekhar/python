import sqlite3
from getpass import getpass

# Database connection
conn = sqlite3.connect('IM DB.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        barcode TEXT NOT NULL,
        name TEXT NOT NULL,
        quantity INTEGER NOT NULL
    )
''')

# Functions for admin operations
def add_product():
    barcode = input("Enter product barcode: ")
    name = input("Enter product name: ")
    quantity = int(input("Enter product quantity: "))

    cursor.execute('INSERT INTO products (barcode, name, quantity) VALUES (?, ?, ?)', (barcode, name, quantity))
    conn.commit()
    print("Product added successfully.")

def remove_product():
    barcode = input("Enter product barcode: ")

    cursor.execute('DELETE FROM products WHERE barcode = ?', (barcode,))
    conn.commit()
    print("Product removed successfully.")

def view_products():
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()

    print("Product ID\tBarcode\tProduct Name\tQuantity")
    for product in products:
        print(f"{product[0]}\t\t{product[1]}\t{product[2]}\t\t{product[3]}")

# Functions for employee operations
def view_available_products():
    cursor.execute('SELECT * FROM products WHERE quantity > 0')
    products = cursor.fetchall()

    print("Product ID\tBarcode\tProduct Name\tQuantity")
    for product in products:
        print(f"{product[0]}\t\t{product[1]}\t{product[2]}\t\t{product[3]}")

# Main program loop
while True:
    print("\n1. Admin Login")
    print("2. Employee Login")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        username = input("Enter admin username: ")
        password = getpass("Enter admin password: ")

        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ? AND role = "admin"', (username, password))
        admin = cursor.fetchone()

        if admin:
            while True:
                print("\nAdmin Menu:")
                print("1. Add Product")
                print("2. Remove Product")
                print("3. View Products")
                print("4. Logout")

                admin_choice = int(input("Enter your choice: "))

                if admin_choice == 1:
                    add_product()
                elif admin_choice == 2:
                    remove_product()
                elif admin_choice == 3:
                    view_products()
                elif admin_choice == 4:
                    break
                else:
                    print("Invalid choice. Try again.")
        else:
            print("Invalid username or password. Try again.")

    elif choice == 2:
        username = input("Enter employee username: ")
        password = getpass("Enter employee password: ")

        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ? AND role = "employee"', (username, password))
        employee = cursor.fetchone()

        if employee:
            while True:
                print("\nEmployee Menu:")
                print("1. View Available Products")
                print("2. Logout")

                employee_choice = int(input("Enter your choice: "))

                if employee_choice == 1:
                    view_available_products()
                elif employee_choice == 2:
                    break
                else:
                    print("Invalid choice. Try again.")
        else:
            print("Invalid username or password. Try again.")

    elif choice == 3:
        break

    else:
        print("Invalid choice. Try again.")

# Close database connection
conn.close()
