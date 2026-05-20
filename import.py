import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()


# Categories
cursor.execute("""
INSERT OR IGNORE INTO category (category_id, name)
VALUES (1, 'Sandbox')
""")

cursor.execute("""
INSERT OR IGNORE INTO category (category_id, name)
VALUES (2, 'Action Adventure')
""")

cursor.execute("""
INSERT OR IGNORE INTO category (category_id, name)
VALUES (3, 'Battle Royale')
""")

cursor.execute("""
INSERT OR IGNORE INTO category (category_id, name)
VALUES (4, 'Tactical Shooter')
""")

cursor.execute("""
INSERT OR IGNORE INTO category (category_id, name)
VALUES (5, 'Role-Playing Game')
""")

cursor.execute("""
INSERT OR IGNORE INTO category (category_id, name)
VALUES (6, 'Sports')
""")

# Publishers
cursor.execute("""
INSERT OR IGNORE INTO publisher (publisher_id, name)
VALUES (1, 'Mojang Studios')
""")

cursor.execute("""
INSERT OR IGNORE INTO publisher (publisher_id, name)
VALUES (2, 'Rockstar Games')
""")

cursor.execute("""
INSERT OR IGNORE INTO publisher (publisher_id, name)
VALUES (3, 'Epic Games')
""")

cursor.execute("""
INSERT OR IGNORE INTO publisher (publisher_id, name)
VALUES (4, 'Riot Games')
""")

cursor.execute("""
INSERT OR IGNORE INTO publisher (publisher_id, name)
VALUES (5, 'Bandai Namco Entertainment')
""")

cursor.execute("""
INSERT OR IGNORE INTO publisher (publisher_id, name)
VALUES (6, 'EA Sports')
""")

# Games
cursor.execute("""
INSERT OR IGNORE INTO game
    (game_id, title, release_date, price, average_rating, category_id, publisher_id)
VALUES
    (1, 'Minecraft', '2011-11-18', 29.99, 4.5, 1, 1)
""")

cursor.execute("""
INSERT OR IGNORE INTO game
    (game_id, title, release_date, price, average_rating, category_id, publisher_id)
VALUES
    (2, 'GTA V', '2013-09-17', 59.99, 4.0, 2, 2)
""")

cursor.execute("""
INSERT OR IGNORE INTO game
    (game_id, title, release_date, price, average_rating, category_id, publisher_id)
VALUES
    (3, 'Fortnite', '2017-07-21', 0.00, 4.0, 3, 3)
""")

cursor.execute("""
INSERT OR IGNORE INTO game
    (game_id, title, release_date, price, average_rating, category_id, publisher_id)
VALUES
    (4, 'Valorant', '2020-06-02', 0.00, 4.5, 4, 4)
""")

cursor.execute("""
INSERT OR IGNORE INTO game
    (game_id, title, release_date, price, average_rating, category_id, publisher_id)
VALUES
    (5, 'Elden Ring', '2022-02-25', 79.99, 5.0, 5, 5)
""")

cursor.execute("""
INSERT OR IGNORE INTO game
    (game_id, title, release_date, price, average_rating, category_id, publisher_id)
VALUES
    (6, 'EA Sports FC 25', '2024-09-27', 89.99, 3.5, 6, 6)
""")

# Users
cursor.execute("""
INSERT OR IGNORE INTO user (user_id, username, email)
VALUES (1, 'alex', 'alex@example.com')
""")

cursor.execute("""
INSERT OR IGNORE INTO user (user_id, username, email)
VALUES (2, 'speed', 'speed@example.com')
""")

cursor.execute("""
INSERT OR IGNORE INTO user (user_id, username, email)
VALUES (3, 'rpgfan', 'rpgfan@example.com')
""")

cursor.execute("""
INSERT OR IGNORE INTO user (user_id, username, email)
VALUES (4, 'bude', 'bude@example.com')
""")

# Reviews
cursor.execute("""
INSERT OR IGNORE INTO review
    (review_id, rating, review_text, user_id, game_id)
VALUES
    (1, 5, 'Creative, relaxing, and great value for the price.', 1, 1)
""")

cursor.execute("""
INSERT OR IGNORE INTO review
    (review_id, rating, review_text, user_id, game_id)
VALUES
    (2, 4, 'A good game because it has endless replay value.', 4, 1)
""")

cursor.execute("""
INSERT OR IGNORE INTO review
    (review_id, rating, review_text, user_id, game_id)
VALUES
    (3, 4, 'Large open world with lots of activities and missions.', 2, 2)
""")

cursor.execute("""
INSERT OR IGNORE INTO review
    (review_id, rating, review_text, user_id, game_id)
VALUES
    (4, 4, 'Fun with friends and easy to start because it is free.', 1, 3)
""")

cursor.execute("""
INSERT OR IGNORE INTO review
    (review_id, rating, review_text, user_id, game_id)
VALUES
    (5, 5, 'Competitive gameplay with clear team strategy.', 2, 4)
""")

cursor.execute("""
INSERT OR IGNORE INTO review
    (review_id, rating, review_text, user_id, game_id)
VALUES
    (6, 5, 'Challenging combat and excellent world design.', 3, 5)
""")

cursor.execute("""
INSERT OR IGNORE INTO review
    (review_id, rating, review_text, user_id, game_id)
VALUES
    (7, 3, 'Good football gameplay, but the price is quite high.', 4, 6)
""")

# Wishlist items
cursor.execute("""
INSERT OR IGNORE INTO wishlist (wishlist_id, user_id, game_id)
VALUES (1, 1, 5)
""")

cursor.execute("""
INSERT OR IGNORE INTO wishlist (wishlist_id, user_id, game_id)
VALUES (2, 4, 2)
""")

cursor.execute("""
INSERT OR IGNORE INTO wishlist (wishlist_id, user_id, game_id)
VALUES (3, 3, 6)
""")
print("Sample data inserted successfully.")

conn.commit()
conn.close()