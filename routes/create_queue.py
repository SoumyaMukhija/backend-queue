from flask import request, jsonify

from app import app, queues

# End point for creating a new queue.
# Get queue name from the params, check if the name is unique. If it is, create a new list by that name and return success.
@app.route('/create_queue', methods=['POST'])
def create_queue():
    queue_name = request.args.get('name')

    if queue_name in queues:
        return jsonify({"message": "Sorry, a queue with that name already exists."}), 400

    queues[queue_name] = list()
    return jsonify({"message": "The queue was created successfully!"}), 200