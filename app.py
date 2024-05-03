from flask import Flask, render_template, request, redirect, url_for, session
from flaskext.mysql import MySQL

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

# MySQL configurations
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'your_username'
app.config['MYSQL_DATABASE_PASSWORD'] = 'your_password'
app.config['MYSQL_DATABASE_DB'] = 'myflaskapp'

mysql = MySQL(app)

# Function to create the user table if it doesn't exist
def create_user_table():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    email VARCHAR(255) NOT NULL,
                    location VARCHAR(255) NOT NULL)''')
    conn.commit()
    conn.close()

# Route to handle user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        location = request.form['location']

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, email, location) VALUES (%s, %s, %s)',
                     (name, email, location))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))  # Redirect to the homepage after registration
    return render_template('register.html')  # Render the registration form

# Route to handle user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
        user = cursor.fetchone()  # Fetch the first user with the provided email
        conn.close()

        if user:
            # If the user exists, store their information in the session
            session['user'] = {'id': user[0], 'name': user[1], 'email': user[2], 'location': user[3]}
            return redirect(url_for('index'))  # Redirect to the homepage after login
        else:
            # If the user does not exist, display an error message
            error_message = 'User not found. Please register.'
            return render_template('login.html', error=error_message)

    return render_template('login.html')  # Render the login form

# Route to handle user logout
@app.route('/logout')
def logout():
    # Clear the session (remove user data)
    session.clear()
    # Redirect the user to the login page (or any other page)
    return redirect(url_for('login'))

# Index route
@app.route('/')
def index():
    if 'user' in session:
        user = session['user']
        return render_template('index.html', user=user)
    return redirect(url_for('login'))  # Redirect to login if user is not logged in

# About route
@app.route('/about')
def about():
    return render_template('about.html')

# Contact route
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    create_user_table()  # Ensure the user table exists before running the app
    app.run(debug=True)
