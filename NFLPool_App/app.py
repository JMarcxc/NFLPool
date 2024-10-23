from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

# In-memory user storage (for simplicity)
users = []


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Basic validation (you can expand this)
        if any(user['username'] == username for user in users):
            flash('Username already exists!', 'danger')
            return redirect(url_for('register'))

        # Store user data
        users.append({'username': username, 'email': email, 'password': password})
        flash('Registration successful!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
