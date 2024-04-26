import os
from locust import HttpUser, task, between
import base64

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)
    image_files = sorted(os.listdir("inputfolder"))
    image_index = 0

    @task(1)
    def predict_image(self):
        if self.image_index >= len(self.image_files):
            self.image_index = 0

        image_file = self.image_files[self.image_index]
        with open(os.path.join("inputfolder", image_file), "rb") as f:
            image_data = f.read()
        image_base64 = base64.b64encode(image_data).decode("utf-8")

        payload = {"id": "1", "image": image_base64}
        headers = {"Content-Type": "application/json"}

        self.client.post("/predict", json=payload, headers=headers)
        self.image_index += 1
