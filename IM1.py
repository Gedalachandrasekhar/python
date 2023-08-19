from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'gedala'  # Change this to a secure value

@app.route('/')
def home():
    if 'username' in session:
        return redirect('/dashboard')
    else:
        return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Check the entered credentials against the database
    # If valid, store the username in the session
    session['username'] = username
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')
