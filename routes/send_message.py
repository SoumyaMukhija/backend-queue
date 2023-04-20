from flask import request, jsonify

from app import app, queues

# End point for sending msg to a queue.
# Get queue name from args and msg from json body. Validate for empty msgs or invalid queue names. If everything is correct,
# append message to the queue with that name and return success.
@app.route('/send_message', methods=['POST'])
def send_message():
    queue_name = request.args.get('name')
    message = request.json.get('message')

    if not message:
        return jsonify({"message": "Sorry, you cannot send an empty msg to a queue."}), 400
    if queue_name not in queues:
        return jsonify({"message": "Sorry, the queue does not exist."}), 400

    queues[queue_name].append(message)
    return jsonify({"message": "Your message has been added successfully!"}), 200
