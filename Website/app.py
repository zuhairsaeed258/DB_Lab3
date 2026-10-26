from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

def get_db_connection():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='ZS123456*',
        database='library_db',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

@app.route('/')
def index():
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM AUTHOR")
        authors = cursor.fetchall()
        
        cursor.execute("SELECT * FROM BOOK")
        books = cursor.fetchall()
    conn.close()
    return render_template('index.html', authors=authors, books=books)

@app.route('/add_author', methods=('GET', 'POST'))
def add_author():
    if request.method == 'POST':
        author_id = request.form['author_id']
        name = request.form['name']
        country = request.form['country']
        
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO AUTHOR (author_id, name, country) VALUES (%s, %s, %s)",
                           (author_id, name, country))
            conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_author.html')

@app.route('/edit_author/<int:author_id>', methods=('GET', 'POST'))
def edit_author(author_id):
    conn = get_db_connection()
    if request.method == 'POST':
        name = request.form['name']
        country = request.form['country']
        with conn.cursor() as cursor:
            cursor.execute("UPDATE AUTHOR SET name = %s, country = %s WHERE author_id = %s", (name, country, author_id))
            conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM AUTHOR WHERE author_id = %s", (author_id,))
        author = cursor.fetchone()
    conn.close()
    return render_template('edit_author.html', author=author)

@app.route('/add_book', methods=('GET', 'POST'))
def add_book():
    conn = get_db_connection()
    if request.method == 'POST':
        book_id = request.form['book_id']
        title = request.form['title']
        price = request.form['price']
        author_id = request.form['author_id']
        
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO BOOK (book_id, title, price, author_id) VALUES (%s, %s, %s, %s)",
                           (book_id, title, price, author_id))
            conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM AUTHOR")
        authors = cursor.fetchall()
    conn.close()
    return render_template('add_book.html', authors=authors)

@app.route('/edit_book/<int:book_id>', methods=('GET', 'POST'))
def edit_book(book_id):
    conn = get_db_connection()
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        author_id = request.form['author_id']
        with conn.cursor() as cursor:
            cursor.execute("UPDATE BOOK SET title = %s, price = %s, author_id = %s WHERE book_id = %s", (title, price, author_id, book_id))
            conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM BOOK WHERE book_id = %s", (book_id,))
        book = cursor.fetchone()
        cursor.execute("SELECT * FROM AUTHOR")
        authors = cursor.fetchall()
    conn.close()
    return render_template('edit_book.html', book=book, authors=authors)

@app.route('/delete_book/<int:book_id>', methods=('POST', 'GET'))
def delete_book(book_id):
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM BOOK WHERE book_id = %s", (book_id,))
        conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete_author/<int:author_id>', methods=('POST', 'GET'))
def delete_author(author_id):
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM AUTHOR WHERE author_id = %s", (author_id,))
        conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)