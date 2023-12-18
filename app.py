from flask import Flask, redirect, send_from_directory
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')


@app.get('/')
def index():
    return redirect('/home')

@app.get('/home')
def home():
    return send_from_directory('static', 'home.html')

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    socketio.send(message)

if __name__ == '__main__':
    socketio.run(app, debug=True)