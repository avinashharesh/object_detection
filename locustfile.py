import os
import json
import base64
from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 3)
    host = "http://130.162.193.76:30003"  # Replace with your Flask app's host and port

    @task
    def predict_images(self):
        # Path to the input folder containing images
        input_folder = "inputfolder"

        # Get list of image files from input folder
        image_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

        # List to store image data in the specified format
        images_data = []

        # Iterate over each image file
        for image_file in image_files:
            # Read image file as bytes
            with open(os.path.join(input_folder, image_file), "rb") as f:
                image_data = f.read()

            # Encode image bytes to base64
            image_base64 = base64.b64encode(image_data).decode("utf-8")

            # Append image data to the list
            images_data.append({
                "id": image_file,  # Use file name as ID
                "image": image_base64
            })

        # Define JSON payload with image data in the specified format
        payload = {"images": images_data}
        

        headers = {"Content-Type": "application/json"}

        # Send POST request to /predict endpoint
        response = self.client.post("/predict", data=json.dumps(payload), headers=headers)

        # Check response status code and content
        if response.status_code == 200:
            print("Predictions successful")
            print(response.json())
        else:
            print(f"Prediction failed with status code: {response.status_code}")

    def on_start(self):
        pass

    def on_stop(self):
        pass
