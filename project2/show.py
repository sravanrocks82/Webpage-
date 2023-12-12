from flask import Flask, render_template, request
import mysql.connector
import show




app = Flask(__name__)
def fetch_data():
    # Replace these with your MySQL database credentials
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '991969',
        'database': 'firstdatabase'
    }

    # Connect to the database
    conn = mysql.connector.connect(**db_config)

    # Create a cursor to execute SQL queries
    cursor = conn.cursor()

    # Replace 'your_table' with the name of your table
    query = "SELECT * FROM sims"

    # Execute the query
    cursor.execute(query)

    # Fetch all the rows
    rows = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    return rows

if __name__ == "__main__":
    second_data = fetch_data()
    for row in second_data:
        print(row)



if __name__ == '__main__':
    app.run(debug=True)