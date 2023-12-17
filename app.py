from flask import Flask, redirect, send_from_directory

app = Flask(__name__)

@app.get('/')
def index():
    return redirect('/home')

@app.get('/home')
def home():
    return send_from_directory('static', 'home.html')

if __name__ == '__main__':
    app.run(debug=True)