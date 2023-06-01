from flask import Flask, request, render_template, redirect

app = Flask(__name__)

users = {}

# Load users from file
with open('users.txt', 'r') as f:
    for line in f:
        username, password = line.strip().split(':')
        users[username] = password

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username] == password:
        return redirect('/home')
    else:
        return render_template('login.html', error='Invalid username or password')

@app.route('/home')
def home():
    return 'Welcome to the home page!'

# Save users to file
def save_users():
    with open('users.txt', 'w') as f:
        for username, password in users.items():
            f.write(f'{username}:{password}\n')

if __name__ == '__main__':
    app.run(debug=True)