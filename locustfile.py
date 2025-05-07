from locust import HttpUser, task, between

class LoadTestUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def load_homepage(self):
        self.client.get("/")

    @task
    def load_api(self):
        self.client.get("/api")  # 

    @task(2)  
    def load_about(self):
        self.client.get("/about") 