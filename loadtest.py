from locust import HttpUser, task

class MyUser(HttpUser):
    host = "http://157.15.202.244:98"

    def on_start(self):
        self.client.post("/api/auth/login", json={
            "email": "Sk12@gmail.com",
            "password": "Sk@123"
        })




# locust -f loadtest.py

