from flask import Flask, render_template, request, jsonify, redirect,url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/movie', methods=['POST'])
def addMovie():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    name = request.form['name']
    rating = request.form['rating']

    try:
        cursor.execute('INSERT INTO movies(name, rating) VALUES (?, ?)', (name, rating))
        connection.commit()
        message = name + ' has been successfully added!'
    except:
        connection.rollback()
        message = name + ' was not added due to an error'
    finally:
        connection.close()
        return redirect('/movies')


@app.route('/movies')
def movies():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM movies')
    movies = cursor.fetchall()
    connection.close()
    return render_template('movies.html', movies=movies)


app.run(debug=True)
