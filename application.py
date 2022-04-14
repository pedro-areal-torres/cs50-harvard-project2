import os

from flask import Flask, render_template, request, jsonify, session, redirect
from flask_session import Session
from flask_socketio import SocketIO, emit

import json

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Store all users
allUsers = []

# Store all channels, general channel inicialized
channels=['General']

# Store channel messages
channelMsgs = {"general": []}

# Messages Limit per channel
msgLimit = 100

# Log in screen that check if the user it's already active
@app.route("/")
def index():
    # Check if there's already a user active
    username = session.get('username')
    if not username:
        return render_template('login.html')
    else:
        return render_template('chat.html', username=username,channels=channels, channelMsgs=channelMsgs['general'])

# Log in and register user session
@app.route('/login', methods = ["POST"])
def login():
    # Get username entered by the user
    username = request.form.get('display-name')
    # Store the username in session
    session['username'] = username
    allUsers.append(username)
    return redirect('/')

# Socket for when a user write a new message
@socketio.on("new msg")
def messages(data):
    #Get all the data from the message
    username = data["username"]
    msg = data["msg"]
    channel = data["channel"]
    dateTime = data["dateTime"]
    #If the channel already exceed the limit it will not store the message
    if len(channelMsgs[channel]) >= 100:
        emit("announce message", {"success": False})
    else:
        channelMsgs[channel].append([username, dateTime, msg])
        emit("announce message", {"success": True, "channel": channel, "username": username,"dateTime": dateTime, "msg": msg}, broadcast=True)

# When a user creates a new channel
@socketio.on("new channel")
def new_channel(data):
    channel = data["channel"]
    username = data["username"]
    # If the channel already exists, fails
    if channel in channels:
        emit("announce channel", {"success": False})
    # Otherwise just add it to channels list
    else:
        channels.append(channel)
        channelMsgs[channel] = []
        emit("announce channel", {"success":True, "channel": channel, "username":username}, broadcast=True)

# When a user changes the channel
@app.route('/channel/<channel>')
def channel(channel):
    # Takes the JSON object and returns a string
    return json.dumps(channelMsgs[channel])

# Remove a message (Personal Touch)
@app.route('/delete_msg/<activeChannel>/<hiddenMsg>')
def delete_msg(activeChannel, hiddenMsg):
    # Pick the message
    msg = list(hiddenMsg.split(","))
    msg.pop()
    msgs_list = channelMsgs[activeChannel]
    # And delete it from messages list of that channel
    for i in range(len(msgs_list)):
        if msgs_list[i] == msg:
            del channelMsgs[activeChannel][i]
            return 'OK'
    return 'OK'
    


