from flask import Flask, render_template, request, abort
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('query', '').strip()
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM game WHERE title LIKE ?", ('%' + query + '%',))
    games = cursor.fetchall()
    conn.close()
    return render_template('index.html', games=games)

@app.route('/game/<int:game_id>')
def game_detail(game_id):
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
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
    game = cursor.fetchall()
    if game is None:
        conn.close()
        abort(404)
    conn.close()
    return render_template('game_detail.html', game=game)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
    
if __name__ == '__main__':
    app.run(debug=True)