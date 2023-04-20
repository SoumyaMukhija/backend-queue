from flask import Flask
from collections import defaultdict

app = Flask(__name__)
queues = defaultdict(list)

if __name__ == '__main__':
    app.run(debug=True)

from routes import create_queue, delete_message, send_message, read_message
