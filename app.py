from flask import Flask, render_template, request

app = Flask(__name__)

# This is our list of cars (The "Memory")
cars_data = [
    {"name": "Tesla Model S", "price": 120},
    {"name": "BMW M4", "price": 150},
    {"name": "Audi R8", "price": 250}
]

@app.route('/')
def home():
    # This tells Python: "Open index.html and show the cars_data"
    return render_template('index.html', cars=cars_data)

@app.route('/book', methods=['POST'])
def book():
    # This runs when the user clicks the "Book Now" button
    name = request.form['car_name']
    days = int(request.form['days'])
    price = int(request.form['price'])
    total = days * price
    return f"<h1>Booking Confirmed!</h1><p>You reserved a {name} for {days} days.</p><h2>Total Cost: ${total}</h2><a href='/'>Go Back</a>"

if __name__ == "__main__":
    app.run(debug=True)