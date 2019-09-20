import os

from app import socket, server

import views

socket.on_namespace(views.ChatApp('/chat'))

if __name__ == '__main__':
    socket.run(server, host='0.0.0.0',
               port=int(os.environ.get('PORT', 5000)))
