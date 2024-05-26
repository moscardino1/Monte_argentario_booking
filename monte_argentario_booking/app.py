from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    beach = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time_slot = db.Column(db.String(50), nullable=False)
    spot = db.Column(db.Integer, nullable=False)
    booked = db.Column(db.Boolean, default=False)

# Define the number of spots for each beach
beach_spots = {
    "Beach 1": 5,
    "Beach 2": 10,
    "Beach 3": 8,
    "Beach 4": 8,
    "Beach 5": 8
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book/<beach>', methods=['GET', 'POST'])
def book(beach):
    if request.method == 'POST':
        date_str = request.form['date']
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        spot = int(request.form['spot'])
        time_slots = request.form.getlist('time_slot')
        
        # Check if any conflicting bookings exist for the selected date and spot
        conflicting_bookings = Booking.query.filter_by(beach=beach, date=date, spot=spot).all()
        for booking in conflicting_bookings:
            if booking.time_slot in time_slots:
                flash('Conflicting booking exists for the selected date, spot, and time slot.')
                return redirect(url_for('book', beach=beach))
        
        # If no conflicting bookings, proceed with the booking
        for time_slot in time_slots:
            booking = Booking(beach=beach, date=date, time_slot=time_slot, spot=spot, booked=True)
            db.session.add(booking)
        db.session.commit()
        flash('Booking successful!')
        
        return redirect(url_for('book', beach=beach))
    
    return render_template('booking.html', beach=beach)

@app.route('/api/available_spots/<beach_name>')
def api_available_spots(beach_name):
    date_str = request.args.get('date')
    date = datetime.strptime(date_str, '%Y-%m-%d').date()

    # Get all existing bookings for the specified beach and date
    existing_bookings = Booking.query.filter_by(beach=beach_name, date=date).all()

    booked_spots = {}
    for booking in existing_bookings:
        if booking.spot not in booked_spots:
            booked_spots[booking.spot] = []
        booked_spots[booking.spot].append(booking.time_slot)

    total_spots = beach_spots.get(beach_name, 10)  # Default to 10 if beach not found

    available_spots = {
        spot: {
            "Morning": "Morning" not in booked_spots.get(spot, []),
            "Evening": "Evening" not in booked_spots.get(spot, [])
        }
        for spot in range(1, total_spots + 1)
    }

    return jsonify({'available_spots': available_spots})

@app.route('/bookings')
def view_bookings():
    bookings = Booking.query.all()
    return render_template('view_bookings.html', bookings=bookings)

@app.route('/beach/<beach_name>')
def view_beach_bookings(beach_name):
    return render_template('beach_bookings.html', beach=beach_name)

if __name__ == '__main__':
    app.run(debug=True)
