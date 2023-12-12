import pandas as pd
import csv
import show,os
import pandas
from flask import Flask, render_template, request
from fileinput import filename
import mysql.connector
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload.html')
def upload():
    return render_template('upload.html')

@app.route('/show.html')
def device():
    second_data=show.fetch_data()
    return render_template('show.html',second_data=second_data)
@app.route('/result', methods=['POST','GET'])
def result():
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '991969',
        'database': 'firstdatabase'
    }

    # Get user input from the HTML form
    user_input = request.form['sravan']


    # Establish a connection to the MySQL database
    connection = mysql.connector.connect(**db_config)

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Execute a SELECT query with user input
    query = 'SELECT * FROM sims WHERE  Network= %s'
    cursor.execute(query, (user_input,))

    # Fetch all rows from the query result
    first_data= cursor.fetchall()

    # Close the database connection
    connection.close()

    second_data = show.fetch_data()

    # Render the HTML template and pass the retrieved data
    return render_template('show.html', first_data=first_data,second_data=second_data)

# MySQL configurations



@app.route('/insert', methods=['POST'])
def insert1():
    return render_template('uploaddata.html')


 

if __name__ == '__main__':
    app.run(debug=True)
