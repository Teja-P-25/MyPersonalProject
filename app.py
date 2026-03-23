import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    # Create the table if it doesn't exist
    conn.execute('CREATE TABLE IF NOT EXISTS bookings (id INTEGER PRIMARY KEY, car TEXT, days INTEGER, total INTEGER)')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    cars = [
        {"name": "Tesla Model S", "price": 120},
        {"name": "BMW M4", "price": 150},
        {"name": "Audi R8", "price": 250}
    ]
    return render_template('index.html', cars=cars)

@app.route('/book', methods=['POST'])
def book():
    car_name = request.form['car_name']
    days = int(request.form['days'])
    price = int(request.form['price'])
    total = days * price
    
    # SAVE TO DATABASE
    conn = sqlite3.connect('database.db')
    conn.execute('INSERT INTO bookings (car, days, total) VALUES (?, ?, ?)', (car_name, days, total))
    conn.commit()
    conn.close()
    
    return f"<h1>Booking Confirmed!</h1><p>Reserved {car_name}. Total: ${total}</p><a href='/'>Home</a>"

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
