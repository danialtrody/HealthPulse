from locust import HttpUser, task, between

class HealthPulseUser(HttpUser):
    host = "https://api.github.com"
    wait_time = between(1, 3)

    @task(3)
    def check_github(self):
        self.client.get("/")

    @task(2)
    def check_jsonplaceholder(self):
        self.client.get("/repos/python/cpython")

    @task(1)
    def check_rate_limit(self):
        self.client.get("/rate_limit")
        
# locust -f locustfile.py