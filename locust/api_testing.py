from locust import HttpUser, task, between

class AppUser(HttpUser):
    wait_time = between(2,5)

    @task
    def index_page(self):
        self.client.get("/")