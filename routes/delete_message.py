from flask import request, jsonify

from app import app, queues

# End point to delete a msg from the queue. 
# Get queue name and message id from request params. Check for validity. If valid, remove that message (assuming message 
# id is the same as its 1-based index in the list).
@app.route('/delete_message', methods=['DELETE'])
def delete_message():
    queue_name = request.args.get('name')
    idx = request.args.get('msg_id')

    if queue_name not in queues:
        return jsonify({"message": "Sorry, a queue with that name does not exist."}), 400
    if idx >= len(queues[queue_name]):
        return jsonify({"message": "Sorry, that message ID is invalid."}), 400

    queues[queue_name].pop(idx)
    return jsonify({"message": "The message was deleted successfully!"}), 200