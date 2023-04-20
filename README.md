# Backend Queue Service

## Technology used: Flask (Python)


# Steps to run
1. Traverse to the project root directory using terminal and run:
    `pip install -r requirements.txt`
    `env FLASK_APP=app.py flask run`
2. The server is now running on localhost:5000. You can check the following methods and routes on Postman/Insomnia/etc.

    a. POST - localhost:5000/create_queue?name=<queue_name>
    
    b. POST - localhost:5000/send_message?name=<queue_name>
    
        - Body contains JSON message in the format 
        - 
            ` {"message" : "This is a demo message"} `
            
    c. GET - localhost:5000/read_message?name=<queue_name>
    
    d. DELETE - localhost:5000/delete_message?name=<queue_name>&msg_id=<message_index>

