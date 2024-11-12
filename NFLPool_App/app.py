from flask import render_template, request, redirect, url_for, flash
from . import create_app, db  # Ensure db is imported if needed
from .models import User

# Create the Flask app using the factory function
app = create_app()

app.secret_key = 'your_secret_key'  # Needed for flash messages

# In-memory user storage (for simplicity)
users = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/entry', methods=['GET', 'POST'])
def entry():
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        pool_nickname = request.form['pool_nickname']
        playing_status = 'money' if 'playing_status' in request.form else 'free'

        # Check if the user exists in the database
        user = User.query.filter_by(email=email, username=pool_nickname).first()
        if not user:
            flash('User not found. If this is unexpected, please reach out for assistance.', 'warning')

        # Proceed with handling the game picks and saving the entry
        flash('Entry submitted successfully!', 'success')
        return redirect(url_for('home'))

    # Sample data for the game slate with spreads
    games = [
        {'home_team': 'Team A', 'away_team': 'Team B', 'spread': '-3.5'},
        {'home_team': 'Team C', 'away_team': 'Team D', 'spread': '+1.5'},
        {'home_team': 'Team E', 'away_team': 'Team F', 'spread': '-7.0'},
    ]
    return render_template('entry.html', games=games)

if __name__ == '__main__':
    app.run(debug=True)
