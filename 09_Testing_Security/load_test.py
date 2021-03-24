
import time
import json
from locust import HttpUser, task, between


test_data = json.dumps({"data": [[8.75, 0.83, 70, 259, 15.82, 1016.51, 1.0]]})
headers = {'Content-Type': 'application/json'}


class MLServiceUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def test_weather_predictions(self):
        self.client.post("", data=test_data, headers=headers)
