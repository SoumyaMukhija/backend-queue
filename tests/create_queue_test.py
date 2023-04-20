import json
from flask import Flask
from collections import defaultdict
from flask_testing import TestCase
from __main__ import app, queues

class CreateQueueTests(TestCase):
    def create_app(self):
        app = Flask(__name__)
        return app

    def test_create_queue_success(self):
        response = self.client.post('/create_queue?name=test')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {"message": "The queue was created successfully!"})

    def test_create_queue_failure(self):
        response = self.client.post('/create_queue?name=test')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), {"message": "QSorry, a queue with that name already exists."})
