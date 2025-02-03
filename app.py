from flask import Flask, render_template
import sqlite3
from dates import dates

app = Flask(__name__)

# Function to get data from the database
def get_data_from_db():
    connection = sqlite3.connect('danedoanalizy.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM cars WHERE datecollected like '2021-07-01%' ORDER BY datecollected DESC LIMIT 10")
    data = cursor.fetchall()
    connection.close()
    return data


@app.route('/<date>', methods=['GET'])
def get_cars_for_date(date):
    connection = sqlite3.connect('danedoanalizy.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM cars WHERE datecollected like '{date}%' ORDER BY datecollected DESC")
    data = cursor.fetchall()
    connection.close()
    return render_template('index.html', dates=dates, cars=data)

@app.route('/')
def index():
    # Fetch data from the database
    # users = get_data_from_db()
    # Render the data in the HTML template
    return render_template('index.html', dates=dates)

if __name__ == '__main__':
    app.run(debug=False)