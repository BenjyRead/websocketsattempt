from flask import Flask, redirect, send_from_directory
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)


@app.get('/')
def index():
    return redirect('/home')

@app.get('/home')
def home():
    return send_from_directory('static', 'home.html')

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

if __name__ == '__main__':
    app.run(debug=True)