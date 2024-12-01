from flask import Flask, request, redirect, url_for, send_from_directory, render_template_string
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__)
socketio = SocketIO(app)  # Initialize SocketIO
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
        os.mkdir(UPLOAD_FOLDER)

@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    files = [f for f in files if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], f))]
    return render_template_string('''
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Photo Uploader</title>
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap" rel="stylesheet">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.0/socket.io.js"></script>
        <style>
            body { font-family: 'Roboto', sans-serif; background-color: #0B1121; margin: 40px; }
            h1, h2 { color: #ffffff; }
            form { background-color: #b8cabe; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
            input[type="file"] { margin-top: 10px; }
            input[type="submit"] { background-color: #0084ff; color: white; padding: 12px 20px; border: none; border-radius: 4px; cursor: pointer; }
            input[type="submit"]:hover { background-color: #0056b3; }
            ul { list-style-type: none; padding: 0; }
            li { padding: 8px; background-color: #b8cabe; border: 1px solid #ddd; margin-top: 5px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
            a { text-decoration: none; color: #333; }
            a:hover { text-decoration: underline; }
            #chat { margin-top: 20px; }
            #messages { height: 200px; overflow-y: scroll; border: 1px solid #c6a6a6; padding: 10px; background-color: #b8cabe; border-radius: 8px; } /* Adjusted border and background color for better contrast */
        </style>
    </head>
    <body>
     <h1>Upload a File</h1>
        <form action="/upload" method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Upload">
        </form>
        <h2>Uploaded Photos</h2>
        <ul>
        {% for file in files %}
            <li><a href="{{ url_for('uploaded_file', filename=file) }}">{{ file }}</a></li>
        {% endfor %}
        </ul>
        <h2>Chat</h2>
        <div id="chat">
            <div id="messages"></div>
            <form id="chat-form">
                <input type="text" id="message" placeholder="Type your message here..." required>
                <input type="submit" value="Send">
            </form>
        </div>
        <script>
            const socket = io();

            const form = document.getElementById('chat-form');
            const messageInput = document.getElementById('message');
            const messagesDiv = document.getElementById('messages');

            form.addEventListener('submit', function(e) {
                e.preventDefault();
                const message = messageInput.value;
                socket.emit('send_message', message);
                messageInput.value = '';
            });

            socket.on('receive_message', function(message) {
                const messageElement = document.createElement('div');
                messageElement.textContent = message;
                messagesDiv.appendChild(messageElement);
                messagesDiv.scrollTop = messagesDiv.scrollHeight; // Scroll to the bottom
            });
        </script>
    </body>
    </html>
    ''', files=files)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('index'))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@socketio.on('send_message')
def handle_message(message):
    print(f"Message received: {message}")
    emit('receive_message', message, broadcast=True)  # Broadcast message to all clients

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
