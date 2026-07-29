from flask import Flask, render_template, request, abort, redirect, url_for
import sqlite3

app = Flask(__name__)
DATABASE = 'database.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM game ORDER BY title ASC")
    games = cursor.fetchall()
    conn.close()
    return render_template('index.html', games=games, page_title='All Games', message='Browse the current game database or search by title.')

@app.route('/search')
def search():
    query = request.args.get('query', '').strip()
    conn = get_db_connection()
    cursor = conn.cursor()
    if query == '':
        cursor.execute("SELECT * FROM game ORDER BY title ASC")
        message = 'Showing al games'
    else:
        cursor.execute("SELECT * FROM game WHERE title LIKE ? ORDER BY title ASC", ('%' + query + '%',))
        message = 'Showing results for "' + query + '".'
    games = cursor.fetchall()
    conn.close()
    return render_template('index.html', games=games, query=query, page_title='Search Results', message=message)


@app.route('/top')
def top_game():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM game ORDER BY average_rating DESC, title ASC")
    games = cursor.fetchall()
    conn.close()
    return render_template('index.html', games=games, page_title='Top Rated Games', message='Games ordered by highest average rating.')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/wishlist')
def wishlist():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT
            wishlist.wishlist_id,
            wishlist.created_at,
            user.username,
            game.game_id,
            game.title,
            game.price,
            game.average_rating
        FROM wishlist
        LEFT JOIN user ON wishlist.user_id = user.user_id
        LEFT JOIN game ON wishlist.game_id = game.game_id
        ORDER BY user.username ASC, game.title ASC
    """)
    wishlist_items = cursor.fetchall()
    conn.close()
    return render_template('wishlist.html',wishlist_items=wishlist_items)


@app.route('/game/<int:game_id>', methods=['GET', 'POST'])
def game_detail(game_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute( """
        SELECT 
            game.game_id,
            game.title,
            game.release_date,
            game.price, 
            game.average_rating, 
            category.name AS category_name, 
            publisher.name AS publisher_name
        FROM game
        LEFT JOIN category ON game.category_id = category.category_id
        LEFT JOIN publisher ON game.publisher_id = publisher.publisher_id
        WHERE game.game_id = ?
    """, (game_id,))
    game = cursor.fetchone()
    if game is None:
        conn.close()
        abort(404)
    error = None
    wishlist_error = None

    if request.method == 'POST':
        form_type = request.form.get('form_type')

        if form_type == 'wishlist':
            username = request.form.get('wishlist_username', '').strip()
            if username == '':
                wishlist_error = 'Please enter a username before adding to wishlist.'
            else:
                cursor.execute(
                    "SELECT user_id FROM user WHERE username = ?",
                    (username,)
                )
                user = cursor.fetchone()
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        rating = request.form.get('rating', '').strip()
        review_text = request.form.get('review_text', '').strip()
        if username == '' or email == '' or rating == '' or review_text == '':
            error = 'Please fill in every field before submitting a review.'
        else:
            try:
                rating_number = int(rating)
                if rating_number < 1 or rating_number > 5:
                    error = 'Rating myst be a number between 1 to 5'
                else:
                    cursor.execute("SELECT user_id FROM user WHERE username = ?",(username,))
                    user = cursor.fetchone()
                    if user is None:
                        cursor.execute("INSERT INTO user (username, email) VALUES (?, ?)",(username, email))
                        user_id = cursor.lastrowid
                    else: user_id = user['user_id']
                    cursor.execute(
                        """
                        INSERT INTO review (rating, review_text, user_id, game_id)
                        VALUES (?, ?, ?, ?)
                        """,
                        (rating_number, review_text, user_id, game_id)
                    )
                    cursor.execute("SELECT AVG(rating) AS new_rating FROM review WHERE game_id = ?",(game_id,))
                    new_rating = cursor.fetchone()['new_rating']
                    cursor.execute("UPDATE game SET average_rating = ? WHERE game_id = ?",(round(new_rating, 1),game_id))
                    conn.commit()
                    conn.close()
                    return redirect(url_for('game_detail',game_id=game_id,review_added='yes'))
            except ValueError:
                error = 'Rating must be a number between 1 and 5.'

    cursor.execute("""
        SELECT
            review.rating,
            review.review_text,
            review.created_at,
            user.username
        FROM review
        LEFT JOIN user ON review.user_id = user.user_id
        WHERE review.game_id = ?
        ORDER BY review.created_at DESC
    """, (game_id,))
    reviews = cursor.fetchall()

    conn.close()
    return render_template('game_detail.html', game=game, reviews=reviews, error=error, review_added=request.args.get('review_added'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
    
if __name__ == '__main__':
    app.run(debug=True)