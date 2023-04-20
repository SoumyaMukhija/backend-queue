from flask import request, jsonify

from app import app, queues

# Function for an end user to consume a message.
# Take queue name from req params, and if the name exists then consume/read it.
@app.route('/read_message')
def consume_msg():
    queue_name = request.args.get('name')
    if queue_name not in queues:
        return jsonify({"error": "Sorry, a queue with that name does not exist!"}), 400

    else:
        message = queues[queue_name].pop()
        return jsonify('Consuming message:' + message + 'from' + queue_name)