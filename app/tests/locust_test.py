
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):

    @task
    def hello_world(self):
        self.client.get("/")
        #self.client.post("/token", json={"name":"yanki", "password":"pass1"})



#locust -f ./tests/locust_test.py
#http://localhost