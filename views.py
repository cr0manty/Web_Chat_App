from flask import render_template, redirect, url_for, request, session
from flask_socketio import Namespace, join_room, leave_room

from app import server
from models import Login


@server.route('/', methods=['POST', 'GET'])
def index():
    form = Login()
    if form.validate_on_submit():
        session['username'] = form.username.data
        session['room'] = form.room.data
        return redirect(url_for('chat'))
    elif request.method == 'GET':
        form.username.data = session.get('username', '')
        form.room.data = session.get('room', '')
    return render_template('index.html', form=form, username=session.get('username'))


@server.route('/chat', methods=['POST', 'GET'])
def chat():
    username = session.get('username', '')
    room = session.get('room', '')
    if username == '' or room == '':
        return redirect(url_for('index'))
    return render_template('chat.html', username=username, room=room)


class ChatApp(Namespace):
    def on_connect(self):
        room = session.get('room')
        join_room(room)
        self.emit('options', {'msg': '\'{}\' joined the room.'.format(session.get('username'))},
                  room=room)

    def on_disconnect(self):
        room = session.get('room')
        leave_room(room)
        self.emit('options', {'msg': '\'{}\' has left the room.'.format(session.get('username'))},
                  room=session.get('room'))

    def on_message(self, message):
        msg = message.get('msg').encode('latin-1').decode('utf-8')
        self.emit('message', {'msg': '{}: {}'.format(session.get('username'), msg)},
                  room=session.get('room'))
