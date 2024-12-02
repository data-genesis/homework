import sqlite3

prod = {
    "title": ["Кола", "Вода", "Биткоин", "Курс по уверенности"],
    "description": ["с газом", "без газа", "дорогой", "поможет, будь уверен"],
    "price": [100, 200, 95000, 1000]
}
def initiate_db():
    conn = sqlite3.connect('products.db')

    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        description TEXT NOT NULL,
                        price INTEGER NOT NULL
                      )''')
    conn.commit()
    conn.close()

def get_all_products():
    conn = sqlite3.connect('products.db')

    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM Products''')
    return cursor.fetchall()
    conn.close()

def add_product(title, description, price):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                   (title, description, price))
    conn.commit()
    conn.close

# for title, description, price in zip(prod["title"], prod["description"], prod["price"]):
#     add_product(title, description, price)