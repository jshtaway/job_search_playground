from locust import User, task

class MyFirstTest(User):
    @task
    def launch(self):
        print("Launching stuff, i mean, the URL")

    @task
    def search(self):
        print("Searching stuff")
    
    @task
    def pytest(self):
        test_tests.test_jsons()