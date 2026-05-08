import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS user (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS category (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS publisher (
    publisher_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS game (
    game_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    release_date DATE,
    price DECIMAL,
    average_rating FLOAT,
    category_id INTEGER,
    publisher_id INTEGER,
    FOREIGN KEY (category_id)
        REFERENCES category(category_id),
    FOREIGN KEY (publisher_id)
        REFERENCES publisher(publisher_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS review (
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    rating INTEGER,
    review_text TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    user_id INTEGER,
    game_id INTEGER,
    FOREIGN KEY (user_id)
        REFERENCES user(user_id),
    FOREIGN KEY (game_id)
        REFERENCES game(game_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS wishlist (
    wishlist_id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    user_id INTEGER,
    game_id INTEGER,
    FOREIGN KEY (user_id)
        REFERENCES user(user_id),
    FOREIGN KEY (game_id)
        REFERENCES game(game_id)
)
""")

conn.commit()
conn.close()

print("Database initialized successfully.")