from os import urandom

from flask import Flask
from flask_socketio import SocketIO

server = Flask(__name__)
server.config['SECRET_KEY'] = urandom(24)

socket = SocketIO(server)
